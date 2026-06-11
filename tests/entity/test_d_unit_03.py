"""D-UNIT-03 — CL-R7-001/002 (FR-UNIT-03 cm/mm 파싱·변환)."""

from convert_length import convert_length


def test_cl_r7_001_cm_to_meter_and_feet():
    # Given — Mom Test R6: cm/mm → inch 실패, cm 입력
    result = convert_length("cm:100")
    # Then — 100 cm = 1 m
    assert result.meter == 1.0
    assert abs(result.feet_decimal - 3.28084) < 1e-6


def test_cl_r7_002_mm_to_meter():
    # Given — Mom Test R6: mm 입력
    result = convert_length("mm:2500")
    # Then — 2500 mm = 2.5 m
    assert result.meter == 2.5
    assert abs(result.feet_decimal - 2.5 * 3.28084) < 1e-6
