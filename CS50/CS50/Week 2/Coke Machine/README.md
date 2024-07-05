# Coke Machine

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 2 - Coke Machine Problem Set](https://cs50.harvard.edu/python/2022/psets/2/coke/), named `coke.py`, simulates a coke machine that accepts coins of 25 cents, 10 cents, and 5 cents. The program prompts the user to insert coins one at a time until the total inserted amount reaches at least 50 cents. After that, it calculates and outputs the change owed to the user.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `coke.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python coke.py
   ```

4. The program will prompt you to insert coins one at a time. After you insert enough coins to reach at least 50 cents, it will output the change owed to you.

## Program Code

```python
# coke.py

def main():
    balance = 50
    accepted_denom = [25, 10, 5]
    while balance > 0:
        print("Amount Due:", balance)
        insert = int(input("Insert Coin: "))
        if insert in accepted_denom:
            if balance > insert:
                balance -= insert
            else:
                print("Change Owed:", insert - balance)
                break
        else:
            pass

if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Follow the prompts to insert coins of 25 cents, 10 cents, or 5 cents.
3. Once you have inserted enough coins to reach 50 cents or more, the program will output the change owed to you.

## Sample Test Cases

1. **Amount Due:** 50
   **Insert Coin:** 25
   **Amount Due:** 25
   **Insert Coin:** 25
   **Change Owed:** 0

2. **Amount Due:** 50
   **Insert Coin:** 25
   **Amount Due:** 25
   **Insert Coin:** 10
   **Amount Due:** 15
   **Insert Coin:** 25
   **Change Owed:** 10

## Additional Notes

Remember to save the `coke.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, make sure you are in the correct directory and have saved the file with the correct name.