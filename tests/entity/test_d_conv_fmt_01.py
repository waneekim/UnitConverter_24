"""D-CONV-FMT — convert_length 오입력."""

import pytest
from length_spec import LengthSpecError
from convert_length import convert_length


def test_cl_fmt_001_missing_colon_raises():
    with pytest.raises(LengthSpecError, match="Invalid format"):
        convert_length("meter2.5")


def test_cl_fmt_002_unknown_unit_raises():
    with pytest.raises(LengthSpecError, match="Unknown unit"):
        convert_length("foo:1.0")
