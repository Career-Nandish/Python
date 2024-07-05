# Watch on YouTube

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 7 - Watch on YouTube Problem Set](https://cs50.harvard.edu/python/2022/psets/7/watch/). The `watch.py` program is designed to extract YouTube video URLs from HTML containing embedded video elements. The program aims to convert the longer `src` URLs back to their shorter, shareable `youtu.be` format. Let's take a closer look at how the program works and how to use it.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `watch.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the `python` command:

   ```
   python watch.py
   ```

4. The program will prompt you to enter HTML containing an embedded video element's `src` attribute.
5. Paste the HTML code into the terminal and press Enter.
6. The program will output the shorter `youtu.be` URL equivalent if a valid YouTube video URL is found, otherwise, it will return `None`.

## Program Explanation

The `watch.py` program uses the `re` module to perform regular expression matching to find the `src` attribute value of an embedded video element. It follows these steps:

1. The `parse()` function takes the HTML code as input and attempts to find a valid YouTube URL pattern using regular expressions.
   
2. If a valid pattern is found, the function extracts the URL and converts it to the `youtu.be` format using string manipulation.

3. The function returns the converted URL if found, otherwise, it returns `None`.

## How to Test

1. Follow the steps mentioned in the "How to Run the Program" section to run the `watch.py` program.
2. Copy and paste different HTML codes containing embedded video elements to test whether the program can correctly extract the YouTube URL and convert it to the `youtu.be` format.
```
python watch.py
```
- **Input:**
```
HTML: <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
```
- **Output:**
```
https://youtu.be/xvFZjo5PgG0
```

- **Input:**
```
HTML: <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```
- **Output:**
```
https://youtu.be/xvFZjo5PgG0
```

- **Input:**
```
HTML: <iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>
```
- **Output:**
```
None
```

## Additional Notes

- The program uses regular expressions to extract the `src` attribute value from the input HTML code. It's important to ensure that the regular expression pattern is accurate and covers various possible cases.
- The program provides a basic extraction and conversion process. More complex HTML structures may require additional handling.
- Regular expressions can be quite powerful, but they can also be complex to create and maintain. It's important to thoroughly test the program with different scenarios to ensure its correctness.
- Make sure to thoroughly understand the provided HTML examples and how they match the regular expression pattern in your `parse()` function.