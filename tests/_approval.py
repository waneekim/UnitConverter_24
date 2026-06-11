"""Golden Master approval helpers — 수동 편집 우회 금지."""

import os
from pathlib import Path

from conversion_result import ConversionResult

GOLDEN_DIR = Path(__file__).parent / "golden"


def format_golden(result: dict) -> str:
    """Approval 출력 포맷 — 고정."""
    status = result["status"]
    lines = result.get("failed_lines", [])
    slots = [0] * 6
    for i, idx in enumerate(lines[:6]):
        slots[i] = idx + 1  # 0-based → 1-index
    line_str = ",".join(str(s) for s in slots)
    return f"status={status}\nfailed_lines=[{line_str}]\nerror_code=none\n"


def format_conversion_golden(result: ConversionResult) -> str:
    est = (
        result.estimate_rounded if result.estimate_rounded is not None else "none"
    )
    return (
        f"feet_decimal={result.feet_decimal}\n"
        f"meter={result.meter}\n"
        f"feet={result.feet}\n"
        f"yard={result.yard}\n"
        f"inch={result.inch}\n"
        f"estimate_rounded={est}\n"
    )


def format_ui_golden(lines: list[str], error: str | None) -> str:
    """UI boundary Approval 출력 — stdout 한 덩어리."""
    if error:
        return f"stdout={error}\n"
    return f"stdout={chr(10).join(lines)}\n"


def assert_matches_golden(test_id: str, actual: str) -> None:
    golden_path = GOLDEN_DIR / f"{test_id}.approved.txt"
    update = os.environ.get("UPDATE_GOLDEN") == "1"

    if update or not golden_path.exists():
        golden_path.parent.mkdir(parents=True, exist_ok=True)
        golden_path.write_text(actual, encoding="utf-8")
        return

    expected = golden_path.read_text(encoding="utf-8")
    if actual != expected:
        raise AssertionError(
            f"Golden mismatch: {test_id}\n"
            f"--- expected ({golden_path})\n{expected}"
            f"--- actual\n{actual}"
        )
