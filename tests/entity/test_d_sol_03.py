"""Golden Master — D-FMT-03 (분수 인치)."""

from _approval import assert_matches_golden, format_conversion_golden
from fixtures import ARCH_2QUARTER_IN, ARCH_4HALF_IN
from convert_length import convert_length


def test_cl_r5_001_golden():
    result = convert_length(ARCH_4HALF_IN)
    assert_matches_golden("CL-R5-001", format_conversion_golden(result))


def test_cl_r5_002_golden():
    result = convert_length(ARCH_2QUARTER_IN)
    assert_matches_golden("CL-R5-002", format_conversion_golden(result))
