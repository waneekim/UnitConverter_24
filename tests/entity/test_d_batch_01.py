"""D-BATCH-01 — VL-R3-001, VL-R3-002 (FR-BATCH-01)."""

from fixtures import ARCH_3FT_6IN, ARCH_9FT_2IN, STEEL_DIMS_8
from validate_lines import validate_lines


def test_vl_r3_001_steel_dims_8_passes():
    # Given — VL-R3-001: STEEL_DIMS_8 일괄 pass
    # When
    result = validate_lines(STEEL_DIMS_8)
    # Then
    assert result["status"] == "pass"
    assert result["failed_lines"] == []


def test_vl_r3_002_steel_dims_one_misconversion_fails():
    # Given — VL-R3-002: row 4 feet:3.5 오환산
    grid = [
        [ARCH_3FT_6IN],
        [ARCH_9FT_2IN],
        ['12\'-0"'],
        ['6\'-8"'],
        ["feet:3.5"],
        ['10\'-6"'],
        ['8\'-3"'],
        ['5\'-4"'],
    ]
    # When
    result = validate_lines(grid)
    # Then
    assert result["status"] == "fail"
    assert result["failed_lines"] == [4]
