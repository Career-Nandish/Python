# Felipe’s Taqueria

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 3 - Felipe’s Taqueria Problem Set](https://cs50.harvard.edu/python/2022/psets/3/taqueria/), named `taqueria.py`, simulates an order system for Felipe's Taqueria. The program allows a user to place an order by inputting menu items. After each input, the program displays the total cost of all items inputted so far, formatted as a dollar amount with two decimal places. The program treats the user's input case insensitively and ignores any input that isn't a valid menu item.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `taqueria.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python taqueria.py
   ```

4. The program will prompt you to enter menu items one by one. After each input, it will display the updated total cost of all items inputted so far.

## Program Code

```python
# taqueria.py

def take_order(prompt, menu):
    total = 0
    while True:
        try:
            item = input(prompt).title()
            if item not in menu:
                print(f"We don't sell {item}s")
            else:
                total += menu[item]
                print(f"Total: ${total:.2f} ")
        except EOFError:
            print(f"\nThanks for your order, your total is ${total:.2f}.")
            break

def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    take_order("What would you like to have?: ", menu)

if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Follow the prompts to enter various menu items. Make sure to test both upper and lower case inputs, as well as mixed case inputs.
3. After each input, the program will display the total cost of all items entered so far.
4. When you're done entering items, press `Ctrl-D` (or `Ctrl-Z` on Windows) to signal the end of input. The program will exit, and your order summary will be displayed.

## Sample Test Cases

1. **Input:** Taco (or taco) and Taco
   **Result:** Total: $6.00

2. **Input:** Baja Taco (or baja taco) and Tortilla Salad (or tortilla salad)
   **Result:** Total: $12.00

3. **Input:** Burger
   **Result:** (no output)

## Additional Notes

Make sure to save the `taqueria.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, ensure you are in the correct directory and have saved the file with the correct name.