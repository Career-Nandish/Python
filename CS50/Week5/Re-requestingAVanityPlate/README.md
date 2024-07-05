# Re-requesting a Vanity Plate

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 5 - Re-requesting a Vanity Plate Problem Set](https://cs50.harvard.edu/python/2022/psets/5/test_plates/). The `plates.py` program checks whether a given license plate meets certain requirements to be considered valid. The program checks if the license plate starts with at least two letters, has a valid length between 2 and 6 characters, does not contain numbers in the middle, and does not have any punctuation marks. To ensure the program's correctness, a set of tests have been implemented in the `test_plates.py` file. These tests thoroughly test the `is_valid` function, checking its behavior against various license plates.

## How to Run the Tests

1. Open your terminal.
2. Navigate to the directory where you have saved both `plates.py` and `test_plates.py`.

   ```
   cd path/to/your/directory
   ```

3. Run the tests using the `pytest` command:

   ```
   pytest test_plates.py
   ```

4. The tests will be executed, and the results will be displayed in the terminal.

## Program Code

### plates.py

```python
import re

def main():
    plate = input("Plate: ")
    print(is_valid(plate))

def is_valid(s):
    return re.match(r'^[A-Z]{2,6}[1-9]?[0-9]?$', s)

if __name__ == "__main__":
    main()
```

### test_plates.py

```python
from plates import is_valid

def test_numbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False

def test_first_two():
    assert is_valid("AB") == True
    assert is_valid("12") == False
    assert is_valid("A1") == False
    assert is_valid("1") == False

def test_punctuation():
    assert is_valid("AB11.") == False

def test_len():
    assert is_valid("COOK12") == True
    assert is_valid("CO") == True
    assert is_valid("COOOOOK11") == False
```

## How to Test

1. Run the tests as mentioned in the "How to Run the Tests" section.
2. The tests will be executed, and you will see the results in the terminal.

## Sample Test Cases

1. **Valid License Plate ("CS50"):**
   - **Input:**
     ```
     assert is_valid("CS50") == True
     ```

2. **Valid License Plate ("NRVOUS"):**
   - **Input:**
     ```
     assert is_valid("NRVOUS") == True
     ```

3. **Invalid License Plate (Contains Number in Middle):**
   - **Input:**
     ```
     assert is_valid("CS05") == False
     ```

4. **Invalid License Plate (Too Long):**
   - **Input:**
     ```
     assert is_valid("CS50P") == False
     ```

5. **Invalid License Plate (Contains Punctuation):**
   - **Input:**
     ```
     assert is_valid("PI3.14") == False
     ```

6. **Invalid License Plate (Too Short):**
   - **Input:**
     ```
     assert is_valid("H") == False
     ```

7. **Invalid License Plate (Ends with "0"):**
   - **Input:**
     ```
     assert is_valid("OUTATIME") == False
     ```

## Additional Notes

- Ensure that the `plates.py` and `test_plates.py` files are saved in the same directory and have the correct names.
- The `is_valid` function is responsible for determining the validity of the given license plate. The `test_is_valid` function in `test_plates.py` tests the `is_valid` function using various inputs and expected outputs.
- Running the tests using `pytest` will show whether your implementation of the `is_valid` function is working correctly. It's important to have both the correct and incorrect versions of `plates.py` to validate your tests.