"""Focused contract tests for the one public Apps RG resume pipeline."""

from __future__ import annotations

from apps_rg.bare_pipeline import _validate_outreach_email, _validate_tailored_resume


def _complete_resume() -> str:
    return """# Ada Candidate
ada@example.com

## EXECUTIVE SUMMARY
Executive AI leader.

## CORE COMPETENCIES
- Partnerships

## PROFESSIONAL EXPERIENCE
### Acme Corp — Remote
**VP Engineering** | 2020–Present
- Built a platform.

### Earlier Co — Remote
**Director** | 2017–2020
- Led delivery.

## TECHNICAL EXPERTISE
Cloud platforms.

## EDUCATION
**MS, Computer Science** — Example University

## CERTIFICATIONS
- Example Certification
""" + ("\nEvidence-backed delivery." * 60)


def test_x1_requires_every_resume_section_and_source_employer() -> None:
    result = _validate_tailored_resume(
        _complete_resume(),
        required_employers=("Acme Corp", "Earlier Co"),
    )

    assert result["status"] == "PASS"
    assert result["missing"] == []
    assert result["checks"]["employers"] == {"Acme Corp": True, "Earlier Co": True}


def test_x1_rejects_a_resume_missing_a_required_section() -> None:
    incomplete = _complete_resume().replace("## CERTIFICATIONS\n- Example Certification\n", "")

    result = _validate_tailored_resume(incomplete, required_employers=("Acme Corp", "Earlier Co"))

    assert result["status"] == "FAIL"
    assert "heading:CERTIFICATIONS" in result["missing"]


def test_x1_requires_a_targeted_email_with_subject() -> None:
    result = _validate_outreach_email(
        """Subject: Applied AI Partnerships

Hello Anthropic Hiring Team,

I am writing about the Manager of Applied AI Architecture, Partnerships role at Anthropic.
""",
        company="Anthropic",
        role="Manager of Applied AI Architecture, Partnerships",
    )

    assert result["status"] == "PASS"
    assert result["missing"] == []
