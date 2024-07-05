# CS50 P-Shirt

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 6 - CS50 P-Shirt Problem Set](https://cs50.harvard.edu/python/2022/psets/6/shirt/). The `shirt.py` program allows you to virtually try on a CS50 t-shirt by overlaying a transparent shirt image on your photo. Here's a guide on how to use and understand the program.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `shirt.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the `python` command and provide the filenames of the input and output images as arguments:

   ```
   python shirt.py input.jpg output.png
   ```

   Replace `input.jpg` with the name of the photo you want to try the shirt on, and `output.png` with the name of the resulting image that will have the virtual shirt.

## Program Explanation

The `shirt.py` program uses the Python Imaging Library (Pillow) to perform the virtual shirt try-on process. Here's a brief explanation of the program's functionality:

1. The program checks if the user has provided exactly two command-line arguments.

2. It then checks if both input and output filenames have valid extensions (`.jpg`, `.jpeg`, or `.png`), case-insensitively.

3. If the extensions are valid, the program reads the input image using `Image.open()` from Pillow.

4. The program opens the [shirt.png](https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png) file, which has a transparent background, using `Image.open()`.
    - Download [muppets.zip](https://cs50.harvard.edu/python/2022/psets/6/shirt/muppets.zip)

5. The input image is resized to match the dimensions of the shirt image using `ImageOps.fit()` from Pillow.

6. The program overlays the resized shirt image on the input image using `Image.paste()`.

7. The resulting image with the virtual shirt is saved using `Image.save()` to the specified output filename.

## How to Test

1. Follow the steps mentioned in the "How to Run the Program" section to run the `shirt.py` program.
2. Provide the name of an existing image as the input argument and a desired output filename as the output argument.
3. The program will read the input image, overlay the virtual shirt, resize and paste it, and save the resulting image.

## Additional Notes

- The program performs error handling to handle cases where the user provides incorrect command-line arguments or the specified files do not exist.
- The program's functionality is dependent on the presence of the `shirt.png` file, which is provided by CS50. Make sure to keep this file in the same directory as your `shirt.py` program.
- The `Pillow` library needs to be installed to run the program. If you haven't installed it already, you can do so using the command:
  ```
  pip install Pillow
  ```