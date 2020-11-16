import pytest
from pos.domain.value_objects import Rfc

def test_rfc_equality():
    assert Rfc("XAXX010101000") == Rfc("XAXX010101000")

def test_rfc_inequality():
    assert Rfc("XAXX010101000") != Rfc("XAXX010101001")
