"""U-SINGLE-01 — UI-SINGLE-001 (--batch 일괄 모드 분리)."""

from UnitConverter import BATCH_PROMPT, is_batch_mode


def test_ui_single_001_default_is_not_batch_mode():
    assert is_batch_mode([]) is False
    assert is_batch_mode(["UnitConverter.py"]) is False


def test_ui_single_002_batch_flag_enables_batch_mode():
    assert is_batch_mode(["UnitConverter.py", "--batch"]) is True


def test_ui_single_003_batch_prompt_only_for_batch_mode():
    assert "빈 줄" in BATCH_PROMPT
