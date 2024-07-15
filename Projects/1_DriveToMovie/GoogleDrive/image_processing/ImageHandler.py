import cv2
import re
from sys import exit
import numpy as np
from os import listdir, path, mkdir
from typing import List, Dict, Generator
from datetime import datetime
from pillow_heif import open_heif


def extract_date(filename: str) -> datetime:
    
    """
    Extracts a date from a filename string formatted as 
    "sometext_YYYY-MM-DD HH_MM_SS.ext".

    Args:
        filename (str): The filename to extract the date from.

    Returns:
        datetime: The extracted date as a datetime object, or None 
                  if no date is found.
    """
    
    try:
        # Regular expression pattern to match the date and time in the filename
        pattern = re.compile(r"(20\d{2}-\d{2}-\d{2} \d{2}_\d{2}_\d{2})")
        
        # Search for the pattern in the filename
        if match := pattern.search(filename):
            # Replace underscores with colons and convert to datetime object
            return datetime.strptime(match.group(1).replace("_", ":"), 
                "%Y-%m-%d %H:%M:%S")
        
    except Exception as error:
        print(f"\n\n**** ERROR EXTRACTING DATE FROM FILENAME '{filename}': {error} ****")
        raise
        
    
    # Return None if no date is found or an error occurs
    return None

def image_modifier(downloading_path: str) -> str:
    
    """
    Modifies images in a given directory by sorting them based on the 
    date in their filenames and saving the altered images in a new directory.

    Args:
        downloading_path (str): The path to the directory containing the images 
                                to be modified.

    Returns:
        str: The path to the directory containing the modified images.
    """
    try:
        # If the directory doesn't exist, exit the workflow
        if not path.exists(downloading_path):
            print(f"==== The directory {downloading_path} doesn't exist. ====")
            print(f"==== Exiting workflow. ====")
            exit()

        split_path = downloading_path.split("\\")
        # Creating a new directory for altered images
        root, folder = "\\".join(split_path[:-1]), split_path[-1]
        modified_folder_path = path.join(root, f"modified_{folder}") 
        
        # If the directory doesn't exist, create it
        if path.exists(modified_folder_path):
            print(f"==== The directory {modified_folder_path} already exists. ====")
        else:
            mkdir(modified_folder_path)
        
        # Sorting filenames based on dates
        sorted_filenames = sorted(listdir(downloading_path), key=extract_date)

        # Total number of files (used for desaturation)
        total_files = len(sorted_filenames)
        
        # Iterate over the sorted filenames
        for counter, file in enumerate(sorted_filenames):
            try:
                # Altering the image
                img_array = image_alteration(path.join(downloading_path, file), 
                    counter + 1, total_files)

                # Extracting extension
                img_ext = file.split('.')[-1]

                # .heic isn't supported by OpenCV, so converting it to jpg
                if img_ext == 'heic':
                    img_ext = "jpg"

                # Creating the path for the altered image
                img_name = path.join(modified_folder_path, f"{counter + 1}.{img_ext}") 

                # Writing the image
                cv2.imwrite(img_name, img_array)

            except Exception as error:
                print(f"\n\n**** ERROR PROCESSING FILES '{file}': {error} ****")

        # Returning path where altered images are stored
        return modified_folder_path
    
    except Exception as error:
        print(f"\n\n**** ERROR IN image_modifier: {error} ****")
        return None

def image_alteration(fname: str, counter: int, total_files: int, 
    max_h: int = 1080, max_w: int = 1920) -> np.ndarray:
    
    """
    Alters an image by resizing, padding, and desaturating it.

    Args:
        fname (str): The path to the image file to be altered.
        counter (int): The current file counter for desaturation calculation.
        total_files (int): The total number of files for desaturation calculation.
        max_h (int, optional): The maximum height for the resized image. Defaults to 1080.
        max_w (int, optional): The maximum width for the resized image. Defaults to 1920.

    Returns:
        np.ndarray: The altered image as a NumPy array.
    """
    
    try:
        # Print the name of the file being altered
        print(f"\n==== Altering file {fname}. ====")

        # Initialize the final image
        final_img = None

        # Iphone users please change your camera settings
        # to most compatible, this is just unproductive
        # Check if the file is a HEIC image
        if fname.split(".")[-1] == "heic":
            try:
                # Use pillow-heif extension to open HEIC images
                img_t = open_heif(fname, convert_hdr_to_8bit=False, bgr_mode=True)
                img = np.asarray(img_t)
            except Exception as error:
                print(f"\n\n****ERROR READING .HEIC FILE '{fname}': {error} ****")
                return final_img
        else:
            try:
                # Load the image from the file using OpenCV
                img = cv2.imread(fname)
            except Exception as error:
                print(f"\n\n****ERROR READING IMAGE FILE '{fname}': {error} ****")
                return final_img

        # Check if the image was loaded successfully
        if img is not None:
            try:
                # Convert grayscale image to BGR
                if len(img.shape) == 2:
                    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
                    
                # Get the actual image dimensions
                img_h, img_w = img.shape[:2]

                # Calculate scaling factors for width and height
                scale_width = max_w / img_w
                scale_height = max_h / img_h

                # Determine scaling factor to fit within max_width and max_height
                scale = min(scale_width, scale_height)

                # Calculate new dimensions after scaling
                new_w = int(img_w * scale)
                new_h = int(img_h * scale)

                # Resize the image
                resized_img = cv2.resize(img, (new_w, new_h))

                # Calculate padding
                top = (max_h - new_h) // 2
                bottom = max_h - new_h - top
                left = (max_w - new_w) // 2
                right = max_w - new_w - left

                # Add padding to the resized image
                pad_img = cv2.copyMakeBorder(resized_img, top, bottom, left, 
                    right, cv2.BORDER_CONSTANT)

                # Calculate the ratio of desaturation based on the number of images
                ratio = counter / total_files  
                    
                # Desaturate the image
                d_img = cv2.cvtColor(pad_img, cv2.COLOR_BGR2GRAY)

                # Merge desaturated image channels
                cd_img = cv2.merge((d_img, d_img, d_img))
                    
                # Blend the original and desaturated image based on the ratio
                final_img = cv2.addWeighted(pad_img, 1 - ratio, cd_img, ratio, 0)

                # Delete temporary images to free up memory
                del img, resized_img, d_img, cd_img

            except Exception as error:
                print(f"\n\n**** ERROR PROCESSING IMAGE'{fname}': {error} ****")
        else:
            print(f"## Unsupported File -  {fname} ##")

        # Returning ndarray of the image
        return final_img
    
    except Exception as error:
        print(f"\n\n**** ERROR IN image_alterations: {error} ****")
        return None