## 1. [`requirements.txt`](\requirements.txt)

Contains the necessary Python modules to be installed for the project. Make sure to run 

```bash
pip install -r requirements.txt
``` 

to set up the environment.

## 2. [`main.py`](\main.py)

The main script for handling Google Drive operations. It performs the following tasks:

* Imports required modules and functions from various subdirectories.
* Uses `argparse` to parse command-line arguments.
* Initializes `GoogleDriveClient` and interacts with Google Drive to get folder IDs and files.
* Manages file downloads, modifies images, creates videos, and applies audio processing.
* Displays messages using cowsay to indicate the start and end of the project.

Here's a quick breakdown of the script:

### 1. Imports:

* Imports from `google_drive`, `file_handling`, `image_processing`, `video_processing`, and `audio_processing` subdirectories.
* Imports `sys` and `path` from the `os` module to manage paths.
* Uses `cowsay` for display messages.

### 2. Functions:

* `take_arguements()`: Parses command-line arguments.
* `is_valid_name()`: Validates the folder name.
* `GoogleDriveClient`: Manages Google Drive interactions.
* `manage_files()`: Handles file downloads.
* `image_modifier()`: Modifies images.
* `video_writer()`: Creates a video from images.
* `audiofy()`: Adds audio to the video.
* `video_enhancer()`: Enhances the final video.

### 3. Main Workflow:

* Checks if the folder name is valid.
* If valid, it starts processing using `GoogleDriveClient` and other functions.
* If not valid, it displays an error message and instructions for valid folder names.