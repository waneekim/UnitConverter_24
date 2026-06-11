"""U-HINT-02 — UI-R7-005 (FR-IN-04 단건 vs 일괄 한 줄 안내)."""

from UnitConverter import INPUT_PROMPT, SINGLE_MODE_HINT


def test_ui_r7_005_single_hint_mentions_batch_and_empty_line():
    assert "--batch" in SINGLE_MODE_HINT
    assert "빈 줄" in SINGLE_MODE_HINT


def test_ui_r7_006_single_prompt_stays_one_line_no_batch_noise():
    assert "예:" in INPUT_PROMPT
    assert "빈 줄" not in INPUT_PROMPT
