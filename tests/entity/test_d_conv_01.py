"""D-CONV-01 — convert_length 건축 표기 (FR-LOC 연계)."""

from fixtures import ARCH_3FT_6IN
from convert_length import convert_length


def test_cl_r1_001_arch_3ft_6in_feet_decimal():
    # Given — CL-R1-001: 3'-6" = 3.75 feet (Mom Test E1)
    # When
    result = convert_length(ARCH_3FT_6IN)
    # Then
    assert result.feet_decimal == 3.75
    assert result.feet == 3.75
