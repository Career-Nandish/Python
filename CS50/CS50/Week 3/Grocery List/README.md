# Grocery List

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 3 - Grocery List Problem Set](https://cs50.harvard.edu/python/2022/psets/3/grocery/), named `grocery.py`, helps you organize your grocery list by counting the occurrences of each item, sorting them alphabetically, and displaying the results. The program prompts the user to input grocery items, one per line, until the user inputs `Ctrl-D` (or `Ctrl-Z` on Windows) to signal the end of input. After processing the input, the program displays each item's count and the item itself in uppercase, sorted alphabetically.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `grocery.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python grocery.py
   ```

4. The program will prompt you to enter grocery items one by one. After each input, it will process the input and keep track of the item counts.

5. When you're done entering items, press `Ctrl-D` (or `Ctrl-Z` on Windows) to signal the end of input. The program will display the organized grocery list.

## Program Code

```python
# grocery.py

def take_grocery_list():
    grocery_dict = {}
    while True:
        try:
            item = input().upper()
            if item not in grocery_dict:
                grocery_dict[item] = 1
            else:
                grocery_dict[item] += 1
        except EOFError:
            return grocery_dict

def prettify_grocery_list(d):
    grocery_list = ''
    for k in sorted(d.keys()):
        grocery_list += (str(d[k]) + ' ' +  k)
        grocery_list += '\n'
    return grocery_list

def main():
    print(prettify_grocery_list(take_grocery_list()))

if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Follow the prompts to enter various grocery items. Make sure to test both upper and lower case inputs, as well as mixed case inputs.
3. After processing the input, the program will display each item's count and the item itself in uppercase, sorted alphabetically.
4. When you're done entering items, press `Ctrl-D` (or `Ctrl-Z` on Windows) to signal the end of input. The program will display the organized grocery list.

## Sample Test Cases

1. **Input:**
   ```
   mango
   strawberry
   ```
   **Result:**
   ```
   1 MANGO
   1 STRAWBERRY
   ```

2. **Input:**
   ```
   milk
   milk
   ```
   **Result:**
   ```
   2 MILK
   ```

3. **Input:**
   ```
   tortilla
   sweet potato
   ```
   **Result:**
   ```
   1 SWEET POTATO
   1 TORTILLA
   ```

## Additional Notes

Make sure to save the `grocery.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, ensure you are in the correct directory and have saved the file with the correct name.