"""U-IN-01 — UI-R4-001 (FR-IN-01)."""

from UnitConverter import process_input

ERROR_INVALID_FORMAT = "Invalid format. Use unit:value (ex: meter:2.5)"


def test_ui_r4_001_missing_colon_shows_error():
    # Given — UI-R4-001: meter2.5 stdin 콜론 누락
    # When
    lines, error = process_input("meter2.5")
    # Then
    assert lines == []
    assert error == ERROR_INVALID_FORMAT
