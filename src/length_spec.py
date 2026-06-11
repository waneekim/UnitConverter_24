"""치수 문자열 파싱 — 건축 표기·단위:값 SSOT."""

import re

from constants import (
    CM_PER_METER,
    FEET_PER_METER,
    INCHES_PER_FOOT,
    KNOWN_UNITS,
    MM_PER_METER,
    R1_ARCH_INCH_DIVISOR,
    YARD_PER_METER,
)

_ARCH_PATTERN = re.compile(r"^(\d+)'-(\d+)\"$")
_FRACTION_INCH_PATTERN = re.compile(r"^(\d+)(½|¼)\"$")
_FRACTION_VALUE = {"½": 0.5, "¼": 0.25}


class LengthSpecError(ValueError):
    """FR-IN-01/02 · convert_length 파싱 오류."""


def is_arch_notation(spec: str) -> bool:
    return _ARCH_PATTERN.match(spec) is not None


def is_fraction_inch_notation(spec: str) -> bool:
    return _FRACTION_INCH_PATTERN.match(spec) is not None


def parse_fraction_inch_to_feet(spec: str) -> float:
    match = _FRACTION_INCH_PATTERN.match(spec)
    if not match:
        raise LengthSpecError(f"Invalid fraction inch notation: {spec}")
    whole = int(match.group(1))
    frac = _FRACTION_VALUE[match.group(2)]
    return (whole + frac) / R1_ARCH_INCH_DIVISOR


def parse_arch_to_feet(spec: str) -> float:
    match = _ARCH_PATTERN.match(spec)
    if not match:
        raise LengthSpecError(f"Invalid arch notation: {spec}")
    feet = int(match.group(1))
    inches = int(match.group(2))
    return feet + inches / R1_ARCH_INCH_DIVISOR


def parse_spec_to_feet_decimal(spec: str) -> float:
    """spec → canonical 소수 feet (Mom Test R1 SSOT)."""
    if is_arch_notation(spec):
        return parse_arch_to_feet(spec)
    if is_fraction_inch_notation(spec):
        return parse_fraction_inch_to_feet(spec)

    if ":" not in spec:
        raise LengthSpecError("Invalid format. Use unit:value (ex: meter:2.5)")

    unit, value_str = spec.split(":", 1)
    unit = unit.strip()
    value_str = value_str.strip()
    try:
        value = float(value_str)
    except ValueError:
        raise LengthSpecError(f"Invalid number: {value_str}")

    if unit not in KNOWN_UNITS:
        raise LengthSpecError(f"Unknown unit: {unit}")

    if unit == "meter":
        return value * FEET_PER_METER
    if unit == "feet":
        return value
    if unit == "yard":
        return value * FEET_PER_METER / YARD_PER_METER
    if unit == "cm":
        return (value / CM_PER_METER) * FEET_PER_METER
    if unit == "mm":
        return (value / MM_PER_METER) * FEET_PER_METER
    if unit == "inch":
        return value / INCHES_PER_FOOT
    raise LengthSpecError(f"Unknown unit: {unit}")
