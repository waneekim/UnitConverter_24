import re

from constants import (
    FEET_COMPARE_EPSILON,
    FEET_PER_METER,
    KNOWN_UNITS,
    R1_ARCH_INCH_DIVISOR,
    YARD_PER_METER,
)

_ARCH_PATTERN = re.compile(r"^(\d+)'-(\d+)\"$")


def _is_arch(cell: str) -> bool:
    return _ARCH_PATTERN.match(cell) is not None


def _parse_arch_feet(cell: str) -> float | None:
    match = _ARCH_PATTERN.match(cell)
    if not match:
        return None
    feet = int(match.group(1))
    inches = int(match.group(2))
    return feet + inches / R1_ARCH_INCH_DIVISOR


def _parse_feet_value(cell: str) -> float | None:
    if ":" not in cell:
        return None
    unit, value_str = cell.split(":", 1)
    if unit != "feet":
        return None
    try:
        return float(value_str)
    except ValueError:
        return None


def _parse_unit_value(cell: str) -> tuple[str, float] | None:
    if ":" not in cell:
        return None
    unit, value_str = cell.split(":", 1)
    if unit not in KNOWN_UNITS:
        return None
    try:
        return unit, float(value_str)
    except ValueError:
        return None


def _row_fails_r4_format(row: list[str]) -> bool:
    for cell in row:
        if _is_arch(cell):
            continue
        if ":" not in cell:
            return True
        unit = cell.split(":", 1)[0]
        if unit not in KNOWN_UNITS:
            return True
    return False


def _row_fails_r1(row: list[str]) -> bool:
    arch_feet: list[float] = []
    feet_values: list[float] = []

    for cell in row:
        arch = _parse_arch_feet(cell)
        if arch is not None:
            arch_feet.append(arch)
            continue
        feet_val = _parse_feet_value(cell)
        if feet_val is not None:
            feet_values.append(feet_val)

    if arch_feet and feet_values:
        return abs(arch_feet[0] - feet_values[0]) >= FEET_COMPARE_EPSILON
    return False


def _row_fails_r2(row: list[str]) -> bool:
    units: dict[str, float] = {}
    for cell in row:
        if _is_arch(cell):
            continue
        parsed = _parse_unit_value(cell)
        if parsed is not None:
            units[parsed[0]] = parsed[1]

    if "feet" in units and "yard" in units:
        if abs(units["feet"] - units["yard"]) < FEET_COMPARE_EPSILON:
            return True

    if "meter" in units and "feet" in units and "yard" in units:
        meter = units["meter"]
        expected_feet = meter * FEET_PER_METER
        expected_yard = meter * YARD_PER_METER
        feet_ok = abs(units["feet"] - expected_feet) < FEET_COMPARE_EPSILON
        yard_ok = abs(units["yard"] - expected_yard) < FEET_COMPARE_EPSILON
        if not feet_ok or not yard_ok:
            return True

    return False


def _row_has_arch_only(row: list[str]) -> bool:
    return bool(row) and all(_is_arch(cell) for cell in row)


def _row_has_valid_meter_triple(row: list[str]) -> bool:
    units: dict[str, float] = {}
    for cell in row:
        parsed = _parse_unit_value(cell)
        if parsed is not None:
            units[parsed[0]] = parsed[1]
    if set(units.keys()) != {"meter", "feet", "yard"}:
        return False
    meter = units["meter"]
    return (
        abs(units["feet"] - meter * FEET_PER_METER) < FEET_COMPARE_EPSILON
        and abs(units["yard"] - meter * YARD_PER_METER) < FEET_COMPARE_EPSILON
    )


def _row_passes(row: list[str]) -> bool:
    if _row_fails_r4_format(row):
        return False
    if _row_fails_r1(row):
        return False
    if _row_fails_r2(row):
        return False

    if _row_has_arch_only(row):
        return True

    has_arch = any(_is_arch(cell) for cell in row)
    has_unit = any(":" in cell and not _is_arch(cell) for cell in row)

    if has_unit and not has_arch:
        if _row_has_valid_meter_triple(row):
            return True
        return False

    return True


def validate_lines(grid: list[list[str]]) -> dict:
    for row in grid:
        if any(cell == "" for cell in row):
            return {"status": "incomplete", "failed_lines": []}

    failed_lines = [idx for idx, row in enumerate(grid) if not _row_passes(row)]
    status = "fail" if failed_lines else "pass"
    return {"status": status, "failed_lines": failed_lines}
