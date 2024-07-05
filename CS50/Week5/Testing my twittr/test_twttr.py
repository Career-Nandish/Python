from twttr import shorten


def test_upper():
    assert shorten("HELLO") == "HLL"

def test_lower():
    assert shorten("hello") == "hll"

def test_empty():
    assert shorten(" ") == " "

def test_numeric():
    assert shorten("123") == "123"

def test_alpha_numeric():
    assert shorten("123abc") == "123bc"

def test_punctuation():
    assert shorten(",.;") == ",.;"