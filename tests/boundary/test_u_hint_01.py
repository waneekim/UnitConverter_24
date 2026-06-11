"""U-HINT-01 — UI-HINT-001/002 (FR-IN-03 한국어 안내)."""

from UnitConverter import ERROR_INVALID_FORMAT, INPUT_PROMPT, process_input


def test_ui_hint_001_error_shows_korean_examples():
    lines, error = process_input("meter2.5")
    assert lines == []
    assert error == ERROR_INVALID_FORMAT
    assert "예:" in error
    assert "meter:2.5" in error


def test_ui_hint_002_prompt_korean_with_examples():
    assert "변환" in INPUT_PROMPT
    assert "예:" in INPUT_PROMPT
    assert "meter:2.5" in INPUT_PROMPT
