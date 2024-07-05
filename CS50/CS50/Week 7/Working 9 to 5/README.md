# Working 9 to 5

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 7 - Working 9 to 5 Problem Set](https://cs50.harvard.edu/python/2022/psets/7/working/). The `working.py` program is designed to convert 12-hour time formats to their corresponding 24-hour format. It handles various input time formats and raises a `ValueError` if the input is not in the expected format or if the provided time is invalid. This README will guide you through how to use the program, understand its structure, and how to test it effectively.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `working.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the `python` command:

   ```
   python working.py
   ```

4. The program will prompt you to enter a time in one of the specified formats.
5. Input the time and format as indicated in the instructions and press Enter.
6. The program will output the converted time in 24-hour format.

## Program Explanation

The `working.py` program uses regular expressions to match and extract the provided time format. It follows these steps:

1. The `convert()` function takes the input time as a string and applies a regular expression pattern to extract the time components.
   
2. The extracted time components (hours, minutes, and meridiem) are then validated for correctness. If any component is invalid, a `ValueError` is raised.

3. The program handles AM and PM conversion to 24-hour format correctly, considering cases where hours are equal to 12.

4. The function then formats the hours and minutes into the 24-hour format and returns the converted time.

## How to Test

1. Follow the steps mentioned in the "How to Run the Program" section to run the `working.py` program.
2. Input various valid and invalid time formats to test if the program converts them accurately and raises the appropriate exceptions.

## Writing Test Cases

The provided test cases are implemented in a separate file named `test_working.py`. The pytest framework is used to run these test cases.

### Running Tests

1. Ensure you have the `pytest` framework installed. If not, you can install it using:

   ```sh
   pip install pytest
   ```

2. Run the test cases by executing the following command in your terminal:

   ```sh
   pytest test_working.py
   ```

3. The test cases will be executed, and the output will indicate whether each test passed or failed.

## Additional Notes

- Regular expressions can be complex to write and debug. Make sure you understand the regular expression pattern used in the `convert()` function.
- Handling various edge cases, such as invalid times and time ranges, is crucial to ensure your program works correctly.
- The provided test cases in the `test_working.py` file cover various scenarios. Make sure to thoroughly understand them and expand the test cases if needed.