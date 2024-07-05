import re, sys
import inflect
from datetime import date

def main():
    d = input("Date of Birth: ").strip()
    if dob:=valid_date(d):
        print(sing_date(get_minutes(dob)))

def valid_date(d):
    try:
        return date.fromisoformat(d)
    except ValueError:
        sys.exit("Invalid date")

def sing_date(minutes):
    m_str = inflect.engine().number_to_words(minutes, andword="") + " minutes"
    return m_str.capitalize()

def get_minutes(dob):
    return (date.today() - dob).days * 24 * 60

if __name__ == "__main__":
    main()