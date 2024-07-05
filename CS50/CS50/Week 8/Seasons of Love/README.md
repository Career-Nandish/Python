# Seasons of Love

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 8 - Seasons of Love Problem Set](https://cs50.harvard.edu/python/2022/psets/8/seasons/). The `saesons.py` program allows users to input their date of birth and calculates their age in minutes, rounded to the nearest integer, using English words to express the duration. This README will guide you through how to use the program, understand its structure, and effectively test its functionality.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `seasons.py` file.

   ```sh
   cd path/to/your/directory
   ```

3. Run the program using the `python` command:

   ```sh
   python seasons.py
   ```

4. The program will prompt you to enter your date of birth in YYYY-MM-DD format.
5. Input your date of birth and press Enter.
6. The program will output your age in minutes, using English words.

## Program Explanation

The `seasons.py` program uses the `datetime` library to calculate the age of the user in minutes. Here's how it works:

1. The `convert_to_words()` function takes the user's date of birth as input.
2. The `get_dob()` function extracts and validates the date of birth entered by the user.
3. The `datetime` library is used to calculate the difference between the current date and the user's date of birth.
4. The difference is converted into minutes and rounded to the nearest integer.
5. The `inflect` library is used to convert the minutes into English words.
6. The final result is returned in the format of "X minutes", where X is the age in English words.

## How to Test

1. Follow the steps mentioned in the "How to Run the Program" section to run the `seasons.py` program.
2. Input your date of birth to calculate your age in minutes using English words.

## Testing with `test_seasons.py`

To ensure the accuracy and reliability of the `seasons.py` program, the provided `test_seasons.py` file includes several test cases. Here's how to run these tests:

1. Open your terminal.
2. Navigate to the directory where you have saved the `test_seasons.py` file.

   ```sh
   cd path/to/your/directory
   ```

3. Run the tests using the `pytest` command:

   ```sh
   pytest test_seasons.py
   ```

4. The tests will run, and you will see the results indicating whether the program passes each test case.

## Installing Dependencies

To use the `inflect` library, you can install it using the following command:

```sh
pip install inflect
```

## Additional Notes

- The program assumes that the user was born at midnight on their date of birth.
- The program provides a creative way to express age in minutes using English words.
- The `datetime` library's `date` class and the `inflect` library are used effectively to achieve the desired functionality.
- Make sure to test the program with different birthdates to ensure its accuracy and reliability.