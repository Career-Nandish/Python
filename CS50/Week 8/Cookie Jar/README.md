# Cookie Jar

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 8 - Cookie Jar Problem Set](https://cs50.harvard.edu/python/2022/psets/8/jar/). The Cookie Jar program, implemented in `jar.py`, simulates a cookie jar with the following methods:

- `__init__(self, capacity=12)`: Initializes a cookie jar with the specified capacity. Raises a ValueError if the capacity is not a non-negative integer.
- `__str__(self)`: Returns a string representation of the cookie jar using 🍪 characters to indicate the number of cookies in the jar.
- `deposit(self, n)`: Adds `n` cookies to the jar. Raises a ValueError if the deposit would exceed the jar's capacity.
- `withdraw(self, n)`: Removes `n` cookies from the jar. Raises a ValueError if there aren't enough cookies in the jar.
- `capacity(self)`: Returns the jar's capacity.
- `size(self)`: Returns the number of cookies currently in the jar.

## How to Use the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `jar.py` file.

   ```sh
   cd path/to/your/directory
   ```

3. Run the program using the `python` command:

   ```sh
   python jar.py
   ```

4. The program will interactively prompt you to test various functionalities of the cookie jar.

## Class Explanation

The `Jar` class effectively simulates the behavior of a cookie jar. Here's how it works:

1. The `__init__` method initializes the cookie jar with a specified capacity.
2. The `__str__` method returns a string representation of the cookie jar using 🍪 characters.
3. The `deposit` method adds cookies to the jar, adjusting the size attribute accordingly.
4. The `withdraw` method removes cookies from the jar, updating the size attribute.
5. The `capacity` property returns the capacity of the cookie jar.
6. The `size` property returns the number of cookies currently in the jar.

## How to Test

1. Open your terminal.
2. Navigate to the directory where you have saved the `test_jar.py` file.

   ```sh
   cd path/to/your/directory
   ```

3. Run the tests using the `pytest` command:

   ```sh
   pytest test_jar.py
   ```

4. The tests will run, and you will see the results indicating whether the program passes each test case.

## Additional Notes

- The program uses a class structure to create a virtual cookie jar with various functionalities.
- The tests provided in the `test_jar.py` file ensure that the program behaves as expected.
- The class methods and properties are designed to handle various scenarios, including invalid inputs and exceeding the jar's capacity.
- Remember to thoroughly test the program and ensure it meets all requirements.