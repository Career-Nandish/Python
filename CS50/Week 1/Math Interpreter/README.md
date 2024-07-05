# Math Interpreter

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 1 - Math Interpreter Problem Set](https://cs50.harvard.edu/python/2022/psets/1/interpreter/), named `interpreter.py`, acts as a simple interpreter for arithmetic expressions. The program prompts the user for an arithmetic expression in the format "x y z", where `x` and `z` are integers, and `y` is an operator (+, -, *, /). The program then calculates the result of the expression and outputs the result as a floating-point value formatted to one decimal place.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `interpreter.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python interpreter.py
   ```

4. The program will prompt you to enter an arithmetic expression in the format "x y z". After you press Enter, it will output the result of the expression as a floating-point value rounded to one decimal place.

## Program Code

```python
# interpreter.py

expr = input("Expression: ").strip()
x, y, z = expr.split(" ")
x = int(x)
z = int(z)
match y:
    case "+":
        print(float(x + z))
    case "-":
        print(float(x - z))
    case "*":
        print(float(x * z))
    case "/":
        print(float(x / z))

```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Enter various arithmetic expressions in the format "x y z", where `x` and `z` are integers, and `y` is an operator (+, -, *, /).
3. The program should calculate and output the result of the expression as a floating-point value rounded to one decimal place.

## Sample Test Cases

1. **Expression:** 1 + 1
   **Result:** 2.0

2. **Expression:** 2 - 3
   **Result:** -1.0

3. **Expression:** 2 * 2
   **Result:** 4.0

4. **Expression:** 50 / 5
   **Result:** 10.0

## Additional Notes

Remember to save the `interpreter.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, make sure you are in the correct directory and have saved the file with the correct name.