"""공유 pytest 픽스처."""

import pytest

from fixtures import ARCH_3FT_6IN


@pytest.fixture
def arch_3ft_6in():
    """FR-LOC-01/02 — Mom Test E1."""
    return ARCH_3FT_6IN
