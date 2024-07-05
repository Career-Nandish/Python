# Deep Thought

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 1 - Deep Thought Problem Set](https://cs50.harvard.edu/python/2022/psets/1/deep/), named `deep.py`, simulates the scenario from "The Hitchhiker's Guide to the Galaxy" by Douglas Adams. It prompts the user for the answer to the Great Question of Life, the Universe, and Everything and outputs "Yes" if the input matches 42, "forty-two", or "forty two" in a case-insensitive and space-tolerant manner. Otherwise, it outputs "No".

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `deep.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python deep.py
   ```

4. The program will prompt you to enter your answer to the Great Question. After you press Enter, it will output "Yes" if the answer matches the specified criteria or "No" if it doesn't.

## Program Code

```python
# deep.py

ans = input("What's the answer to the Great Question of Life, \
          the Universe and Everything? ").strip().lower()
if ans == '42' or ans == 'forty-two' or ans == 'forty two':
    print("Yes")
else:
    print("No")
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Enter various answers, including 42, "forty-two", "forty two", and other values.
3. The program should output "Yes" for the specified inputs and "No" for other inputs, while ignoring case and tolerating spaces.

## Sample Test Cases

1. **Input:** 42
   **Output:** Yes

2. **Input:** Forty Two
   **Output:** Yes

3. **Input:** forty-two
   **Output:** Yes

4. **Input:** 50
   **Output:** No

## Additional Notes

Remember to save the `deep.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, make sure you are in the correct directory and have saved the file with the correct name.