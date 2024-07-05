# Meal Time

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 1 - Meal Time Problem Set](https://cs50.harvard.edu/python/2022/psets/1/meal/), named `meal.py`, helps you determine whether it's time for breakfast, lunch, or dinner based on the input time. The program prompts the user for a time in 24-hour format and outputs the corresponding meal time if it falls within the specified meal time ranges.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `meal.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python meal.py
   ```

4. The program will prompt you to enter the current time in the format "hh:mm" (24-hour format). After you press Enter, it will output whether it's time for breakfast, lunch, or dinner. If it's not time for a meal, it won't output anything.

## Program Code

```python
# meal.py

def main():
    time = input("What time is it? ")
    converted_time = convert(time)
    print(tell_meal(converted_time))

def tell_meal(t):
    if 7.00 <= t <= 8.00:
        return "breakfast time"
    elif 12.00 <= t <= 13.00:
        return "lunch time"
    elif 18.00 <= t <= 19.00:
        return "dinner time"
    else:return None

def convert(time):
    hour, minutes = [int(i) for i in time.split(":")]
    return round(hour + minutes/60, 2)

if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Enter various times in the format "hh:mm" (24-hour format).
3. The program should determine whether it's breakfast time, lunch time, or dinner time based on the input time and output the corresponding message.

## Sample Test Cases

1. **Time:** 7:00
   **Result:** breakfast time

2. **Time:** 7:30
   **Result:** breakfast time

3. **Time:** 12:42
   **Result:** lunch time

4. **Time:** 18:32
   **Result:** dinner time

## Additional Notes

Remember to save the `meal.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, make sure you are in the correct directory and have saved the file with the correct name.

Optionally, if you're up for a challenge, you can try adding support for 12-hour times (a.m. and p.m.) as mentioned in the "Challenge" section of the prompt.