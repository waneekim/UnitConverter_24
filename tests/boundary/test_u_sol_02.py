"""Golden Master — Mom Test R2 UI (U-OUT, U-BATCH, U-HINT)."""

from _approval import assert_matches_golden, format_ui_golden
from fixtures import ARCH_3FT_6IN, STEEL_DIMS_8
from UnitConverter import ERROR_INVALID_FORMAT, INPUT_PROMPT, process_batch_input, process_input

STEEL_SPECS_8 = [row[0] for row in STEEL_DIMS_8]


def test_u_out_01_ui_r5_001_golden():
    lines, error = process_input(ARCH_3FT_6IN)
    assert_matches_golden("UI-R5-001", format_ui_golden(lines, error))


def test_u_batch_01_ui_batch_001_golden():
    lines, error = process_batch_input(STEEL_SPECS_8)
    assert_matches_golden("UI-BATCH-001", format_ui_golden(lines, error))


def test_u_hint_01_ui_hint_001_golden():
    lines, error = process_input("meter2.5")
    assert_matches_golden("UI-HINT-001", format_ui_golden(lines, error))


def test_u_hint_02_ui_hint_002_golden():
    assert_matches_golden("UI-HINT-002", f"prompt={INPUT_PROMPT}\n")
