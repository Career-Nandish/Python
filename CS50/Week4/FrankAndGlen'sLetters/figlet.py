import sys
from pyfiglet import Figlet

def main():
    # input
    inp = input("Input: ")

    if len(sys.argv) == 1:
        f = Figlet()
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-f' or sys.argv[1] == '--font':
            f = Figlet(sys.argv[2])
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")

    # Output
    print("Output: \n" , f.renderText(inp))


if __name__ == "__main__":
    main()