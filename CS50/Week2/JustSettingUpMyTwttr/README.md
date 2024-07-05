# Just setting up my twttr

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 2 - Just setting up my twttr Problem Set](https://cs50.harvard.edu/python/2022/psets/2/twttr/), named `twttr.py`, simulates the text shortening commonly seen in texting and tweeting, where vowels (A, E, I, O, and U) are omitted from the input text. The program prompts the user for a string of text and then outputs the same text with all vowels removed, regardless of whether they are in uppercase or lowercase.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `twttr.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python twttr.py
   ```

4. The program will prompt you to enter a string of text. After you enter the text, it will output the same text with all vowels removed.

## Program Code

```python
# twttr.py

def main():
    in_str = input("Input: ")
    print("Output:", remove_vowels(in_str))

def remove_vowels(s):
    out_str = ''
    for i in s:
        if not i.lower() in 'aeiou':
            out_str += i
    return out_str

if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Follow the prompts to enter various strings of text containing vowels.
3. The program will output the entered text with all vowels removed.

## Sample Test Cases

1. **Input:** Twitter
   **Output:** Twttr

2. **Input:** What's your name?
   **Output:** Wht's yr nm?

3. **Input:** CS50
   **Output:** CS50

## Additional Notes

Remember to save the `twttr.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, make sure you are in the correct directory and have saved the file with the correct name.