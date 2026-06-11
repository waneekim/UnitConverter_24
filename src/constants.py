"""도메인 상수 SSOT — config/conversion.json + 기본값 fallback."""

import json
from pathlib import Path

_CONFIG_PATH = Path(__file__).resolve().parent.parent / "config" / "conversion.json"

_DEFAULTS = {
    "feet_per_meter": 3.28084,
    "yard_per_meter": 1.09361,
    "r1_arch_inch_divisor": 8,
    "feet_compare_epsilon": 1e-9,
    "estimate_decimal_places": 2,
    "known_units": ["meter", "feet", "yard", "cm", "mm", "inch"],
    "cm_per_meter": 100,
    "mm_per_meter": 1000,
    "inches_per_foot": 12,
}


def _load_config() -> dict:
    if not _CONFIG_PATH.is_file():
        return dict(_DEFAULTS)
    with _CONFIG_PATH.open(encoding="utf-8") as f:
        data = json.load(f)
    merged = dict(_DEFAULTS)
    merged.update(data)
    return merged


_CFG = _load_config()

FEET_PER_METER = float(_CFG["feet_per_meter"])
YARD_PER_METER = float(_CFG["yard_per_meter"])
R1_ARCH_INCH_DIVISOR = int(_CFG["r1_arch_inch_divisor"])
FEET_COMPARE_EPSILON = float(_CFG["feet_compare_epsilon"])
DEFAULT_ESTIMATE_DECIMAL_PLACES = int(_CFG["estimate_decimal_places"])
KNOWN_UNITS = frozenset(_CFG["known_units"])
CM_PER_METER = float(_CFG["cm_per_meter"])
MM_PER_METER = float(_CFG["mm_per_meter"])
INCHES_PER_FOOT = float(_CFG["inches_per_foot"])
