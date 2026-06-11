"""Golden Master — convert_length / convert_lengths."""

from _approval import assert_matches_golden, format_conversion_golden
from fixtures import ARCH_3FT_6IN, STEEL_DIMS_8
from convert_length import convert_length, convert_lengths


def test_cl_r1_001_golden():
    result = convert_length(ARCH_3FT_6IN)
    assert_matches_golden("CL-R1-001", format_conversion_golden(result))


def test_cl_batch_001_golden():
    specs = [row[0] for row in STEEL_DIMS_8]
    results = convert_lengths(specs)
    combined = "\n---\n".join(format_conversion_golden(r) for r in results)
    assert_matches_golden("CL-BATCH-001", combined)


def test_cl_out_001_golden():
    result = convert_length("10'-6\"")
    assert_matches_golden("CL-OUT-001", format_conversion_golden(result))
