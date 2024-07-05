# Response Validation

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 7 - Response Validation Problem Set](https://cs50.harvard.edu/python/2022/psets/7/response/). The `response.py` program is designed to prompt the user for an email address and validate whether the input is a syntactically valid email address. This README will guide you through how to use the program, understand its structure, and effectively test its functionality.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `response.py` file.

   ```sh
   cd path/to/your/directory
   ```

3. Run the program using the `python` command:

   ```sh
   python response.py
   ```

4. The program will prompt you to enter an email address.
5. Input the email address and press Enter.
6. The program will output "Valid" if the input is a syntactically valid email address or "Invalid" if it is not.

## Program Explanation

The `response.py` program uses the `validators` library to validate the syntax of the input email address. Here's how it works:

1. The `validate_email()` function takes an email address as input.

2. The `validators.email()` function is used to check whether the input string is a valid email address. If it is valid, the function returns `True`; otherwise, it returns `False`.

3. Based on the result of the validation, the function returns either "Valid" or "Invalid" as the output.

## How to Test

1. Follow the steps mentioned in the "How to Run the Program" section to run the `response.py` program.
2. Input various email addresses to test if the program validates them correctly.

## Installing Dependencies

To use the `validators` library, you can install it using the following command:

```sh
pip install validators
```

## Additional Notes

- The `validators` library provides a convenient way to validate email addresses without having to manually write regular expressions.
- The program focuses solely on validating the syntax of the email address, not whether the domain name actually exists.
- Properly utilizing the `validators.email()` function ensures that the email address is checked for syntactic validity.
- Make sure to test the program with various valid and invalid email addresses to ensure its accuracy.