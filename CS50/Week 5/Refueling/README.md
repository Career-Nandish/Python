# Refueling

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 5 - Refueling Problem Set](https://cs50.harvard.edu/python/2022/psets/5/test_fuel/). The `fuel.py` program calculates the fuel gauge reading based on a given fraction input and provides the corresponding gauge reading using the `convert` and `gauge` functions. The `convert` function calculates the percentage representation of the given fraction, and the `gauge` function provides the corresponding gauge reading.

## How to Run the Tests

1. Open your terminal.
2. Navigate to the directory where you have saved both `fuel.py` and `test_fuel.py`.

   ```
   cd path/to/your/directory
   ```

3. Run the tests using the `pytest` command:

   ```
   pytest test_fuel.py
   ```

4. The tests will be executed, and the results will be displayed in the terminal.

## Program Code

### fuel.py

```python
class FormatError(Exception):
    def __init__(self, message = None):
        self.message = message
        super().__init__(message)

def convert(prompt):
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

def gauge(ind):
    if ind <= 1:
        return "E"
    elif  1 < ind < 99:
        return str(ind) + "%"
    else:
        return "F"

def main():
    indicator = convert("Enter the value of x and y(format: x/y):")
    print(gauge(indicator))

if __name__ == "__main__":
    main()
```

### test_fuel.py

```python
import pytest
from fuel import convert, gauge


def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):convert("6/1")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(36) == "36%"
    assert gauge(99) == "F"

def test_convert():
    assert convert("1/100") == 1
    assert convert("1/2") == 50
    assert convert("99/100") == 99
```

## How to Test

1. Run the tests as mentioned in the "How to Run the Tests" section.
2. The tests will be executed, and you will see the results in the terminal.

## Sample Test Cases

1. **Conversion Test ("1/4"):**
   - **Input:**
     ```
     assert convert("1/4") == 25
     ```

2. **Gauge Reading Test (25%):**
   - **Input:**
     ```
     assert gauge(25) == "25%"
     ```
     ```
     assert gauge(100) == "F"
     ```
     ```
     assert gauge(0) == "E"
     ```

3. **Zero Division Error Test:**
   - **Input:**
     ```
     with pytest.raises(ZeroDivisionError):
         convert('100/0')
     ```

4. **Value Error Test (Non-Digit Input):**
   - **Input:**
     ```
     with pytest.raises(ValueError):
         convert('a/b')
     ```

5. **Value Error Test (X > Y):**
   - **Input:**
     ```
     with pytest.raises(ValueError):
         convert('5/2')
     ```

## Additional Notes

- Ensure that the `fuel.py` and `test_fuel.py` files are saved in the same directory and have the correct names.
- The tests in `test_fuel.py` cover various scenarios to validate the correctness of the `convert` and `gauge` functions. Running the tests using `pytest` will indicate whether your implementation of these functions is working correctly.