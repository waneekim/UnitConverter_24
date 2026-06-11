"""D-LOC-01 Golden Master — Approval Test (VL-R1-001 ~ VL-R1-002)."""

from _approval import assert_matches_golden, format_golden
from fixtures import ARCH_3FT_6IN
from validate_lines import validate_lines


def test_d_loc_01_step_a_success():
    """VL-R1-001 / FR-LOC-02 — 건축 표기 단독 pass."""
    result = validate_lines([[ARCH_3FT_6IN]])
    assert_matches_golden("VL-R1-001", format_golden(result))


def test_d_loc_01_step_b_misconversion_fail():
    """VL-R1-002 / FR-LOC-01 — feet:3.5 오환산 fail."""
    result = validate_lines([[ARCH_3FT_6IN, "feet:3.5"]])
    assert_matches_golden("VL-R1-002", format_golden(result))
