# I hate writing test cases

from um import count

def test_input():
    assert count("Um, thanks, yum...") == 1
    assert count("Um,") == 1
    assert count("um, um, um, yummy") == 3
    assert count("") == 0