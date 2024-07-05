from jar import Jar
from pytest import raises

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.deposit(1)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(2)
    assert jar.size == 2
    with raises(ValueError):
        jar.deposit(4)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    with raises(ValueError):
        jar.withdraw(3)