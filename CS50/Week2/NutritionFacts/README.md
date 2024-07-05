# Nutrition Facts

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 2 - Nutrition Facts Problem Set](https://cs50.harvard.edu/python/2022/psets/2/nutrition/), named `nutrition.py`, allows users to input a fruit and outputs the number of calories in one portion of that fruit, based on information from the FDA's poster for fruits. The program handles input in a case-insensitive manner and matches the input fruit with its corresponding calories from the provided list.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `nutrition.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python nutrition.py
   ```

4. The program will prompt you to enter a fruit. After you enter the fruit, it will output the number of calories in one portion of that fruit based on the FDA's information.

## Program Code

```python
# nutrition.py

def main():
    item = input("Item: ")
    match item.lower():
        case "apple":
                print("Calories:",130)
        case "avocado":
                print("Calories:",50)
        case "banana":
                print("Calories:","110")
        case "cantaloupe":
                print("Calories:","50")
        case "grapefruit":
                print("Calories:","60")
        case "grapes":
                print("Calories:","90")
        case "honeydew melon":
                print("Calories:","50")
        case "kiwifruit":
                print("Calories:","90")
        case "lemon":
                print("Calories:","15")
        case "lime":
                print("Calories:","20")
        case "nectarine":
                print("Calories:","60")
        case "orange":
                print("Calories:","80")
        case "peach":
                print("Calories:","60")
        case "pear":
                print("Calories:","100")
        case "pineapple":
                print("Calories:","50")
        case "plums":
                print("Calories:","70")
        case "strawberries":
                print("Calories:","50")
        case "sweet cherries":
                print("Calories:","100")
        case "tangerine":
                print("Calories:","50")
        case "watermelon":
                print("Calories:","80")
        case _:
                print("Fruit Not found.")

if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Follow the prompts to enter various fruit names. Make sure to vary the casing of your input (e.g., "apple," "Apple," "APPLE").
3. The program will output the number of calories in one portion of the entered fruit if it matches the list of fruits. If the entered fruit is not found in the list, the program will display nothing.

## Sample Test Cases

1. **Input:** Apple
   **Result:** Calories: 130

2. **Input:** Avocado
   **Result:** Calories: 50

3. **Input:** Sweet Cherries
   **Result:** Calories: 100

4. **Input:** Tomato
   **Result:**

## Additional Notes

Make sure to save the `nutrition.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, ensure you are in the correct directory and have saved the file with the correct name.