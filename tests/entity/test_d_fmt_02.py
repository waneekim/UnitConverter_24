"""D-FMT-02 — VL-R4-003 (FR-FMT-02)."""

from fixtures import ARCH_3FT_6IN
from validate_lines import validate_lines


def test_vl_r4_003_empty_cell_incomplete():
    # Given — VL-R4-003: 빈 셀 → incomplete
    grid = [[ARCH_3FT_6IN, ""]]
    # When
    result = validate_lines(grid)
    # Then
    assert result["status"] == "incomplete"
    assert result["failed_lines"] == []
