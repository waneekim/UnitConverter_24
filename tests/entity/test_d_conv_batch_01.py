"""D-CONV-BATCH-01 — convert_lengths 일괄 (FR-BATCH 연계)."""

from fixtures import ARCH_3FT_6IN, STEEL_DIMS_8
from convert_length import convert_lengths


def test_cl_batch_001_eight_arch_specs():
    # Given — 8개 철골 건축 표기 1 Command
    specs = [row[0] for row in STEEL_DIMS_8]
    # When
    results = convert_lengths(specs)
    # Then
    assert len(results) == 8
    assert results[0].feet_decimal == 3.75
    assert results[0].input_spec == ARCH_3FT_6IN
