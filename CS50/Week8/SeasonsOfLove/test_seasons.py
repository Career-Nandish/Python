
from datetime import date
from seasons import sing_date, valid_date

def test_sing_date():
    assert sing_date(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"
    assert sing_date(365) == "Five hundred twenty-five thousand, six hundred minutes"


def test_valid_date():
    assert valid_date("2022-06-11") == date.fromisoformat("2022-06-11")
    with pytest.raises(SystemExit):
        valid_date("January 1, 1999")
    with pytest.raises(SystemExit):
        valid_date("")