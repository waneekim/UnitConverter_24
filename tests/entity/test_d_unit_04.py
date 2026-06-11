"""D-UNIT-04 — CL-R7-003/004 (FR-UNIT-04 inch 파싱·inch 출력)."""

from convert_length import convert_length


def test_cl_r7_003_inch_colon_parses_to_feet():
    # Given — Mom Test R6: inch 단독 입력
    result = convert_length("inch:12")
    # Then — 12 inch = 1 foot
    assert result.feet_decimal == 1.0
    assert result.inch == 12.0


def test_cl_r7_004_cm_to_inch_mom_test():
    # Given — Mom Test R6: cm → inch (2.54 cm = 1 inch)
    result = convert_length("cm:2.54")
    # Then
    assert abs(result.inch - 1.0) < 1e-6
