import sys
import csv
from tabulate import tabulate
from os import path


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
        if ext != "csv" or ext == '':
            sys.exit("Not a csv file")
        else:
            if not path.exists(fname):
                sys.exit("File does not exist")
            else:
                return True
    else:
        sys.exit("Not a csv file")

def read_csv(fname):
    content = []
    with open(fname) as f:
        reader = csv.reader(f)
        for row in reader:
            content.append(row)
    return content

def prettify_csv(content):
    return tabulate(content[1:], headers = content[0], tablefmt="grid")

def main():
    if check_args(sys.argv):
        fname = sys.argv[1]
        if check_file_n_ext(fname):
            print(prettify_csv(read_csv(fname)))

if __name__ == "__main__":
    main()