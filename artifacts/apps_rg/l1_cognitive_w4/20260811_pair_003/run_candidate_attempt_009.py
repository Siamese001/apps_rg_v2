"""Retained launcher for non-product Apps RG L1 cognitive candidate attempt 009."""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "src"))
from apps_rg.evals.l1_cognitive_shadow_runner import run_l1_cognitive_shadow_arm
from apps_rg.runtime.bindings.l1_cognitive_treatment import (
    L1_COGNITIVE_V3_CANDIDATE_ARM,
)


CAMPAIGN = Path(__file__).resolve().parent

result = run_l1_cognitive_shadow_arm(
    artifact_dir=CAMPAIGN / "candidate_attempt_009",
    target_company="Lincoln Financial Group",
    target_role="SVP IT Strategy & AI Enablement",
    target_level="EXECUTIVE",
    generation_mode="strategic_tailor",
    jd_path=(
        ROOT
        / "docs"
        / "reports"
        / "apps_rg"
        / "fixtures"
        / "senior_roles"
        / "lincoln_insurer_it_ai_jd.txt"
    ),
    briefing_path=(
        ROOT
        / "docs"
        / "reports"
        / "apps_rg"
        / "fixtures"
        / "senior_roles"
        / "lincoln_insurer_it_ai_brief.txt"
    ),
    resume_path=ROOT / "src" / "apps_rg" / "resume" / "base" / "amit_ayer_base_resume_v1.json",
    treatment_arm=L1_COGNITIVE_V3_CANDIDATE_ARM,
    repo_root=ROOT,
    allow_nonproduct_provider_preflight_disable=True,
)
print(json.dumps(result, indent=2, sort_keys=True))
