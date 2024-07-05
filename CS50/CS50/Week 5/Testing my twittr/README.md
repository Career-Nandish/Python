# Testing my twttr

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 5 - Testing my twttr Problem Set](https://cs50.harvard.edu/python/2022/psets/5/test_twttr/). The `twttr.py` program is designed to remove all vowels (both uppercase and lowercase) from a given string. To ensure that the program functions correctly, a set of tests have been implemented in the `test_twttr.py` file. These tests thoroughly test the `shorten` function, checking its behavior against various inputs.

## How to Run the Tests

1. Open your terminal.
2. Navigate to the directory where you have saved both `twttr.py` and `test_twttr.py`.

   ```
   cd path/to/your/directory
   ```

3. Run the tests using the `pytest` command:

   ```
   pytest test_twttr.py
   ```

4. The tests will be executed, and the results will be displayed in the terminal.

## Program Code

### twttr.py

```python
def main():
    in_str = input("Input: ")
    print("Output:", shorten(in_str))

def shorten(s):
    if s.isdigit():
        return s
    else:
        out_str = ''
        for i in s:
            if (i not in 'aeiou') or i.isdigit():
                out_str += i
        return out_str

if __name__ == "__main__":
    main()
```

### test_twttr.py

```python
from twttr import shorten


def test_upper():
    assert shorten("HELLO") == "HLL"

def test_lower():
    assert shorten("hello") == "hll"

def test_empty():
    assert shorten(" ") == " "

def test_numeric():
    assert shorten("123") == "123"

def test_alpha_numeric():
    assert shorten("123abc") == "123bc"

def test_punctuation():
    assert shorten(",.;") == ",.;"
```

## How to Test

1. Run the tests as mentioned in the "How to Run the Tests" section.
2. The tests will be executed, and you will see the results in the terminal.

## Sample Test Cases

1. **Shorten Word with Vowels:**
   - **Input:**
     ```
     assert shorten("cat") == "ct"
     ```

2. **Shorten Word with Repeated Vowels:**
   - **Input:**
     ```
     assert shorten("twitter") == "twttr"
     ```

3. **Shorten Uppercase Word:**
   - **Input:**
     ```
     assert shorten("APPLE") == "PPL"
     ```

4. **Shorten Word with Numbers:**
   - **Input:**
     ```
     assert shorten("Twitt3r") == "Twtt3r"
     ```

5. **Shorten Word with Special Characters:**
   - **Input:**
     ```
     assert shorten("pr,@oud!") == "pr,@d!"
     ```

## Additional Notes

- Ensure that the `twttr.py` and `test_twttr.py` files are saved in the same directory and have the correct names.
- The `shorten_text` function is responsible for removing vowels from the given input string and returning the modified string. The `test_shorten` function in `test_twttr.py` tests the `shorten` function using various inputs and expected outputs.
- Running the tests using `pytest` will show whether your implementation of the `shorten` function is working correctly. It's important to have both the correct and incorrect versions of `twttr.py` to validate your tests.