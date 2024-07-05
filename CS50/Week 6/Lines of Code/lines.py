import sys
from os import path


def file_lines(fname):
    count = 0
    with open(fname) as f:
        for line in f.readlines():
            if not (line.lstrip().startswith("#") or line.replace(" ", "") == "\n"):
                count += 1
    return count

def check_args(args):
    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(args) > 2:
        sys.exit("Too many command-line arguments")
    else:
        return True

def check_file_n_ext(fname):
    if '.' in fname:
        _, ext = fname.split('.')
        if ext != "py" or ext == '':
            sys.exit("Not a Python file")
        else:
            if not path.exists(fname):
                sys.exit("File does not exist")
            else:
                return True
    else:
        sys.exit("Not a Python file")


def main():
    if check_args(sys.argv):
        fname = sys.argv[1]
        if check_file_n_ext(fname):
            print(file_lines(fname))

if __name__ == "__main__":
    main()