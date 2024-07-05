# Guessing Game

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 4 - Guessing Game Problem Set](https://cs50.harvard.edu/python/2022/psets/4/game/). The `game.py` program implements a simple number guessing game. The program prompts the user to enter a level, generates a random number within the specified range, and then allows the user to make guesses. The program provides feedback on whether the guess is too small, too large, or just right.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `game.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python game.py
   ```

4. The program will prompt you to enter a level. Enter a positive integer to set the maximum range for the random number.

5. The program will then prompt you to make a guess. Enter an integer as your guess.

6. Based on your guess, the program will provide feedback: "Too small!" if the guess is smaller than the generated number, "Too large!" if the guess is larger, or "Just right!" if the guess matches the generated number.

7. If the guess is "Just right!" the program will exit. If the guess is not correct, you can make more guesses.

## Program Code

```python
# game.py

import random

def get_input(prompt):
    while True:
        try:
            inp = int(input(prompt))
            if inp > 0:
                break
        except ValueError:
            pass
    return inp

def check_guess(inp):
    while True:
        guess = get_input("Guess: ")
        if guess < inp:
            print("Too small!")
        elif guess > inp:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()

def main():
    inp = get_input("Level: ")
    check_guess(random.randint(1,inp))

if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Follow the program's prompts to enter a level and make guesses.
3. The program will provide feedback based on your guesses and exit when you guess the correct number.

## Sample Test Cases

1. **Invalid Level Input:**
   - **Input:**
     ```
     Level: cat
     ```
     reprompt for input
     ```
     Level:
     ```

2. **Invalid Level (Negative Number):**
   - **Input:**
     ```
     Level: -1
     ```
     reprompt for input
     ```
     Level:
     ```

3. **Valid Level:**
   - **Input (Level):**
     ```
     Level: 10
     ```
   - **Invalid Guess - Input (Guess):**
     ```
     Guess: cat
     ```
     reprompt for guess
     ```
     Guess:
     ```
   - **Valid Guess but too small - Input (Guess):**
     ```
     Guess: 5
     ```
     ```
     Too small!
     ```
     reprompt for guess
     ```
     Guess:
     ```
   - **Valid Guess but too large - Input (Guess):**
     ```
     Guess: 5
     ```
     ```
     Too large!
     ```
     reprompt for guess
     ```
     Guess:
     ```
   - **Valid Guess - Input (Guess):**
     ```
     Guess: 5
     ```
     ```
     Just right!
     ```

## Additional Notes

- Make sure to save the `game.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, ensure you are in the correct directory and have saved the file with the correct name.
- The program uses the `random` module to generate a random number within the specified range. The generated number serves as the target for the user's guesses.