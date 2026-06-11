"""U-BATCH-01 — UI-BATCH-001 (FR-BATCH-02 다중 입력)."""

from fixtures import STEEL_DIMS_8
from UnitConverter import process_batch_input

STEEL_SPECS_8 = [row[0] for row in STEEL_DIMS_8]


def test_ui_batch_001_eight_specs_single_call():
    lines, error = process_batch_input(STEEL_SPECS_8)
    assert error is None
    assert len(lines) == 24
