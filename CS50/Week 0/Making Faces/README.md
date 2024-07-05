# Making Faces

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 0 - Making Faces Problem Set](https://cs50.harvard.edu/python/2022/psets/0/faces/), named `faces.py`, provides functionality to convert emoticons like :) and :( to their corresponding emoji equivalents, namely 🙂 (slightly smiling face) and 🙁 (slightly frowning face). The program includes a `convert` function that performs the conversion, and a `main` function that prompts the user for input, calls the `convert` function, and prints the result.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `faces.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python faces.py
   ```

4. The program will prompt you to enter some text. After you press Enter, it will output the input text with converted emoticons.

## Program Code

```python
# faces.py

def convert(text):
    return text.replace(':)', '🙂').replace(':(', '🙁')

def main():
    text = input("Write your text here : ")
    print(convert(text))

if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Enter various types of input containing :) and :( emoticons.
3. The program should output the input text with the corresponding emoji conversions.

## Sample Test Cases

1. **Input:** Hello :)
   **Output:** Hello 🙂

2. **Input:** Goodbye :(
   **Output:** Goodbye 🙁

3. **Input:** Hello :) Goodbye :(
   **Output:** Hello 🙂 Goodbye 🙁

## Additional Notes

Remember to save the `faces.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, make sure you are in the correct directory and have saved the file with the correct name.