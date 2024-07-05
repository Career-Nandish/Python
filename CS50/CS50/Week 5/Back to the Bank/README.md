# Back to the Bank

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 5 - Back to the Bank Problem Set](https://cs50.harvard.edu/python/2022/psets/5/test_bank/). The `bank.py` program determines the value associated with a greeting message. If the greeting starts with "hello," the value is $0. If it starts with an "h" (but not "hello"), the value is $20. Otherwise, the value is $100. To ensure that the program functions correctly, a set of tests have been implemented in the `test_bank.py` file. These tests thoroughly test the `value` function, checking its behavior against various greetings.

## How to Run the Tests

1. Open your terminal.
2. Navigate to the directory where you have saved both `bank.py` and `test_bank.py`.

   ```
   cd path/to/your/directory
   ```

3. Run the tests using the `pytest` command:

   ```
   pytest test_bank.py
   ```

4. The tests will be executed, and the results will be displayed in the terminal.

## Program Code

### bank.py

```python
import re

def main():
    greet = input("Greeting: ")
    print(value(greet))

def value(greet):
    greet  = greet.lower().lstrip()
    if re.match(r'^hello.*$', greet): return 0
    elif greet[0] == 'h': return 20
    else: return 100

if __name__ == "__main__":
    main()
```

### test_bank.py

```python
from bank import value

def test0():
    assert value("hello") == 0
    assert value("HELLO") == 0

def test20():
    assert value("hyena") == 20
    assert value("HYENA") == 20

def test100():
    assert value("wassup bro") == 100
    assert value("WASSUP BRO") == 100
```

## How to Test

1. Run the tests as mentioned in the "How to Run the Tests" section.
2. The tests will be executed, and you will see the results in the terminal.

## Sample Test Cases

1. **Greeting Starts with "hello":**
   - **Input:**
     ```
     assert value("Hello") == "0"
     ```

2. **Greeting Starts with "hello," (with trailing spaces):**
   - **Input:**
     ```
     assert value("Hello, Newman ") == "0"
     ```

3. **Greeting Starts with "h" (without "hello"):**
   - **Input:**
     ```
     assert value("How you doing?") == "20"
     ```

4. **Greeting Starts with a Different Letter:**
   - **Input:**
     ```
     assert value("What's happening?") == "100"
     ```

## Additional Notes

- Ensure that the `bank.py` and `test_bank.py` files are saved in the same directory and have the correct names.
- The `value` function is responsible for determining the value associated with the given greeting message. The `test_value` function in `test_bank.py` tests the `value` function using various inputs and expected outputs.
- Running the tests using `pytest` will show whether your implementation of the `value` function is working correctly. It's important to have both the correct and incorrect versions of `bank.py` to validate your tests.