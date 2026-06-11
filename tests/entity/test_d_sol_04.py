"""Golden Master — D-FMT-04 (콜론 뒤 공백)."""

from _approval import assert_matches_golden, format_conversion_golden
from convert_length import convert_length


def test_cl_r6_001_golden():
    result = convert_length("meter: 2.5")
    assert_matches_golden("CL-R6-001", format_conversion_golden(result))
