# Outdated

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 3 - Outdated Problem Set](https://cs50.harvard.edu/python/2022/psets/3/outdated/), named `outdated.py`, helps you convert dates from the month-day-year (MM/DD/YYYY) format or month day, year format (e.g., September 8, 1636) to the international standard format, which is year-month-day (YYYY-MM-DD). This standard format ensures that dates are consistently sorted and unambiguous, regardless of the country.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `outdated.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python outdated.py
   ```

4. The program will prompt you to enter a date in one of the supported formats. You can enter dates in either MM/DD/YYYY format (e.g., 9/8/1636) or month day, year format (e.g., September 8, 1636).

5. After entering the date, the program will process the input and display the date in the standard YYYY-MM-DD format.

## Program Code

```python
# outdated.py

import re
from datetime import datetime

def convert_date(inp):

    pattern1 = r'^\d{1,2}/\d{1,2}/\d{4}$'
    pattern2 = r'^\w+ \d{1,2}, \d{4}$'

    if re.match(pattern1, inp):
        try:
            return datetime.strptime(inp, "%m/%d/%Y").strftime("%Y-%m-%d")
        except ValueError:
            return 0

    elif re.match(pattern2, inp):
        try:
            return datetime.strptime(inp, "%B %d, %Y").strftime("%Y-%m-%d")
        except ValueError:
            return 0

    return 0

def main():
    while True:
        inp = input("Date: ").strip()
        date = convert_date(inp)
        if date:
            print(date)
            break
        else:
            print("Invalid date format. Please try again.")

if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Follow the prompts to enter various dates in both supported formats.
3. After processing the input, the program will display the inputted date in the standard YYYY-MM-DD format.

## Sample Test Cases

1. **Input:**
   ```
   9/8/1636
   ```
   **Result:**
   ```
   1636-09-08
   ```

2. **Input:**
   ```
   September 8, 1636
   ```
   **Result:**
   ```
   1636-09-08
   ```

3. **Input:**
   ```
   23/6/1912
   ```
   **Result:**
   *(The program will prompt for input again)*

4. **Input:**
   ```
   December 80, 1980
   ```
   **Result:**
   *(The program will prompt for input again)*

## Additional Notes

Make sure to save the `outdated.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, ensure you are in the correct directory and have saved the file with the correct name.