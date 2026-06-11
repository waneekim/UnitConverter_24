"""D-FMT-03 — CL-R5-001/002 (FR-FMT-03 분수 인치)."""

from fixtures import ARCH_2QUARTER_IN, ARCH_4HALF_IN
from convert_length import convert_length


def test_cl_r5_001_fraction_half_inch_parses():
    # Given — Mom Test R2: 4½" 문턱
    # When
    result = convert_length(ARCH_4HALF_IN)
    # Then — 4.5 / R1_ARCH_INCH_DIVISOR(8) = 0.5625
    assert result.feet_decimal == 0.5625


def test_cl_r5_002_fraction_quarter_inch_parses():
    result = convert_length(ARCH_2QUARTER_IN)
    assert result.feet_decimal == 0.28125
