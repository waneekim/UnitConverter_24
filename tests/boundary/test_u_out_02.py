"""U-OUT-02 — UI-R7-001/002 (FR-OUT-03 CLI inch 줄 출력)."""

from UnitConverter import process_input


def test_ui_r7_001_cm254_outputs_inch_line():
    # Given — Mom Test R7: cm:254 → inch 발주 숫자 필요
    lines, error = process_input("cm:2.54")
    # Then
    assert error is None
    assert len(lines) == 4
    inch_lines = [line for line in lines if "inch" in line]
    assert len(inch_lines) == 1
    assert "1.0" in inch_lines[0]


def test_ui_r7_002_cm254_outputs_hundred_inch():
    lines, error = process_input("cm:254")
    assert error is None
    inch_line = next(line for line in lines if "inch" in line)
    assert "100" in inch_line
