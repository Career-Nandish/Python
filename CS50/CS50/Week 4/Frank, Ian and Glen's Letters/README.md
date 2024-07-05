# Frank, Ian and Glen’s Letters

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 4 - Frank, Ian and Glen’s Letters Problem Set](https://cs50.harvard.edu/python/2022/psets/4/figlet/). The `figlet.py` program allows you to convert text into ASCII art using different fonts supported by the FIGlet library. You can choose to use a specific font or let the program select a random font for you.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `figlet.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python figlet.py
   ```

4. The program will prompt you to provide either zero or two command-line arguments:

   - If you provide zero arguments, the program will prompt you to enter the text you want to convert. It will then randomly select a font and display the ASCII art.
   - If you provide two arguments (`-f` or `--font` followed by the font name), the program will prompt you to enter the text you want to convert. It will then display the ASCII art using the specified font.

5. After entering the input text and font (if applicable), the program will display the ASCII art generated using FIGlet.

## Program Code

```python
# figlet.py

import sys
from pyfiglet import Figlet

def main():
    # input
    inp = input("Input: ")

    if len(sys.argv) == 1:
        f = Figlet()
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-f' or sys.argv[1] == '--font':
            f = Figlet(sys.argv[2])
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")

    # Output
    print("Output: \n" , f.renderText(inp))


if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Follow the program's prompts to provide command-line arguments and input text.
3. The program will display the ASCII art generated using FIGlet based on your input and font selection.

## Sample Test Cases

1. **Invalid Usage:**
   - **Input:**
     ```
     $ python figlet.py test
     ```
   - **Output:**
     ```
     Invalid usage
     ```

2. **Without "-f" or "--font" Flag:**
   - **Input:**
     ```
     $ python figlet.py -a slant
     ```
   - **Output:**
     ```
     Invalid usage 
     ```

3. **Without Valid Font:**
   - **Input:**
     ```
     $ python figlet.py -f invalid_font
     ```
   - **Output:**
     ```
     Invalid usage                   
     ```      

4. **Random Font:**
   - **Input:**
     ```
     $ python figlet.py
     ```
   - **Input:**
     ```
     hello, world
     ```
   - **Output:**
     (ASCII art generated using a randomly selected font)

5. **Specific Font:**
   - **Input:**
     ```
     $ python figlet.py -f slant
     ```
   - **Input:**
     ```
     CS50
     ```
   - **Output:**
     ```
        ___________ __________ 
       / ____/ ___// ____/ __ \
      / /    \__ \/___ \/ / / /
     / /___ ___/ /___/ / /_/ / 
     \____//____/_____/\____/  
     ```

6. **Specific Font:**
   - **Input:**
     ```
     $ python figlet.py -f rectangles
     ```
   - **Input:**
     ```
     Hello, world
     ```
   - **Output:**
     ```
      _____     _ _                        _   _ 
     |  |  |___| | |___      _ _ _ ___ ___| |_| |
     |     | -_| | | . |_   | | | | . |  _| | . |
     |__|__|___|_|_|___| |  |_____|___|_| |_|___|
                       |_|                       
     ```      

## Additional Notes

- Make sure to save the `figlet.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, ensure you are in the correct directory and have saved the file with the correct name.
- The program uses the `pyfiglet` library to generate ASCII art from text. You can install it using the following command:

  ```
  pip install pyfiglet
  ```

- The program supports both randomly selecting a font and selecting a specific font based on command-line arguments.
- Experiment with different fonts and input text to see how they are transformed into ASCII art using the program.