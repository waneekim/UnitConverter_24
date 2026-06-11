"""U-FLOW-01 — UI-FLOW-001 (단건 1입력 즉시 출력)."""

from UnitConverter import INPUT_PROMPT, process_input


def test_ui_flow_001_single_input_immediate_three_lines():
    lines, error = process_input("meter: 2.5")
    assert error is None
    assert len(lines) == 4
    assert all("meter: 2.5" in line for line in lines)


def test_ui_flow_002_single_prompt_is_one_line_instruction():
    assert "예:" in INPUT_PROMPT
    assert "batch" not in INPUT_PROMPT.lower()
    assert "빈 줄" not in INPUT_PROMPT
