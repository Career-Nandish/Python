# Tip Calculator

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 0 - Tip Calculator Problem Set](https://cs50.harvard.edu/python/2022/psets/0/tip/), named `tip.py`, calculates the tip amount for a restaurant meal based on the meal cost and the desired tip percentage. The program includes functions `dollars_to_float` and `percent_to_float` to convert input strings to corresponding float values for dollars and percentages.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `tip.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python tip.py
   ```

4. The program will prompt you to enter the meal cost (in the format $##.##) and the desired tip percentage (in the format ##%). After you provide the inputs, it will output the calculated tip amount.

## Program Code

```python
# tip.py

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d.replace('$', ''))

def percent_to_float(p):
    return float(p.replace('%', ''))/100

if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Enter various meal costs in the format $##.## and desired tip percentages in the format ##%.
3. The program should output the calculated tip amount based on the provided inputs.

## Sample Test Cases

1. **How much was the meal?** $50.00
   **What percentage would you like to tip?** 15%
   **Leave** $7.50

2. **How much was the meal?** $100.00
   **What percentage would you like to tip?** 18%
   **Leave** $18.00

3. **How much was the meal?** $15.00
   **What percentage would you like to tip?** 25%
   **Leave** $3.75

## Additional Notes

Remember to save the `tip.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, make sure you are in the correct directory and have saved the file with the correct name.