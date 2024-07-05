import re
from datetime import datetime

def convert_date(inp):

    pattern1 = r'^\d{1,2}/\d{1,2}/\d{4}$'
    pattern2 = r'^\w+ \d{1,2}, \d{4}$'

    if re.match(pattern1, inp):
        try:
            return datetime.strptime(inp, "%m/%d/%Y").strftime("%Y-%m-%d")
        except ValueError:
            return 0

    elif re.match(pattern2, inp):
        try:
            return datetime.strptime(inp, "%B %d, %Y").strftime("%Y-%m-%d")
        except ValueError:
            return 0

    return 0

def main():
    while True:
        inp = input("Date: ").strip()
        date = convert_date(inp)
        if date:
            print(date)
            break
        else:
            print("Invalid date format. Please try again.")

if __name__ == "__main__":
    main()