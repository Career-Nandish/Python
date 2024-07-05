# NUMB3RS

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 7 - NUMB3RS Problem Set](https://cs50.harvard.edu/python/2022/psets/7/numb3rs/). The `numb3rs.py` program provides a way to validate IPv4 addresses. Here's how to use the program and understand its implementation.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `numb3rs.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the `python` command:

   ```
   python numb3rs.py
   ```

4. The program will prompt you to enter an IPv4 address. Enter the address and press Enter.
5. The program will output whether the entered IPv4 address is valid or not.

## Program Explanation

The `numb3rs.py` program uses the `re` module to validate the input IPv4 address. It follows these steps:

1. The `matches()` function uses the `re.search()` function to search for a pattern that matches an IPv4 address. It returns the matched pattern if found, otherwise, it returns `None`.

2. The `validate()` function first calls the `matches()` function to get the matched pattern of the input IPv4 address.

3. If the matched pattern is not `None`, the function splits the pattern into four parts using the dot separator and attempts to convert each part to an integer.

4. The function checks if each part of the IPv4 address is within the valid range of 0 to 255. If all parts are valid, the function returns `True`, indicating a valid IPv4 address.

5. If the input IPv4 address does not match the pattern or any of its parts are not within the valid range, the function returns `False`.

## How to Test

1. Follow the steps mentioned in the "How to Run the Program" section to run the `numb3rs.py` program.
2. Enter different IPv4 addresses, both valid and invalid, to see how the program validates them.

## Writing Test Cases

The `test_numb3rs.py` file contains test cases to ensure the correctness of the `numb3rs.py` program. The `pytest` framework is used to run these test cases. The test cases include scenarios for valid and invalid IPv4 addresses, as well as some edge cases.

To run the test cases, execute the following command in your terminal:

```
pytest test_numb3rs.py
```

This will execute the test cases defined in the `test_numb3rs.py` file and display the results.

## Additional Notes

- The program provides a basic validation for IPv4 addresses based on their format and the range of each part.
- The `re` module is used to perform regular expression matching, which helps to identify patterns in the input string.
- The `pytest` framework simplifies the process of writing and running test cases to ensure the functionality of the program. It's important to write comprehensive test cases to cover various scenarios.
  ```
  pip install pytest
  ```
- The `AttributeError` handling is used in the `matches()` function to handle cases where `re.search()` returns `None`.
- The program only validates IPv4 addresses, not IPv6 addresses.