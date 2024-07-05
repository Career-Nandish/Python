# Playback Speed

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 0 - Playback Speed Problem Set](https://cs50.harvard.edu/python/2022/psets/0/playback/), named `playback.py`, prompts the user for input and then outputs the same input, replacing each space with three periods (`...`). This simulates a slower playback speed or deliberate pausing between words, similar to certain speech patterns observed in videos.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `playback.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python playback.py
   ```

4. The program will prompt you to enter some text. After you press Enter, it will output the input text with spaces replaced by `...`.

## Program Code

```python
# playback.py

# Replace spaces with ...
print(input().replace(' ', '...'))
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Enter various types of input with spaces.
3. The program should output the input text with spaces replaced by ....

## Sample Test Cases

1. **Input:** This is CS50
   **Output:** This...is...CS50

2. **Input:** This is our week on functions
   **Output:** This...is...our...week...on...functions

3. **Input:** Let's implement a function called hello
   **Output:** Let's...implement...a...function...called...hello

## Additional Notes

Remember to save the playback.py file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, make sure you are in the correct directory and have saved the file with the correct name.
