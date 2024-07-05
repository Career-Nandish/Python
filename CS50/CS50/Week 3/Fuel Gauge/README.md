# Fuel Gauge

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 3 - Fuel Gauge Problem Set](https://cs50.harvard.edu/python/2022/psets/3/fuel/), named `fuel.py`, calculates the fuel level in a tank based on a given fraction. It prompts the user to input a fraction in the format X/Y, where X and Y are integers. The program then outputs the fuel level as a percentage, rounded to the nearest integer. If the fuel level is 1% or less, it outputs "E" to indicate that the tank is essentially empty. If the fuel level is 99% or more, it outputs "F" to indicate that the tank is essentially full.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `fuel.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python fuel.py
   ```

4. The program will prompt you to enter a fraction in the format X/Y. After you enter the fraction, it will output the fuel level as a percentage or "E" or "F" based on the calculation.

## Program Code

```python
# fuel.py

class FormatError(Exception):
    def __init__(self, message = None):
        self.message = message
        super().__init__(message)

def get_tank_read(prompt):
    while True:
        try:
            inp = input(prompt)
            if '/' in inp:
                x, y = [int(i) for i in inp.split("/")]
                if x > y and y !=0 :raise ValueError
                else:return round(x*100/y)
            else:
                raise FormatError
        except FormatError:
            print("Format of the input must be x/y")
        except ValueError:
            print("x and y must be integers where x<=y")
        except ZeroDivisionError:
            print("y can not be 0")

def read_indicator(ind):
    if ind <= 1:
        return "E"
    elif  1 < ind < 99:
        return str(ind) + "%"
    else:
        return "F"

def main():
    indicator = get_tank_read("Enter the value of x and y(format: x/y):")
    print(read_indicator(indicator))

if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Follow the prompts to enter various fractions. Make sure to test cases where the fraction is within the range of 1-99, as well as cases where the fraction results in an "E" or "F" output.
3. The program will output the fuel level as a percentage or "E" or "F" based on the input fraction. If the input is not valid (not in the format X/Y, X or Y not an integer, Y is 0, X is greater than Y), the program will display an "Invalid fraction" message.

## Sample Test Cases

1. **Input:** 3/4
   **Result:** 75%

2. **Input:** 1/4
   **Result:** 25%

3. **Input:** 4/4
   **Result:** F

4. **Input:** 0/4
   **Result:** E

## Additional Notes

Make sure to save the `fuel.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, ensure you are in the correct directory and have saved the file with the correct name.