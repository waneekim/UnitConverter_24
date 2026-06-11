"""D-UNIT-02 — VL-R2-002 (FR-UNIT-02)."""

from validate_lines import validate_lines


def test_vl_r2_002_meter_feet_yard_inconsistent_fails():
    # Given — VL-R2-002: meter 기준 yard 비율 불일치
    grid = [["meter:1.0", "feet:3.28084", "yard:1.0"]]
    # When
    result = validate_lines(grid)
    # Then
    assert result["status"] == "fail"
    assert result["failed_lines"] == [0]
