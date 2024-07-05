import sys
import inflect

def main():
    names = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            break

    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        print("Adieu, adieu, to " + ', '.join(names[:-1]) + ', and ' + names[-1])

if __name__ == "__main__":
    main()