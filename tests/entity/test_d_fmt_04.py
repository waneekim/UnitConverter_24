"""D-FMT-04 — CL-R6-001 (FR-FMT-04 콜론 뒤 공백 허용)."""

from convert_length import convert_length


def test_cl_r6_001_meter_colon_space_value_parses():
    # Given — Mom Test R3: meter: 2.5 (공백)
    result = convert_length("meter: 2.5")
    # Then
    assert result.meter == 2.5
    assert abs(result.feet_decimal - 2.5 * 3.28084) < 1e-6
