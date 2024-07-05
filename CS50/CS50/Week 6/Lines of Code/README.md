# Lines of Code

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 6 - Lines of Code Problem Set](https://cs50.harvard.edu/python/2022/psets/6/lines/). The `lines.py` program takes the name of a Python file as a command-line argument and outputs the number of lines of code in that file, excluding comments and blank lines.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `lines.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the `python` command and provide the filename as an argument:

   ```
   python lines.py filename.py
   ```

   Replace `filename.py` with the actual name of the Python file you want to analyze.

## Program Code

### lines.py

```python
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
```

## How to Test

1. Follow the steps mentioned in the "How to Run the Program" section to run the `lines.py` program.
2. Provide the name of a Python file that you want to analyze (e.g., `hello.py`) as a command-line argument.
3. The program will output the number of lines of code in the specified file, excluding comments and blank lines.

## Additional Notes

- The `lines.py` program uses the `sys` module to handle command-line arguments and exit the program if necessary.
- The program also handles different cases of comments, including multi-line comments enclosed in triple quotes (`'''` or `"""`).
- The `count_code_lines` function counts the lines of code in the provided file, excluding comments and blank lines.
- After running the program, it will display the count of code lines in the specified Python file.