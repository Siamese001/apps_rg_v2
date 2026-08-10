from __future__ import annotations

import json

from apps_model_telemetry.otel_runtime import (
    capture_collector_snapshot,
    configure_live_otel,
    verify_live_collector_receipt,
)


def test_live_otel_refuses_an_implicit_noop_provider(monkeypatch) -> None:
    monkeypatch.delenv("APPS_OTEL_EXPORTER_OTLP_ENDPOINT", raising=False)

    status = configure_live_otel(service_name="test")

    assert status.active is False
    assert status.reason == "OTLP_ENDPOINT_NOT_CONFIGURED"


def test_capture_collector_snapshot_selects_exact_trace_root(monkeypatch, tmp_path) -> None:
    source = tmp_path / "collector.json"
    source.write_text(
        json.dumps(
            {
                "resourceSpans": [
                    {
                        "name": "wanted",
                        "attributes": [
                            {"key": "trace.root", "value": {"stringValue": "trace-wanted"}}
                        ],
                    },
                    {"name": "other", "attributes": {"trace.root": "trace-other"}},
                ]
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setenv("APPS_OTEL_COLLECTOR_SPANS_FILE", str(source))

    snapshot = capture_collector_snapshot(
        artifact_dir=tmp_path / "run", trace_id="trace-wanted", timeout_seconds=0
    )

    assert snapshot["status"] == "CAPTURED"
    assert [row["name"] for row in snapshot["spans"]] == ["wanted"]
    assert (tmp_path / "run" / "otel_trace_snapshot.json").is_file()


def test_snapshot_reader_accepts_append_only_collector_documents(monkeypatch, tmp_path) -> None:
    source = tmp_path / "collector.jsonl"
    source.write_text(
        json.dumps({"name": "other", "attributes": {"trace.root": "trace-other"}})
        + "\n"
        + json.dumps({"name": "wanted", "attributes": {"trace.root": "trace-wanted"}})
        + "\n",
        encoding="utf-8",
    )
    monkeypatch.setenv("APPS_OTEL_COLLECTOR_SPANS_FILE", str(source))

    snapshot = capture_collector_snapshot(
        artifact_dir=tmp_path / "run", trace_id="trace-wanted", timeout_seconds=0
    )

    assert snapshot["status"] == "CAPTURED"
    assert [row["name"] for row in snapshot["spans"]] == ["wanted"]


def test_collector_preflight_blocks_without_a_runtime_exporter(monkeypatch, tmp_path) -> None:
    monkeypatch.delenv("APPS_OTEL_EXPORT_ACTIVE", raising=False)

    receipt = verify_live_collector_receipt(artifact_dir=tmp_path)

    assert receipt["status"] == "BLOCKED"
    assert receipt["reason"] == "OTEL_RUNTIME_NOT_ACTIVE"
    assert (tmp_path / "otel_collector_preflight.json").is_file()
