"""D-LOC-01 — VL-R1-001 ~ VL-R1-002 (FR-LOC-01 · FR-LOC-02)."""

from fixtures import ARCH_3FT_6IN
from validate_lines import validate_lines


def test_vl_r1_001_arch_notation_3ft_6in_passes():
    # Given — VL-R1-001 / FR-LOC-02: grid=[[ARCH_3FT_6IN]]
    grid = [[ARCH_3FT_6IN]]
    # When
    result = validate_lines(grid)
    # Then
    assert result["status"] == "pass"
    assert result["failed_lines"] == []


def test_vl_r1_002_feet_3_5_misrepresents_3ft_6in_fails():
    # Given — VL-R1-002 / FR-LOC-01: grid=[[ARCH_3FT_6IN, "feet:3.5"]]
    grid = [[ARCH_3FT_6IN, "feet:3.5"]]
    # When
    result = validate_lines(grid)
    # Then
    assert result["status"] == "fail"
    assert result["failed_lines"] == [0]
