## 1. [`requirements.txt`](\requirements.txt)

Contains the necessary Python modules to be installed for the project. Make 
sure to run 

```bash
pip install -r requirements.txt
``` 
to set up the environment.


## 2. `credentials` 

**Not uploaded on here.**

This folder contains files related to authentication and authorization for 
accessing Google Drive API:

### 2.1 `credentials.json`

* **Description**: This file typically contains OAuth 2.0 client ID and client 
secret information required for authenticating and authorizing access to Google APIs.

* **Usage**: It is used to obtain an authorization token for accessing the 
Google Drive API. This file should be kept secure and not shared publicly.

### 2.2 `token.json`

* **Description**: This file usually contains the OAuth 2.0 access and refresh 
tokens obtained after a successful authentication flow.

* **Usage**: It is used to access Google Drive API on behalf of the user. If the 
access token expires, the refresh token can be used to obtain a new access token 
without requiring the user to re-authenticate.


## 3. `main.py`

This file is the main script that orchestrates various functionalities of the 
project. It interacts with Instagram to download highlights and then uploads the 
processed images to Google Drive.

### 3.1 Imports

* **Standard Libraries**: sys, pathlib.Path, argparse
* **Custom Modules**:
	* From [`insta`](./insta) folder: `load_credentials`, `load_profile`, 
	                                  `download_highlights`, `remove_unnecessary_files`, 
	                                  `get_same_file_names`, `extract_images_from_videos`
	* From [`drive`](./drive) folder: `upload_images`
	* From [`GoogleDrive`](../GoogleDrive/google_drive) `GoogleDriveClient`

### 3.2 Functions

#### 3.2.1 `take_arguements()`

Purpose: Parses command-line arguments using ArgumentParser.
Returns: A Namespace object with parsed arguments.
Arguments:
--highlight_name: Name of the Instagram highlight to download.
--gdrive_folder: Name of the Google Drive folder to save images/videos.
--dir_name: Directory to save images/videos from highlights (default: "highlights").
--meta_dir: Directory to save metadata (default: "metadata").
--token_filename: User token file for Google Drive (default: "token.json").
--creds_filename: User credentials file for Google Drive (default: "credentials.json").
main():

Purpose: Main workflow of the script, performing Instagram data handling and Google Drive uploads.
Steps:
Instagram Handling:
Check if the desired highlight directory exists.
Load Instagram credentials and profile.
Download the desired highlight.
Remove unnecessary files.
Find video names and extract images from videos.
Google Drive Handling:
Initialize GoogleDriveClient with provided token and credentials.
Get folder IDs from Google Drive.
Upload processed images to Google Drive.
Execution
Entry Point: if __name__ == '__main__': main()
The main.py file effectively coordinates between downloading Instagram highlights, processing them, and uploading results to Google Drive based on the user's command-line input.


## 4. [`drive`](./drive)

This folder contains the file(s) which interacts with Google Drive. The files are:

### 4.1 `files_to_drive.py`

This script uploads images from a specified directory to Google Drive folders. The
defined functions are as follows:

#### 4.1.1 `upload_images()`