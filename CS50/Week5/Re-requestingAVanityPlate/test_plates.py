from plates import is_valid

def test_numbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False

def test_first_two():
    assert is_valid("AB") == True
    assert is_valid("12") == False
    assert is_valid("A1") == False
    assert is_valid("1") == False

def test_punctuation():
    assert is_valid("AB11.") == False

def test_len():
    assert is_valid("COOK12") == True
    assert is_valid("CO") == True
    assert is_valid("COOOOOK11") == False