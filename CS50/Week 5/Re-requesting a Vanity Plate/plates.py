import re

def main():
    plate = input("Plate: ")
    print(is_valid(plate))

def is_valid(s):
    return re.match(r'^[A-Z]{2,6}[1-9]?[0-9]?$', s)

if __name__ == "__main__":
    main()