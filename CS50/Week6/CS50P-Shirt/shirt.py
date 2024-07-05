import sys
from PIL import Image, ImageOps
from os import path


def check_args(args):
    if len(args) < 3:
        sys.exit("Too few command-line arguments")
    elif len(args) > 3:
        sys.exit("Too many command-line arguments")
    else:
        return True

def check_file_n_ext(fname, p):
    exts = ["jpg", "jpeg", "png"]
    if '.' in fname:
        _, ext = fname.split('.')
        if (not ext.lower() in exts) or ext == '':
            sys.exit("Invalid " + p)
        else:
            if p == "Input":
                if not path.exists(fname):
                    sys.exit(p + " does not exist")

            return ext
    else:
        sys.exit("Invalid " + p)

def image_maker(iname, oname):
    shirt = Image.open("shirt.png")
    with Image.open(iname) as before:
        before_crop = ImageOps.fit(before, shirt.size)
        before_crop.paste(shirt, mask = shirt)
        before_crop.save(oname)

def main():
    if check_args(sys.argv):
        iname, oname = sys.argv[1:]
        if check_file_n_ext(iname, "Input") != check_file_n_ext(oname, "Output"):
            sys.exit("Input and output have different extensions")
        image_maker(iname, oname)

if __name__ == "__main__":
    main()
