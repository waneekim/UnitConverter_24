"""Golden Master — U-IN-01, U-IN-02 (UI boundary)."""

from _approval import assert_matches_golden, format_ui_golden
from UnitConverter import process_input


def test_u_in_01_ui_r4_001_golden():
    lines, error = process_input("meter2.5")
    assert_matches_golden("UI-R4-001", format_ui_golden(lines, error))


def test_u_in_02_ui_r4_002_golden():
    lines, error = process_input("foo:1.0")
    assert_matches_golden("UI-R4-002", format_ui_golden(lines, error))
