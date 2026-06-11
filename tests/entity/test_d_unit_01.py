"""D-UNIT-01 — VL-R2-001 (FR-UNIT-01)."""

from validate_lines import validate_lines


def test_vl_r2_001_feet_yard_same_value_fails():
    # Given — VL-R2-001: feet:3 + yard:3 동일 수치 → 단위 혼동 fail
    grid = [["feet:3", "yard:3"]]
    # When
    result = validate_lines(grid)
    # Then
    assert result["status"] == "fail"
    assert result["failed_lines"] == [0]
