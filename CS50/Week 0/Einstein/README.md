# Einstein

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 0 - Einstein Problem Set](https://cs50.harvard.edu/python/2022/psets/0/einstein/), named `einstein.py`, calculates the energy equivalent (in Joules) of a given mass (in kilograms) using Einstein's mass-energy equivalence formula, E = mc^2. The program prompts the user for mass as an integer (in kilograms) and outputs the equivalent energy in Joules.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `einstein.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python einstein.py
   ```

4. The program will prompt you to enter the mass (in kilograms). After you press Enter, it will output the energy equivalent in Joules.

## Program Code

```python
# einstein.py

def main():
    m = int(input("Enter the value of m(in kg) = "))
    c = 300000000  # meters per second
    
    e = m * (c ** 2)
    print(f"E = {e}")

if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Enter various mass values in kilograms.
3. The program should output the energy equivalent in Joules based on Einstein's mass-energy equivalence formula.

## Sample Test Cases

1. **m:** 1
   **E:** 90000000000000000

2. **m:** 14
   **E:** 1260000000000000000

3. **m:** 50
   **E:** 4500000000000000000

## Additional Notes

Remember to save the `einstein.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, make sure you are in the correct directory and have saved the file with the correct name.