"""U-BATCH-02 — UI-R7-003 (FR-BATCH-03 일괄 모드 발견·빈 줄 힌트)."""

from UnitConverter import BATCH_INTRO, BATCH_PROMPT


def test_ui_r7_003_batch_intro_mentions_batch_flag():
    assert "--batch" in BATCH_INTRO
    assert "일괄" in BATCH_INTRO


def test_ui_r7_004_batch_prompt_mentions_empty_line_end():
    assert "빈 줄" in BATCH_PROMPT
