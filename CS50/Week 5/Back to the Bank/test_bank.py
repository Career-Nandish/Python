from bank import value

def test0():
    assert value("hello") == 0
    assert value("HELLO") == 0

def test20():
    assert value("hyena") == 20
    assert value("HYENA") == 20

def test100():
    assert value("wassup bro") == 100
    assert value("WASSUP BRO") == 100
