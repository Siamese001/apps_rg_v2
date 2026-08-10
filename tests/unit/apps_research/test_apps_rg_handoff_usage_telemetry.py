from __future__ import annotations

import json
from pathlib import Path

from agentic_core.L3_orchestration.exit_eval.dimension import Dimension, GraderClass
from agentic_core.L3_orchestration.exit_eval.graders.llm_judge import JudgeResponse
from apps_model_telemetry.external_model_usage import LEDGER_FILENAME
from apps_research.integrations.apps_rg_handoff import (
    _AppsRgTargetingBriefGoogleJudge,
    run_apps_rg_handoff_x2_judge,
)


class _UsageReportingJudge:
    observed_model = "gemini-3.1-pro-preview"
    model_usage_attempts = [
        {
            "provider": "gemini_pro",
            "model": "gemini-3.1-pro-preview",
            "response_id": "response-1",
            "prompt_tokens": 100,
            "output_tokens": 50,
            "thought_tokens": 25,
            "cached_tokens": 0,
            "cache_write_tokens": None,
            "total_tokens": 175,
        }
    ]

    def judge(self, _dimension, _context):
        return JudgeResponse(score=0.91, abstain=False, reasoning="supported")


def test_x2_receipt_carries_safe_provider_usage_metadata() -> None:
    receipt = run_apps_rg_handoff_x2_judge(
        brief_text="## Company Thesis\n- Proven evidence.",
        jd_text="Lead partner architecture.",
        research_notes="Verified partner motion.",
        source_register=[{"family": "overview", "has_content": True}],
        judge=_UsageReportingJudge(),
    )

    assert receipt["status"] == "PASS"
    assert receipt["model_usage_attempts"] == _UsageReportingJudge.model_usage_attempts


def test_x2_blocks_an_oversize_input_before_calling_the_judge(monkeypatch) -> None:
    monkeypatch.setenv("APPS_RESEARCH_X2_MAX_INPUT_TOKENS", "1024")

    receipt = run_apps_rg_handoff_x2_judge(
        brief_text="x" * 4_000,
        jd_text="Lead partner architecture.",
        research_notes="Verified partner motion.",
        judge=_UsageReportingJudge(),
    )

    assert receipt["provider_status"] == "BLOCKED_TOKEN_BUDGET"
    assert receipt["attempt_count"] == 0
    assert receipt["model_usage_attempts"] == []


def test_google_x2_usage_is_appended_to_a_bound_run_ledger(
    monkeypatch,
    tmp_path: Path,
) -> None:
    judge = _AppsRgTargetingBriefGoogleJudge(
        model="gemini-3.1-pro-preview",
        api_key="test-key",
        usage_artifact_dir=tmp_path,
    )
    raw = {
        "responseId": "gemini-response-1",
        "modelVersion": "gemini-3.1-pro-preview",
        "usageMetadata": {
            "promptTokenCount": 101,
            "candidatesTokenCount": 21,
            "thoughtsTokenCount": 13,
            "totalTokenCount": 135,
        },
        "candidates": [
            {
                "content": {
                    "parts": [
                        {"text": '{"verdict": "PASS", "score": 0.91, "reasoning": "ok"}'}
                    ]
                }
            }
        ],
    }
    class _Response:
        def read(self) -> bytes:
            return json.dumps(raw).encode("utf-8")

        def __enter__(self):
            return self

        def __exit__(self, *_args) -> bool:
            return False

    monkeypatch.setattr(
        "apps_research.integrations.apps_rg_handoff.urllib.request.urlopen",
        lambda _request, timeout: _Response(),
    )

    response = judge.judge(
        Dimension(
            name="faithfulness",
            grader_class=GraderClass.MODEL_BASED,
            threshold=0.75,
            is_hard_gate=True,
            abstain_allowed=True,
        ),
        {
            "brief_text": "## Company Thesis\n- Evidence.",
            "jd_text": "Lead partner architecture.",
            "research_notes": "Verified partner motion.",
            "source_register": [],
        },
    )

    assert response.score == 0.91
    events = [
        json.loads(line)
        for line in (tmp_path / LEDGER_FILENAME).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    event = next(event for event in events if event["outcome"] == "SUCCESS")
    assert event["provider"] == "gemini_pro"
    assert event["prompt_tokens"] == 101
    assert event["thought_tokens"] == 13
    assert event["total_tokens"] == 135
    assert "Company Thesis" not in json.dumps(event)
