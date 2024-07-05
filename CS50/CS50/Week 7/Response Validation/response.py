from validators import email

def main():
    print(isValid(input("What is your email address? ").strip()))

def isValid(s):
    return "Valid" if email(s) else "Invalid"

if __name__ == "__main__":
    main()