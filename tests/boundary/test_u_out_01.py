"""U-OUT-01 — UI-R5-001 (FR-OUT-02 견적 반올림 출력)."""

from fixtures import ARCH_3FT_6IN
from UnitConverter import process_input


def test_ui_r5_001_estimate_rounded_two_decimal_places():
    lines, error = process_input(ARCH_3FT_6IN)
    assert error is None
    assert len(lines) == 4
    joined = "\n".join(lines)
    assert "1.14" in joined
    assert "3.75" in joined
    assert "45.0" in joined
    assert "inch" in joined
    assert "1.1429999634240011" not in joined
    assert "1.2499961900001217" not in joined
