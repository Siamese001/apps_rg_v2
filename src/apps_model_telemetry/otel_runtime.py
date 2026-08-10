"""Minimal OTLP runtime bootstrap and collector-snapshot capture for live runs."""

from __future__ import annotations

import json
import os
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping


OTEL_ENDPOINT_ENV = "APPS_OTEL_EXPORTER_OTLP_ENDPOINT"
OTEL_SNAPSHOT_FILE_ENV = "APPS_OTEL_COLLECTOR_SPANS_FILE"
OTEL_ACTIVE_ENV = "APPS_OTEL_EXPORT_ACTIVE"


@dataclass(frozen=True)
class OTelRuntimeStatus:
    active: bool
    endpoint: str
    reason: str


_provider_configured = False
_provider: Any | None = None


def configure_live_otel(*, service_name: str, endpoint: str | None = None) -> OTelRuntimeStatus:
    """Configure OTLP only with an explicit collector endpoint."""

    global _provider_configured, _provider
    target = str(endpoint or os.environ.get(OTEL_ENDPOINT_ENV) or "").strip()
    if not target:
        os.environ.pop(OTEL_ACTIVE_ENV, None)
        return OTelRuntimeStatus(False, "", "OTLP_ENDPOINT_NOT_CONFIGURED")
    if _provider_configured:
        os.environ[OTEL_ACTIVE_ENV] = "1"
        return OTelRuntimeStatus(True, target, "ALREADY_CONFIGURED")
    try:
        from opentelemetry import trace
        from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
        from opentelemetry.sdk.resources import Resource
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import BatchSpanProcessor
    except ImportError:
        os.environ.pop(OTEL_ACTIVE_ENV, None)
        return OTelRuntimeStatus(False, target, "OTEL_SDK_UNAVAILABLE")
    provider = TracerProvider(resource=Resource.create({"service.name": service_name}))
    provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=target)))
    trace.set_tracer_provider(provider)
    _provider = provider
    _provider_configured = True
    os.environ[OTEL_ACTIVE_ENV] = "1"
    return OTelRuntimeStatus(True, target, "CONFIGURED")


def flush_live_otel() -> bool:
    return bool(_provider is not None and _provider.force_flush(timeout_millis=10_000))


def _walk(value: Any) -> list[Mapping[str, Any]]:
    if isinstance(value, Mapping):
        rows = [value]
        for child in value.values():
            rows.extend(_walk(child))
        return rows
    if isinstance(value, list):
        rows: list[Mapping[str, Any]] = []
        for child in value:
            rows.extend(_walk(child))
        return rows
    return []


def _attribute_value(value: Any) -> Any:
    if not isinstance(value, Mapping):
        return value
    for key in ("stringValue", "intValue", "doubleValue", "boolValue"):
        if key in value:
            return value[key]
    return value


def _attributes(row: Mapping[str, Any]) -> dict[str, Any]:
    raw = row.get("attributes")
    if isinstance(raw, Mapping):
        return {str(key): _attribute_value(value) for key, value in raw.items()}
    if isinstance(raw, list):
        return {
            str(item.get("key") or ""): _attribute_value(item.get("value"))
            for item in raw
            if isinstance(item, Mapping) and str(item.get("key") or "")
        }
    return {}


def capture_collector_snapshot(
    *,
    artifact_dir: Path,
    trace_id: str,
    timeout_seconds: float = 10.0,
    filename: str = "otel_trace_snapshot.json",
) -> dict[str, Any]:
    """Persist only collector spans correlated to an exact trace root."""

    source_text = str(os.environ.get(OTEL_SNAPSHOT_FILE_ENV) or "").strip()
    target = Path(artifact_dir) / filename
    target.parent.mkdir(parents=True, exist_ok=True)
    result: dict[str, Any] = {
        "schema_version": "apps.otel_trace_snapshot.v1",
        "trace_id": trace_id,
        "collector_source": source_text,
        "status": "UNAVAILABLE",
        "spans": [],
    }
    if source_text:
        deadline = time.monotonic() + max(0.0, timeout_seconds)
        source = Path(source_text)
        while time.monotonic() <= deadline:
            try:
                text = source.read_text(encoding="utf-8")
                # The collector file exporter appends one OTLP JSON document per
                # export.  Accept a conventional single JSON document too.
                documents = [json.loads(line) for line in text.splitlines() if line.strip()]
                raw: Any = documents[0] if len(documents) == 1 else documents
            except (OSError, json.JSONDecodeError):
                time.sleep(0.2)
                continue
            matches: list[dict[str, Any]] = []
            for row in _walk(raw):
                attrs = _attributes(row)
                ids = {
                    str(row.get("traceId") or ""),
                    str(row.get("trace_id") or ""),
                    str(attrs.get("trace.root") or ""),
                    str(attrs.get("trace_id") or ""),
                }
                if trace_id and trace_id in ids and ("name" in row or "spanId" in row):
                    matches.append(dict(row))
            if matches:
                result.update({"status": "CAPTURED", "spans": matches})
                break
            time.sleep(0.2)
    target.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def verify_live_collector_receipt(
    *, artifact_dir: Path, timeout_seconds: float = 10.0
) -> dict[str, Any]:
    """Prove that this process can export a fresh marker to the configured collector.

    An endpoint alone is configuration, not an operational receipt.  The marker is
    random for every run, so a stale collector file cannot satisfy this check.
    """

    marker = f"otel-preflight-{uuid.uuid4().hex}"
    receipt: dict[str, Any] = {
        "schema_version": "apps.otel_collector_preflight.v1",
        "marker": marker,
        "status": "BLOCKED",
        "reason": "OTEL_RUNTIME_NOT_ACTIVE",
    }
    if os.environ.get(OTEL_ACTIVE_ENV) != "1":
        _write_collector_preflight(artifact_dir, receipt)
        return receipt
    try:
        from opentelemetry import trace

        tracer = trace.get_tracer("apps.model.telemetry_preflight")
        with tracer.start_as_current_span("apps.model.collector_preflight") as span:
            span.set_attribute("trace.root", marker)
            span.set_attribute("evidence.kind", "collector_preflight")
        flushed = flush_live_otel()
    except Exception as exc:  # telemetry must make the launch decision explicit
        receipt.update({"reason": "OTEL_MARKER_EMIT_FAILED", "error_class": type(exc).__name__})
        _write_collector_preflight(artifact_dir, receipt)
        return receipt
    snapshot = capture_collector_snapshot(
        artifact_dir=artifact_dir,
        trace_id=marker,
        timeout_seconds=timeout_seconds,
        filename="otel_preflight_snapshot.json",
    )
    receipt.update(
        {
            "flush_succeeded": flushed,
            "snapshot": "otel_preflight_snapshot.json",
            "matched_spans": len(snapshot.get("spans") or []),
            "status": "PASS" if flushed and snapshot.get("status") == "CAPTURED" else "BLOCKED",
            "reason": "COLLECTOR_MARKER_CAPTURED"
            if flushed and snapshot.get("status") == "CAPTURED"
            else "COLLECTOR_MARKER_NOT_CAPTURED",
        }
    )
    _write_collector_preflight(artifact_dir, receipt)
    return receipt


def _write_collector_preflight(artifact_dir: Path, receipt: Mapping[str, Any]) -> None:
    target = Path(artifact_dir) / "otel_collector_preflight.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(dict(receipt), indent=2, sort_keys=True) + "\n", encoding="utf-8")


__all__ = [
    "OTEL_ACTIVE_ENV", "OTEL_ENDPOINT_ENV", "OTEL_SNAPSHOT_FILE_ENV", "OTelRuntimeStatus",
    "capture_collector_snapshot", "configure_live_otel", "flush_live_otel",
    "verify_live_collector_receipt",
]
