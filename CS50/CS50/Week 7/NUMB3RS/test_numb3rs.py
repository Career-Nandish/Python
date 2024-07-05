from numb3rs import validate

def test_validate():
        assert validate("cat") == False
        assert validate("255.255.255.255") == True
        assert validate("0.0.0.0") == True
        assert validate("127.0.0.1") == True
        assert validate("127.999.0.1") == False
        assert validate("1.2.3.4.5") == False
        assert validate("1.11.111.255") == True
        assert validate("111.9.0.0") == True
        assert validate(".255.249.249") == False
        assert validate("255.") == False
        assert validate("255.1.") == False
        assert validate("255.1.1.") == False
        assert validate("255.1.1.1.") == False