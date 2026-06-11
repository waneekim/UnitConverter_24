"""Golden Master — Mom Test R3 UI (U-FLOW, U-SINGLE)."""

from _approval import assert_matches_golden, format_ui_golden
from UnitConverter import process_input


def test_u_flow_01_ui_flow_001_golden():
    lines, error = process_input("meter: 2.5")
    assert_matches_golden("UI-FLOW-001", format_ui_golden(lines, error))
