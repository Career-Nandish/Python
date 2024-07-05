# Home Federal Savings Bank

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 1 - Home Federal Savings Bank Problem Set](https://cs50.harvard.edu/python/2022/psets/1/bank/), named `bank.py`, simulates the scenario from [Seinfeld](https://en.wikipedia.org/wiki/Seinfeld) where a bank offers different rewards based on the user's greeting. The program prompts the user for a greeting, analyzes the greeting's content, and then outputs the corresponding reward: $0 for greetings starting with "hello", $20 for greetings starting with "h" (excluding "hello"), and $100 for other greetings.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `bank.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python bank.py
   ```

4. The program will prompt you to enter a greeting. After you press Enter, it will output the corresponding reward amount.

## Program Code

```python
# bank.py

import re
greet = input("Greeting: ").strip().lower()
if re.match(r'^hello.*$', greet):
    print("$0")
elif greet[0] == 'h':
    print("$20")
else:
    print("$100")
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Enter various greetings, including "hello", greetings starting with "h", and other greetings.
3. The program should output the corresponding reward based on the provided greetings.

## Sample Test Cases

1. **Greeting:** Hello
   **Reward:** $0

2. **Greeting:** Hello, Newman
   **Reward:** $0

3. **Greeting:** How you doing?
   **Reward:** $20

4. **Greeting:** What's happening?
   **Reward:** $100

## Additional Notes

Remember to save the `bank.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, make sure you are in the correct directory and have saved the file with the correct name.