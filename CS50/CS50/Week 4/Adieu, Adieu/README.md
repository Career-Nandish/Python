# Adieu

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 4 - Adieu, Adieu Problem Set](https://cs50.harvard.edu/python/2022/psets/4/adieu/). The `adieu.py` program takes a list of names as input from the user and bids adieu to those names in a grammatically correct manner. It separates the names using the appropriate punctuation, such as commas and the word "and," based on the number of names provided.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `adieu.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python adieu.py
   ```

4. The program will prompt you to enter names, one per line. After entering the names, press `Ctrl-D` to indicate the end of input.

5. The program will then display the farewell message bidding adieu to the entered names.

## Program Code

```python
# adieu.py

import sys
import inflect

def main():
    names = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            break

    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        print("Adieu, adieu, to " + ', '.join(names[:-1]) + ', and ' + names[-1])

if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Follow the program's prompts to enter names.
3. After entering all the names, press `Ctrl-D` to indicate the end of input.
4. The program will display the farewell message bidding adieu to the entered names.

## Sample Test Cases

1. **Single Name:**
   - **Input:**
     ```
     Liesl (press Enter)
     (Press Ctrl-D)
     ```
   - **Output:**
     ```
     Adieu, adieu, to Liesl
     ```

2. **Multiple Names:**
   - **Input:**
     ```
     Liesl (press Enter)
     Friedrich (press Enter)
     (Press Ctrl-D)
     ```
   - **Output:**
     ```
     Adieu, adieu, to Liesl and Friedrich
     ```

3. **Three Names:**
   - **Input:**
     ```
     Liesl (press Enter)
     Friedrich (press Enter)
     Louisa (press Enter)
     (Press Ctrl-D)
     ```
   - **Output:**
     ```
     Adieu, adieu, to Liesl, Friedrich, and Louisa
     ```

## Additional Notes

- Make sure to save the `adieu.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, ensure you are in the correct directory and have saved the file with the correct name.
- The program uses the `inflect` library to generate grammatically correct farewell messages for different numbers of names. You can install it using the following command:

  ```
  pip install inflect
  ```

- Experiment with different numbers of names to see how the program generates the farewell message based on the number of names provided.