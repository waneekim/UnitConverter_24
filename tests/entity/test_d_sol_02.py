"""Golden Master — D-UNIT-01, D-UNIT-02, D-FMT-01, D-FMT-02, D-BATCH-01."""

from _approval import assert_matches_golden, format_golden
from fixtures import ARCH_3FT_6IN, ARCH_9FT_2IN, STEEL_DIMS_8
from validate_lines import validate_lines


def test_d_unit_01_vl_r2_001_golden():
    result = validate_lines([["feet:3", "yard:3"]])
    assert_matches_golden("VL-R2-001", format_golden(result))


def test_d_unit_02_vl_r2_002_golden():
    result = validate_lines([["meter:1.0", "feet:3.28084", "yard:1.0"]])
    assert_matches_golden("VL-R2-002", format_golden(result))


def test_d_fmt_01_vl_r4_001_golden():
    result = validate_lines([["foo:1.0"]])
    assert_matches_golden("VL-R4-001", format_golden(result))


def test_d_fmt_01_vl_r4_002_golden():
    result = validate_lines([["meter2.5"]])
    assert_matches_golden("VL-R4-002", format_golden(result))


def test_d_fmt_02_vl_r4_003_golden():
    result = validate_lines([[ARCH_3FT_6IN, ""]])
    assert_matches_golden("VL-R4-003", format_golden(result))


def test_d_batch_01_vl_r3_001_golden():
    result = validate_lines(STEEL_DIMS_8)
    assert_matches_golden("VL-R3-001", format_golden(result))


def test_d_batch_01_vl_r3_002_golden():
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
    result = validate_lines(grid)
    assert_matches_golden("VL-R3-002", format_golden(result))
