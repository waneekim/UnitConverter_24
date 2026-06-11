"""Golden Master — Mom Test R7 UI (U-OUT-02)."""

from _approval import assert_matches_golden, format_ui_golden
from UnitConverter import process_input


def test_u_out_02_ui_r7_001_golden():
    lines, error = process_input("cm:2.54")
    assert_matches_golden("UI-R7-001", format_ui_golden(lines, error))
