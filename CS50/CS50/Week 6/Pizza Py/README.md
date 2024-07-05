# Pizza Py

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 6 - Pizza Py Problem Set](https://cs50.harvard.edu/python/2022/psets/6/pizza/). The `pizza.py` program reads a CSV file containing pizza menu items and prices and displays the menu in the form of an ASCII art table using the `tabulate` package.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `pizza.py` file.

   ```
   cd path/to/your/directory
   ```

3. Install the `tabulate` package if you haven't already:

   ```
   pip install tabulate
   ```

4. Run the program using the `python` command and provide the filename of the CSV file as an argument:

   ```
   python pizza.py filename.csv
   ```

   Replace `filename.csv` with the actual name of the CSV file you want to display as a menu.

## Program Code

### pizza.py

```python
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
```

## How to Test

1. Follow the steps mentioned in the "How to Run the Program" section to run the `pizza.py` program.
2. Provide the name of a CSV file containing the pizza menu (e.g., [sicilian.csv](https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv) or [regular.csv](https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv)) as a command-line argument.
3. The program will display the menu in the form of an ASCII art table.
   ```
   +-----------------+---------+---------+
   | Regular Pizza   | Small   | Large   |
   +=================+=========+=========+
   | Cheese          | $13.50  | $18.95  |
   +-----------------+---------+---------+
   | 1 topping       | $14.75  | $20.95  |
   +-----------------+---------+---------+
   | 2 toppings      | $15.95  | $22.95  |
   +-----------------+---------+---------+
   | 3 toppings      | $16.95  | $24.95  |
   +-----------------+---------+---------+
   | Special         | $18.50  | $26.95  |
   +-----------------+---------+---------+
   ```

## Additional Notes

- The `pizza.py` program reads the CSV file specified in the command-line argument using the `csv` module.
- It uses the `tabulate` package to format the menu items and prices into an ASCII art table.
- The program performs error handling to handle cases where the user provides incorrect command-line arguments or the specified file does not exist.
- After running the program, it will display the menu in the form of an ASCII art table.