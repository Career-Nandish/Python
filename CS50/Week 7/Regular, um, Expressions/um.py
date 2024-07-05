import re
import sys

def count(s):
    return len(re.findall(r"\bum\b", s, re.I)) # thanks re HOWTO documentation

def main():
    print(count(input("Text: ").strip()))

if __name__ == "__main__":
    main()