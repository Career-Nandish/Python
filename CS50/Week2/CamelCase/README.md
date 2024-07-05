# camelCase

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 2 - camelCase Problem Set](https://cs50.harvard.edu/python/2022/psets/2/camel/), named `camel.py`, helps you convert variable names from camel case to snake case. In some programming languages, camel case is used to name variables where the first word is lowercase and subsequent words start with uppercase letters. Snake case, on the other hand, uses underscores (_) to separate words, and all letters are in lowercase. This program takes a variable name in camel case as input and outputs the corresponding name in snake case.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `camel.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python camel.py
   ```

4. The program will prompt you to enter a variable name in camel case. After you press Enter, it will output the variable name in snake case.

## Program Code

```python
# camel.py

def camelToSnakeCase(s):
    snake_string = ''
    for i in s:
        if not i.isupper():
            snake_string += i
        else:
            snake_string += ('_' + i.lower())
    return snake_string

def main():
    camel_string = input("camelCase: ")
    print('snake_case:', camelToSnakeCase(camel_string))

if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Enter various variable names in camel case (e.g., `firstName`, `preferredFirstName`) as prompted by the program.
3. The program should convert the camel case variable names to snake case and output the corresponding names.

## Sample Test Cases

1. **camelCase:** name
   **Result:** snake_case: name

2. **camelCase:** firstName
   **Result:** snake_case: first_name

3. **camelCase:** preferredFirstName
   **Result:** snake_case: preferred_first_name

## Additional Notes

Remember to save the `camel.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, make sure you are in the correct directory and have saved the file with the correct name.