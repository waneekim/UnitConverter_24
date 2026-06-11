"""D-CONV-02 — convert_length 단위:값."""

from constants import FEET_PER_METER, YARD_PER_METER
from convert_length import convert_length


def test_cl_unit_001_meter_2_5_converts():
    # Given — meter:2.5
    # When
    result = convert_length("meter:2.5")
    # Then
    assert result.feet_decimal == 2.5 * FEET_PER_METER
    assert result.meter == 2.5
    assert result.yard == 2.5 * YARD_PER_METER
