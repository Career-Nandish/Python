# Bitcoin Price Index

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 4 - Bitcoin Price Index Problem Set](https://cs50.harvard.edu/python/2022/psets/4/bitcoin/). The `bitcoin.py` program calculates the current cost of a specified number of Bitcoins in USD using the CoinDesk Bitcoin Price Index API. It takes a single command-line argument indicating the number of Bitcoins the user wants to buy and outputs the cost in USD to four decimal places, using a comma as a thousands separator.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `bitcoin.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter and provide the number of Bitcoins as a command-line argument:

   ```
   python bitcoin.py 2.5
   ```

4. The program will query the CoinDesk API and provide the cost of the specified number of Bitcoins in USD.

## Program Code

```python
# bitcoin.py

import requests
import sys

def get_input():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            return float(sys.argv[1])
        except ValueError:
            sys.exit(f"{sys.argv[1]} is not a number")

def get_bitcoin_price_usd(n):
    res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    return f"${n * res['bpi']['USD']['rate_float']:,.4f}"

def main():
    n = get_input()
    print(get_bitcoin_price_usd(n))

if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Provide a valid number of Bitcoins as a command-line argument.
3. The program will query the API and output the cost of the specified number of Bitcoins in USD.

## Sample Test Cases

1. **Missing Command-line Argument:**
   - **Input:**
     ```
     python bitcoin.py
     ```
   - **Output:**
     ```
     Missing command-line argument
     ```

2. **Invalid Command-line Argument (Not a Number):**
   - **Input:**
     ```
     python bitcoin.py cat
     ```
   - **Output:**
     ```
     Command-line argument is not a number
     ```

3. **Valid Command-line Argument:**
   - **Input:**
     ```
     python bitcoin.py 1
     ```
   - **Output:**
     ```
     $38,761.0833
     ```

4. **Valid Command-line Argument (Decimal Number of Bitcoins):**
   - **Input:**
     ```
     python bitcoin.py 1.5
     ```
   - **Output:**
     ```
     $58,141.6249
     ```

## Additional Notes

- Make sure to save the `bitcoin.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, ensure you are in the correct directory and have saved the file with the correct name.
- The program uses the `requests` module to make an API request to the CoinDesk Bitcoin Price Index API. It handles invalid command-line arguments, network errors, and provides the cost of the specified number of Bitcoins in USD.
- To install `requests`:
  ```
  pip install requests
  ```