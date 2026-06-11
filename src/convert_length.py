"""PRD §5.2 — convert_length / convert_lengths Command API."""

from constants import DEFAULT_ESTIMATE_DECIMAL_PLACES, FEET_PER_METER, YARD_PER_METER
from conversion_result import ConversionResult
from length_spec import LengthSpecError, parse_spec_to_feet_decimal  # noqa: F401 — re-export


def convert_length(
    spec: str,
    estimate_places: int | None = DEFAULT_ESTIMATE_DECIMAL_PLACES,
) -> ConversionResult:
    feet_decimal = parse_spec_to_feet_decimal(spec)
    meter = feet_decimal / FEET_PER_METER
    yard = meter * YARD_PER_METER
    estimate = (
        round(feet_decimal, estimate_places) if estimate_places is not None else None
    )
    return ConversionResult(
        input_spec=spec,
        feet_decimal=feet_decimal,
        meter=meter,
        feet=feet_decimal,
        yard=yard,
        estimate_rounded=estimate,
    )


def convert_lengths(
    specs: list[str],
    estimate_places: int | None = DEFAULT_ESTIMATE_DECIMAL_PLACES,
) -> list[ConversionResult]:
    return [convert_length(s, estimate_places=estimate_places) for s in specs]


# Re-export for boundary error handling
__all__ = ["convert_length", "convert_lengths", "ConversionResult", "LengthSpecError"]
