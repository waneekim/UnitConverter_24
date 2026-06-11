"""Golden Master — D-UNIT-03/04 (cm/mm/inch)."""

from _approval import assert_matches_golden, format_conversion_golden
from convert_length import convert_length


def test_cl_r7_001_golden_cm():
    result = convert_length("cm:100")
    assert_matches_golden("CL-R7-001", format_conversion_golden(result))


def test_cl_r7_004_golden_cm_to_inch():
    result = convert_length("cm:2.54")
    assert_matches_golden("CL-R7-004", format_conversion_golden(result))
