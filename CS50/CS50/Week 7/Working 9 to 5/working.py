import re
import sys

def main():
    print(convert(input("Hours: ").strip()))

def handle_time(h, m, x):
    # Handle Minute
    m = int(m) if m != None else 0

    # Handle hr
    if h == "12":
        if x == "p":
            h = 12
        else:
            h = 0
    else:
        h = int(h) if x == 'a' else int(h) + 12
    return f"{h:02}:{m:02}"

def convert(s):
     if matches:= re.match(r"""^([1-9]|1[0-2])(?::([0-5][0-9]))? ([AP])M to 
                      ([1-9]|1[0-2])(?::([0-5][0-9]))? ([AP])M$""", s, re.I):
         h1, m1, x1, h2, m2, x2 = matches.groups()
         f = handle_time(h1, m1, x1.lower())
         t = handle_time(h2, m2, x2.lower())
         return f"{f} to {t}"
     raise ValueError

if __name__ == "__main__":
    main()
