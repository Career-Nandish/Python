# Indoor Voice

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 0 - Indoor Voice Problem Set](https://cs50.harvard.edu/python/2022/psets/0/indoor/), named `indoor.py`, prompts the user for input and then outputs the same input in lowercase, while preserving punctuation and whitespace. It is designed to provide a more calm and polite "indoor voice" experience when handling user input.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `indoor.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python indoor.py
   ```

4. The program will prompt you to enter some text. After you press Enter, it will output the same text in lowercase.

## Program Code

```python
# indoor.py

# Print user input into lower case
print(input().lower())
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Enter various types of input, including text with uppercase letters, numbers, punctuation, and whitespace.
3. The program should output the input in lowercase while keeping the punctuation and whitespace unchanged.

## Sample Test Cases

1. **Input:** HELLO
   **Output:** hello

2. **Input:** THIS IS CS50
   **Output:** this is cs50

3. **Input:** 50
   **Output:** 50

## Additional Notes

Remember to save the `indoor.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, make sure you are in the correct directory and have saved the file with the correct name.
