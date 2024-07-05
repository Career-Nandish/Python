import pytest
from fuel import convert, gauge


def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):convert("6/1")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(36) == "36%"
    assert gauge(99) == "F"

def test_convert():
    assert convert("1/100") == 1
    assert convert("1/2") == 50
    assert convert("99/100") == 99