# Regular, um, Expressions

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 7 - Regular, um, Expressions Problem Set](https://cs50.harvard.edu/python/2022/psets/7/um/). The `um.py` is a program designed to count the number of occurrences of the word "um" in a given text. This README will guide you through how to use the program, understand its structure, and effectively test its functionality.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `um.py` file.

   ```sh
   cd path/to/your/directory
   ```

3. Run the program using the `python` command:

   ```sh
   python um.py
   ```

4. The program will prompt you to enter a line of text.
5. Input the text and press Enter.
6. The program will output the number of times the word "um" appears in the text as a separate word.

## Program Explanation

The `um.py` program utilizes regular expressions to find all occurrences of the word "um" as a separate word in the provided text. Here's how it works:

1. The `count()` function takes the input text as a string and applies a regular expression pattern to find all instances of the word "um" as a separate word.

2. The `re.findall()` function is used with the pattern `\bum\b` to match occurrences of "um" as a word, ignoring case.

3. The function returns the number of occurrences of the word "um" as a separate word.

## How to Test

1. Follow the steps mentioned in the "How to Run the Program" section to run the `um.py` program.
2. Input various lines of text to test if the program counts the occurrences of "um" as a separate word accurately.

## Writing Test Cases

The provided test cases are implemented in a separate file named `test_um.py`. The [`pytest`](https://docs.pytest.org/en/6.2.x/) framework is used to run these test cases.

### Running Tests

1. Ensure you have the `pytest` framework installed. If not, you can install it using:

   ```sh
   pip install pytest
   ```

2. Run the test cases by executing the following command in your terminal:

   ```sh
   pytest test_um.py
   ```

3. The test cases will be executed, and the output will indicate whether each test passed or failed.

### Test Coverage

The provided test cases cover various scenarios, including single occurrences, multiple occurrences, and edge cases where "um" is a substring of a word. Thoroughly review and understand these test cases, and consider expanding them if necessary.

## Additional Notes

- Regular expressions can be powerful tools for pattern matching. Make sure you understand the regular expression pattern used in the `count()` function.
- Be aware of edge cases, such as "um" being part of another word or occurring in uppercase or mixed case.
- Properly utilizing the `re.IGNORECASE` flag ensures that "um" is matched regardless of its case.
- The provided test cases in the `test_um.py` file cover various scenarios. Make sure to thoroughly understand them and expand the test cases if needed.