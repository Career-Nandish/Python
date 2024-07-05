import sys
import csv
from os import path


def check_args(args):
    if len(args) < 3:
        sys.exit("Too few command-line arguments")
    elif len(args) > 3:
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
                sys.exit(f"Could not read {fname}")
            else:
                return True
    else:
        sys.exit("Not a csv file")

def read_csv(fname):
    content = []
    with open(fname) as f:
        reader = csv.DictReader(f)
        for row in reader:
            content.append(row)
    return content

def write_csv(content, oname):
    with open(oname, "w") as f:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for line in content:
            d = {}
            d["house"] = line["house"]
            d["last"], d["first"] = line["name"].split(", ")
            writer.writerow(d)

def main():
    if check_args(sys.argv):
        iname, oname = sys.argv[1:]
        if check_file_n_ext(iname):
            write_csv(read_csv(iname), oname)

if __name__ == "__main__":
    main()