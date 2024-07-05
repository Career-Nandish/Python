# Emojize

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 4 - Emojize Problem Set](https://cs50.harvard.edu/python/2022/psets/4/emojize/), `emojize.py` program converts text codes or aliases in English to their corresponding emojis. This adds a fun and expressive touch to your messages or documents.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `emojize.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python emojize.py
   ```

4. The program will prompt you to enter a string in English, including any text codes or aliases you want to convert to emojis.

5. After entering the input string, the program will display the "emojized" version of the string with the corresponding emojis replacing the text codes or aliases.

## Program Code

```python
# emojize.py

from emoji import emojize
print(emojize(input("Input: "), language='alias'))
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Enter a string that includes text codes or aliases (e.g., :thumbs_up: or :smile:).
3. The program will display the emojized version of the input string with emojis replacing the text codes or aliases.

## Sample Test Cases

1. **Input:**
   ```
   :1st_place_medal:
   ```
   **Result:**
   ```
   Output: 🥇
   ```

2. **Input:**
   ```
   :money_bag:
   ```
   **Result:**
   ```
   Output: 💰
   ```

3. **Input:**
   ```
   :smile_cat:
   ```
   **Result:**
   ```
   Output: 😸
   ```

## Additional Notes

- Make sure to save the `emojize.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, ensure you are in the correct directory and have saved the file with the correct name.
- The `emoji` module used in the program requires installation. You can install it using the following command:

  ```
  pip install emoji
  ```

- The program uses the `language='alias'` parameter to enable the conversion of aliases. Aliases are shorter versions of text codes that can also be used to represent emojis.
- Experiment with different text codes and aliases to see how they are converted into emojis using the program.