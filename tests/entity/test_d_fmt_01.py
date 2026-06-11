"""D-FMT-01 — VL-R4-001, VL-R4-002 (FR-FMT-01)."""

from validate_lines import validate_lines


def test_vl_r4_001_unknown_unit_fails():
    # Given — VL-R4-001: foo:1.0
    grid = [["foo:1.0"]]
    # When
    result = validate_lines(grid)
    # Then
    assert result["status"] == "fail"
    assert 0 in result["failed_lines"]


def test_vl_r4_002_missing_colon_fails():
    # Given — VL-R4-002: meter2.5 콜론 누락
    grid = [["meter2.5"]]
    # When
    result = validate_lines(grid)
    # Then
    assert result["status"] == "fail"
    assert result["failed_lines"] == [0]
