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

### 2.1 Imports:

* Imports from `google_drive`, `file_handling`, `image_processing`, `video_processing`, and `audio_processing` subdirectories.
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

This folder contains files related to authentication and authorization for accessing Google Drive API:

### 3.1 `credentials.json`

* **Description**: This file typically contains OAuth 2.0 client ID and client secret information required for authenticating and authorizing access to Google APIs.

* **Usage**: It is used to obtain an authorization token for accessing the Google Drive API. This file should be kept secure and not shared publicly.

### 3.2 `token.json`

* **Description**: This file usually contains the OAuth 2.0 access and refresh tokens obtained after a successful authentication flow.

* **Usage**: It is used to access Google Drive API on behalf of the user. If the access token expires, the refresh token can be used to obtain a new access token without requiring the user to re-authenticate.

### 3.3 Summary

The `credentials` folder is crucial for managing authentication with Google Drive API. It should be handled securely to protect sensitive information.


## 4. [`google_drive`](./google_drive)


### 4.1 `GoogleDriveClient.py`

This file contains a class for interacting with the Google Drive API and several utility functions:

#### 4.1.1 `GoogleDriveClient` Class:

* **Purpose**: Provides methods to interact with Google Drive, including authentication and file retrieval.

* **Attributes**:
	
	* `SCOPES`: List of required Google Drive API scopes.
	* `token_filename`: Filename for storing user tokens.
	* `creds_filename`: Filename for API credentials.
	* `creds`: Google OAuth2 credentials object.
	* `service`: Google Drive API service object.

* **Methods**:
	
	* `__init__()`: Initializes the class, sets up API credentials and service.
	* `token_generator()`: Manages Google OAuth2 tokens, generates or loads tokens, and handles token refresh.
	* `get_folder_id()`: Retrieves folder IDs for a given folder name.
	* `get_files_from_folder()`: Retrieves files from specified Google Drive folders based on their IDs and extensions.
	* `is_valid_name()` Function:
		* **Purpose**: Checks if a file or folder name is valid for Windows OS.
		* **Arguments**:
			* `fname`: The file or folder name to check.
			* `Returns`: True if the name is valid, False otherwise.
			* Notes: Validates name length, checks for prohibited characters, and reserved names.
	* `take_arguements()` Function:
		* **Purpose**: Parses command-line arguments for the script.
		* **Returns**: A Namespace object containing the parsed arguments.
		* **Arguments**:
			* `-t, --token_filename`: User token file (default: token.json).
			* `-c, --creds_filename`: User credential file (default: credentials.json).
			* `-f, --folder_name`: Name of the Google Drive folder to search for.
			* `-d, --duration_video_sec`: Duration of the desired video or audio in seconds.
			* `-b, --bitrate`: Bitrate of the video enhancer (default: 15000k).
			* `-e, --extensions`: List of MIME types/extensions of the desired files.