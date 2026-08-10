"""Whole-résumé flatten text — gap placeholders for incomplete sections."""

from __future__ import annotations

from apps_rg.runtime.assembly.full_resume_text import flatten_final_resume_to_text


def test_flatten_emits_not_completed_markers_when_sections_empty() -> None:
    text = flatten_final_resume_to_text(
        {
            "candidate_identity": {"candidate_name": "Test Candidate", "header_contact": {}},
            "sections": [],
        }
    )
    assert "[NOT COMPLETED: headline — missing_or_empty_headline]" in text
    assert "[NOT COMPLETED: insurtech — missing_generated_role_section]" in text
    assert "[NOT COMPLETED: competencies —" in text


def test_generated_role_omits_bullet_that_repeats_narrative_verbatim() -> None:
    narrative = "Led AWS modernization for regulated insurance platforms."
    text = flatten_final_resume_to_text(
        {
            "candidate_identity": {"candidate_name": "Test Candidate", "header_contact": {}},
            "sections": [
                {
                    "section_id": "insurtech_narrative",
                    "assemble_order": 1,
                    "l2_output_snapshot": {
                        "insurtech_header": {"employer": "InsurTech", "title": "CTO"},
                        "narrative_sentence": narrative,
                    },
                },
                {
                    "section_id": "insurtech_bullets",
                    "assemble_order": 2,
                    "l2_output_snapshot": {
                        "bullets": [
                            {"bullet_text": narrative},
                            {"bullet_text": "Built a governed migration delivery model."},
                        ]
                    },
                },
            ],
        }
    )

    assert text.count(narrative) == 1
    assert "• Built a governed migration delivery model." in text
