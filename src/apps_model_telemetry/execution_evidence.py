"""Provider-attempt evidence that is safe to persist and mirror to OpenTelemetry.

This module deliberately does not decide provider routing.  It establishes the
minimum evidence vocabulary needed to say what happened to a model call without
inventing a remote outcome after a client-side timeout.
"""

from __future__ import annotations

import contextlib
import hashlib
import json
import os
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Iterator, Mapping

from apps_model_telemetry.external_model_usage import append_external_model_usage


ATTEMPT_STARTED = "ATTEMPT_STARTED"
ATTEMPT_FINISHED = "ATTEMPT_FINISHED"
REMOTE_OUTCOME_UNKNOWN = "REMOTE_OUTCOME_UNKNOWN"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _safe_digest(value: Mapping[str, Any]) -> str:
    return hashlib.sha256(
        json.dumps(dict(value), sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _tracer() -> Any | None:
    """Return a tracer only when an application configured a real exporter.

    Importing the OpenTelemetry API alone creates a no-op provider.  Treating
    that as execution evidence is the failure mode this module prevents.
    """

    if os.environ.get("APPS_OTEL_EXPORT_ACTIVE", "").strip() != "1":
        return None
    try:
        from opentelemetry import trace

        return trace.get_tracer("apps_model_telemetry.provider_attempt")
    except ImportError:
        return None


@dataclass
class ProviderAttempt:
    """One local model-call attempt and its externally observable boundary."""

    artifact_dir: str | None
    run_id: str
    trace_id: str
    app_id: str
    stage: str
    section_id: str
    provider: str
    requested_model: str
    request_digest: str
    attempt_id: str = field(default_factory=lambda: f"attempt-{uuid.uuid4().hex}")
    started_at_utc: str = field(default_factory=_now)
    local_dispatch_started: bool = False
    request_written: bool = False
    response_headers_received: bool = False
    first_byte_received: bool = False
    observed_model: str = ""
    provider_response_id: str = ""
    http_status_code: int | None = None
    failure_phase: str = ""
    remote_outcome: str = ""
    error_class: str = ""
    _span: Any | None = field(default=None, init=False, repr=False)

    def _event(self, phase: str, **extra: Any) -> None:
        # The existing usage ledger is append-only and fsyncs every row.  It is
        # a local witness, never a substitute for an OTel collector receipt.
        append_external_model_usage(
            artifact_dir=self.artifact_dir,
            provider=self.provider,
            model=self.observed_model or self.requested_model,
            request_digest=self.request_digest,
            outcome=phase,
            provider_status=self.remote_outcome,
            run_id=self.run_id,
            stage=self.stage,
            section_id=self.section_id,
            logical_attempt=1,
            transport_attempt=1,
            response_id=self.provider_response_id,
            raw_response_ref="",
            evidence_event=phase,
            attempt_id=self.attempt_id,
            trace_id=self.trace_id,
            app_id=self.app_id,
            requested_model=self.requested_model,
            observed_model=self.observed_model,
            request_written=self.request_written,
            response_headers_received=self.response_headers_received,
            first_byte_received=self.first_byte_received,
            http_status_code=self.http_status_code,
            failure_phase=self.failure_phase,
            remote_outcome=self.remote_outcome,
            error_class=self.error_class,
            evidence_digest=_safe_digest(
                {
                    "attempt_id": self.attempt_id,
                    "phase": phase,
                    "request_digest": self.request_digest,
                    "trace_id": self.trace_id,
                    **extra,
                }
            ),
        )
        if self._span is not None:
            self._span.add_event(phase, attributes={k: str(v) for k, v in extra.items()})

    def mark_request_written(self) -> None:
        self.request_written = True
        self._event("REQUEST_WRITTEN")

    def mark_local_dispatch_started(self) -> None:
        """Record SDK entry when the library cannot expose a socket write hook."""

        self.local_dispatch_started = True
        self._event("LOCAL_DISPATCH_STARTED")

    def mark_response_headers(
        self, *, status_code: int | None = None, provider_response_id: str = ""
    ) -> None:
        self.response_headers_received = True
        self.http_status_code = status_code
        self.provider_response_id = provider_response_id or self.provider_response_id
        self._event("RESPONSE_HEADERS_RECEIVED")

    def mark_first_byte(self) -> None:
        self.first_byte_received = True
        self._event("FIRST_BYTE_RECEIVED")

    def finish(
        self,
        *,
        observed_model: str = "",
        provider_response_id: str = "",
        http_status_code: int | None = None,
        failure_phase: str = "",
        error_class: str = "",
        remote_outcome: str = "",
    ) -> None:
        self.observed_model = observed_model or self.observed_model
        self.provider_response_id = provider_response_id or self.provider_response_id
        self.http_status_code = http_status_code if http_status_code is not None else self.http_status_code
        self.failure_phase = failure_phase or self.failure_phase
        self.error_class = error_class or self.error_class
        if remote_outcome:
            self.remote_outcome = remote_outcome
        elif self.failure_phase and not self.response_headers_received:
            self.remote_outcome = REMOTE_OUTCOME_UNKNOWN
        elif self.response_headers_received:
            self.remote_outcome = "PROVIDER_RESPONDED"
        else:
            self.remote_outcome = "LOCAL_OUTCOME_ONLY"
        self._event(ATTEMPT_FINISHED)
        if self._span is not None:
            for key, value in self.attributes().items():
                if value is not None and value != "":
                    self._span.set_attribute(key, value)

    def attributes(self) -> dict[str, Any]:
        return {
            "attempt.id": self.attempt_id,
            "app.id": self.app_id,
            "run.id": self.run_id,
            "trace.root": self.trace_id,
            "stage": self.stage,
            "section.id": self.section_id,
            "provider": self.provider,
            "model.requested": self.requested_model,
            "model.observed": self.observed_model,
            "request.digest": self.request_digest,
            "request.written": self.request_written,
            "local.dispatch_started": self.local_dispatch_started,
            "response.headers_received": self.response_headers_received,
            "response.first_byte_received": self.first_byte_received,
            "response.id": self.provider_response_id,
            "http.status_code": self.http_status_code,
            "failure.phase": self.failure_phase,
            "remote.outcome": self.remote_outcome,
            "error.class": self.error_class,
        }


@contextlib.contextmanager
def provider_attempt(
    *,
    artifact_dir: str | None,
    run_id: str,
    trace_id: str,
    app_id: str,
    stage: str,
    section_id: str,
    provider: str,
    requested_model: str,
    request_digest: str,
) -> Iterator[ProviderAttempt]:
    """Write start/finish witnesses and mirror one safe OTel span when active."""

    attempt = ProviderAttempt(
        artifact_dir=artifact_dir,
        run_id=run_id,
        trace_id=trace_id,
        app_id=app_id,
        stage=stage,
        section_id=section_id,
        provider=provider,
        requested_model=requested_model,
        request_digest=request_digest,
    )
    tracer = _tracer()
    cm = (
        tracer.start_as_current_span("apps.model.provider_attempt")
        if tracer is not None
        else contextlib.nullcontext(None)
    )
    with cm as span:
        attempt._span = span
        if span is not None:
            for key, value in attempt.attributes().items():
                if value is not None and value != "":
                    span.set_attribute(key, value)
        attempt._event(ATTEMPT_STARTED)
        try:
            yield attempt
        except BaseException as exc:
            attempt.finish(
                failure_phase=attempt.failure_phase or "CLIENT_EXCEPTION",
                error_class=type(exc).__name__,
            )
            raise
        else:
            if not attempt.remote_outcome:
                attempt.finish()


__all__ = [
    "ATTEMPT_FINISHED",
    "ATTEMPT_STARTED",
    "REMOTE_OUTCOME_UNKNOWN",
    "ProviderAttempt",
    "provider_attempt",
]
