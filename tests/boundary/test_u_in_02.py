"""U-IN-02 — UI-R4-002 (FR-IN-02)."""

from UnitConverter import process_input


def test_ui_r4_002_unknown_unit_shows_error():
    # Given — UI-R4-002: foo:1.0 unknown unit
    # When
    lines, error = process_input("foo:1.0")
    # Then
    assert lines == []
    assert error == "Unknown unit: foo"
