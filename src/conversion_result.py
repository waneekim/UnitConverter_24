"""convert_length / convert_lengths 반환 타입."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ConversionResult:
    input_spec: str
    feet_decimal: float
    meter: float
    feet: float
    yard: float
    inch: float
    estimate_rounded: float | None = None
