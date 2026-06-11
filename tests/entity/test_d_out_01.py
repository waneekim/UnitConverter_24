"""D-OUT-01 — FR-OUT-01 견적용 반올림 (R3)."""

from constants import DEFAULT_ESTIMATE_DECIMAL_PLACES
from convert_length import convert_length


def test_cl_out_001_estimate_rounded_default_places():
    # Given — FR-OUT-01: 견적용 소수 자릿수 (config SSOT)
    # When
    result = convert_length("10'-6\"")
    # Then
    assert result.estimate_rounded == round(10.75, DEFAULT_ESTIMATE_DECIMAL_PLACES)
    assert DEFAULT_ESTIMATE_DECIMAL_PLACES == 2


def test_cl_out_002_estimate_disabled_when_none():
    result = convert_length("3'-6\"", estimate_places=None)
    assert result.estimate_rounded is None
