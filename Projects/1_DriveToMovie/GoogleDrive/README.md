## 1. [`requirements.txt`](\requirements.txt)

Contains the necessary Python modules to be installed for the project. Make 
sure to run 

```bash
pip install -r requirements.txt
``` 
to set up the environment.


## 2. [`main.py`](\main.py)

The main script for handling Google Drive operations. It performs the following tasks:

* Imports required modules and functions from various subdirectories.
* Uses `argparse` to parse command-line arguments.
* Initializes `GoogleDriveClient` and interacts with Google Drive to get 
folder IDs and files.
* Manages file downloads, modifies images, creates videos, and applies audio 
processing.
* Displays messages using cowsay to indicate the start and end of the project.

Here's a quick breakdown of the script:

### 2.1 Imports:

* Imports from `google_drive`, `file_handling`, `image_processing`, 
`video_processing`, and `audio_processing` subdirectories.
* Imports `sys` and `path` from the `os` module to manage paths.
* Uses `cowsay` for display messages.

### 2.2 Functions:

* `take_arguements()`: Parses command-line arguments.
* `is_valid_name()`: Validates the folder name.
* `GoogleDriveClient`: Manages Google Drive interactions.
* `manage_files()`: Handles file downloads.
* `image_modifier()`: Modifies images.
* `video_writer()`: Creates a video from images.
* `audiofy()`: Adds audio to the video.
* `video_enhancer()`: Enhances the final video.

### 2.3 Main Workflow:

* Checks if the folder name is valid.
* If valid, it starts processing using `GoogleDriveClient` and other functions.
* If not valid, it displays an error message and instructions for valid folder names.


## 3. `credentials` 

**Not uploaded on here.**

This folder contains files related to authentication and authorization for 
accessing Google Drive API:

### 3.1 `credentials.json`

* **Description**: This file typically contains OAuth 2.0 client ID and client 
secret information required for authenticating and authorizing access to Google APIs.

* **Usage**: It is used to obtain an authorization token for accessing the 
Google Drive API. This file should be kept secure and not shared publicly.

### 3.2 `token.json`

* **Description**: This file usually contains the OAuth 2.0 access and refresh 
tokens obtained after a successful authentication flow.

* **Usage**: It is used to access Google Drive API on behalf of the user. If the 
access token expires, the refresh token can be used to obtain a new access token 
without requiring the user to re-authenticate.

### 3.3 Summary

The `credentials` folder is crucial for managing authentication with Google 
Drive API. It should be handled securely to protect sensitive information.


## 4. [`google_drive`](./google_drive)

### 4.1 `GoogleDriveClient.py`

This file contains a class for interacting with the Google Drive API and several 
utility functions:

#### 4.1.1 `GoogleDriveClient` Class:

* **Purpose**: Provides methods to interact with Google Drive, including 
authentication and file retrieval.

* **Attributes**:
	
	* `SCOPES`: List of required Google Drive API scopes.
	* `token_filename`: Filename for storing user tokens.
	* `creds_filename`: Filename for API credentials.
	* `creds`: Google OAuth2 credentials object.
	* `service`: Google Drive API service object.

* **Methods**:
	
	* `__init__()`: Initializes the class, sets up API credentials and service.
	* `token_generator()`: Manages Google OAuth2 tokens, generates or loads 
	                       tokens, and handles token refresh.
	* `get_folder_id()`: Retrieves folder IDs for a given folder name.
	* `get_files_from_folder()`: Retrieves files from specified Google Drive 
	                             folders based on their IDs and extensions.
	* `is_valid_name()` Function:
		* **Purpose**: Checks if a file or folder name is valid for Windows OS.
		* **Arguments**:
			* `fname: str`: The file or folder name to check.
		
		* **Returns**: True if the name is valid, False otherwise.
		* **Notes**: Validates name length, checks for prohibited characters, 
		             and reserved names.
	* `take_arguements()` Function:
		* **Purpose**: Parses command-line arguments for the script.
		* **Arguments**:
			* `-t, --token_filename`: User token file (default: token.json).
			* `-c, --creds_filename`: User credential file (default: credentials.json).
			* `-f, --folder_name`: Name of the Google Drive folder to search for.
			* `-d, --duration_video_sec`: Duration of the desired video or audio 
			                              in seconds.
			* `-b, --bitrate`: Bitrate of the video enhancer (default: 15000k).
			* `-e, --extensions`: List of MIME types/extensions of the desired 
			                      files.
		
		* **Returns**: `argparse.Namespace` A Namespace object containing the 
		               parsed arguments.


## 5. [`file_handling`](./file_handling)

This folder contains Python files for managing file downloads and handling 
file creation times. Here’s a detailed breakdown of each file:

### 5.1 `FileDownloader.py`

This script is responsible for downloading files from Google Drive and saving 
them locally. It has following functions:

#### 5.1.1 `manage_files()`

* **Purpose**: Manages the file download process. It checks for the existence of 
the download folder, creates it if necessary, splits the file list into chunks, 
and downloads the files concurrently using a ThreadPoolExecutor.
* **Arguments**:
	* `folder_name (str)`: The name of the folder where files will be downloaded.
	* `files (List[Dict])`: A list of dictionaries, where each dictionary 
	                        contains information about a file to be downloaded, 
	                        including its 'id' and 'mimeType'.
	* `creds (google.auth.credentials.Credentials)`: The Google Drive API 
	                                                 credentials.
	* `chunk_size (int)`: The number of files per chunk to be processed by each 
                          service instance. Defaults to 500.
		
* **Returns**: `str` The path to the folder where files have been downloaded.

#### 5.1.2 `chunk_list()`

* **Purpose**: Splits a list of dictionaries into chunks of a specified size.
* **Arguments**:
	* `files (List[Dict])`: List of dicts containing information of the files.
	* `chunk_size (int)`: The size of each chunk. Defaults to 500.
		
* **Returns**: `Generator[List[Dict], None, None]` A generator yielding lists 
               of chunks.

#### 5.1.3 `download_file()`

* **Purpose**: Downloads a file from Google Drive and saves it to the local folder.
* **Arguments**:
	* `service (googleapiclient.discovery.Resource)`: The Google Drive API 
	                                                  service instance.
	* `fid (str)`: The ID of the file to download.
	* `fname (str)`: The name of the file.
	* `fext (str)`: The extension of the file.
	* `downloading_path (str)`: The folder to save the downloaded file.
		
* **Returns**: `None`


## 6. [`image_processing`](./image_processing)

### 6.1 `ImageHandler.py`

This file contains functions related to processing and modifying images:

#### 6.1.1 `extract_date()`:

* **Purpose**: Extracts a date from a filename formatted as "sometext_YYYY-MM-DD HH_MM_SS.ext".
* **Arguments**:
	* `filename`: The filename string to extract the date from.

* **Returns**: A datetime object representing the extracted date, or None if no date is found.
* **Notes**: Uses regular expressions to search for and convert the date in the filename to a datetime object.

#### 6.1.2 `image_modifier()`:

* **Purpose**: Modifies images in a specified directory by sorting them based on the date in their filenames and saving the altered images in a new directory.
* **Arguments**:
	* `downloading_path`: The path to the directory containing the images to be modified.

* **Returns**: The path to the directory containing the modified images.
* **Notes**: Creates a new directory for modified images if it does not already exist. Images are sorted by date and then altered (resized, padded, and desaturated) using the `image_alteration()` function.

#### 6.1.3 `image_alteration()`:

* **Purpose**: Alters an image by resizing, padding, and desaturating it.
* **Arguments**:
	* `fname`: The path to the image file to be altered.
	* `counter`: The current file counter used for desaturation calculation.
	* `total_files`: The total number of files used for desaturation calculation.
	* `max_h`: The maximum height for the resized image (default is 1080).
	* `max_w`: The maximum width for the resized image (default is 1920).

* **Returns**: A NumPy array representing the altered image.
* **Notes**: Handles both standard and HEIC image formats. Resizes the image to fit within specified dimensions, adds padding, and applies desaturation based on the position of the image in the list.


## 7. [`video_processing`](./video_processing)

### 7.1 `VideoWriter.py`

This file contains two functions related to video processing:

#### 7.1.1 `video_writer()`:

* **Purpose**: Creates a video file from images located in a specified folder using OpenCV.
* **Arguments**:
	* `download_folder_name`: The name of the folder containing image files.
	* `duration`: Duration of the video in seconds, used to calculate the frames per second (fps).
	* `vid_name`: Name of the output video file (default is "video.mp4").
	* `max_h`: Maximum height of the images (default is 1080).
	* `max_w`: Maximum width of the images (default is 1920).
	* `codec`: Codec for video compression (default is 'mp4v').

* **Returns**: Path where the video is saved.
* **Notes**: Handles creation of a video file from images, ensuring the images are sorted and added to the video. If the directory for saving the video does not exist, it is created. The video is written with specified codec and dimensions.

#### 7.1.2 `video_enhancer()`:

* **Purpose**: Enhances the video by adding padding to maintain a specified aspect ratio and setting a specific bitrate using FFmpeg.
* **Arguments**:
	* `result_path`: Path to the input video file.
	* `bitrate`: Target video bitrate (default is "15000k").
	* `aspect_ratio`: Target aspect ratio for the output video (default is 1920).

* **Returns**: Path to the enhanced video file.
* **Notes**: Uses FFmpeg to adjust the video’s aspect ratio and bitrate. The command includes padding to fit the aspect ratio and setting the specified bitrate. Handles errors in the FFmpeg command execution.

