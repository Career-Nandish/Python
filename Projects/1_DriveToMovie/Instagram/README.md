## 1. [`requirements.txt`](./requirements.txt)

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

### 2.3 `password.txt`

* **Description**: This file contains the credentials for the instagram.

* **Usage**: It is used to log into instagram's account(authentication).


## 3. [`main.py`](./main.py)

This file is the main script that orchestrates various functionalities of the 
project. It interacts with Instagram to download highlights and then uploads the 
processed images to Google Drive.

### 3.1 Imports

* **Standard Libraries**: sys, pathlib.Path, argparse
* **Custom Modules**:
	* From [`insta`](./insta) folder: From [`insta.py`](./insta/insta.py) imports
	                                  `load_credentials`, `load_profile`, 
	                                  `download_highlights`, `remove_unnecessary_files`, 
	                                  `get_same_file_names`, `extract_images_from_videos`
	* From [`drive`](./drive) folder: From [`files_to_drive.py`](./drive/files_to_drive.py) 
	                                  imports `upload_images`.
	* From [`GoogleDrive`](../GoogleDrive/google_drive) folder: From 
	      [`GoogleDriveClient.py`](../GoogleDrive/google_drive/GoogleDriveClient.py)
	      imports `GoogleDriveClient`

### 3.2 Functions

#### 3.2.1 `take_arguements()`

* **Purpose**: Parses command-line arguments using ArgumentParser.
* **Returns**: `argparse.Namespace` A Namespace object with parsed arguments.
* **Arguments**:
	`-n, --highlight_name`: Name of the Instagram highlight to download.
	`-g, --gdrive_folder`: Name of the Google Drive folder to save images/videos.
	`-d, --dir_name`: Directory to save images/videos from highlights 
	                  (default: "highlights").
	`-m, --meta_dir`: Directory to save metadata (default: "metadata").
	`-t, --token_filename`: User token file for Google Drive 
	                        (default: "token.json").
	`-c, --creds_filename`: User credentials file for Google Drive 
	                        (default: "credentials.json").


#### 3.2.2 `main()`

* **Purpose**: Main workflow of the script, performing Instagram data handling 
               and Google Drive uploads.

* **Steps**:
	* **Instagram Handling**:
		* Check if the desired highlight directory exists.
		* Load Instagram credentials and profile.
		* Download the desired highlight.
		* Remove unnecessary files.
		* Find video names and extract images from videos.
	
	* **Google Drive Handling**:
		* Initialize GoogleDriveClient with provided token and credentials.
		* Get folder IDs from Google Drive.
		* Upload processed images to Google Drive.

* **Execution**
	* **Entry Point**: if `__name__ == '__main__': main()`

The `main.py` file effectively coordinates between downloading Instagram highlights, processing them, and uploading results to Google Drive based on the user's command-line input.


## 4. [`insta`](./insta)

This folder contains files which interacts with Instagram platform. Mainly download
images from highlights(collection of stories).

### 4.1 [`insta.py`](./insta/insta.py)

This script handles various Instagram-related tasks, including loading credentials, 
downloading highlights, processing images and videos, and removing unnecessary files.
Houses following functions:

#### 4.1.1 `load_credentials()`

* **Purpose**: Loads credentials from a text file. Reads a JSON file located in 
               the "credentials" directory and extracts the username and password.

* **Arguments**: `None`

* **Returns**: `Tuple[str, str]` A tuple containing the username and password.

* **Raises**:
    * `FileNotFoundError`: If the file does not exist.
    * `json.JSONDecodeError`: If the file content is not a valid JSON.
    * `KeyError`: If the required keys ("username" and "password") are not found 
                  in the JSON file.

#### 4.1.2 `remove_emojis()`
 
* **Purpose**: Removes emojis from a given text string.

* **Arguments**:
	* `text (str)`: The input text containing emojis.
		
* **Returns**: `str` The text with emojis removed. 

* **Note**:
	* This function converts all emojis in the input text to their respective 
	text representation using `emoji.demojize`, and then removes them using 
	a regular expression. 
	* The name of the highlights could have different kinds of emojis and special
	characters, so to deal with them this sanitisation function was created.

#### 4.1.3 `load_profile()`

* **Purpose**: Loads an Instagram profile using provided credentials. Initializes 
               an Instaloader instance, logs in with the given username and password, 
               and retrieves the profile.

* **Arguments**:
	* `USERNAME (str)`: The Instagram username.
    * `PASSWORD (str)`: The Instagram password.
		
* **Returns**: `Tuple[instaloader.Instaloader, instaloader.Profile]` A tuple 
               containing the Instaloader instance and the profile.

* **Raises**:
    * `instaloader.exceptions.ConnectionException`: If there is a connection error.
    * `instaloader.exceptions.BadCredentialsException`: If the credentials are incorrect.
    * `instaloader.exceptions.TwoFactorAuthRequiredException`: If two-factor authentication 
                                                               is required.
    * `instaloader.exceptions.ProfileNotExistsException`: If the profile does not exist.

#### 4.1.4 `download_highlights()`

* **Purpose**: Downloads Instagram highlight stories and saves them to the specified 
               directory.

* **Arguments**:
	* `L (instaloader.Instaloader)`: The Instaloader instance.
    * `profile (instaloader.Profile)`: The Instagram profile instance.
    * `desired_highlight (str)`: The title of the highlight to download.
    * `save_dir (str)`: The directory where the highlight stories will be saved.
    * `metadata_dir (str)`: The directory where the metadata will be saved.
		
* **Returns**:`str` The path save_dir\desired_highlight.

* **Note**: This function iterates through the highlights of the given profile, 
            identifies the desired highlight by its title, and downloads all the 
            items (stories) in that highlight to a specified directory. Additionally, 
            it saves metadata of the downloaded items to a JSON file.


#### 4.1.5 `remove_unnecessary_files()`

* **Purpose**: Removes unnecessary files from the specified directory.

* **Arguments**:
	* `desired_dir (str)`: The directory from which unnecessary files should 
                           be removed.
		
* **Returns**: `str` The path to the directory after cleanup.

* **Note**: 
	* This function iterates through all files in the given directory and 
	deletes any file that ends with the '.xz' extension. It prints the 
	name of each file it processes and confirms when the removal is complete.
	* The `L.download_storyitem()` function download files and also
	compressed files as well, which are unwanted since removing them.

#### 4.1.6 `get_same_file_names()`

* **Purpose**: Finds and writes matching file names in a directory.

* **Arguments**:
	* `desired_dir (str)`: The directory path where to search for image and 
	                     video files.
    * `video_file (str)`: The file path where to write the list of matching 
                        video file names.
		
* **Returns**: `str` The path where .txt file with video names is written. 

* **Note**: This function searches for image files (ending with '.jpg') in the 
            specified directory, finds corresponding video files (replacing 
            '.jpg' with '.mp4'), and writes the names of these video files to 
            a specified text file.

#### 4.1.7 `extract_images_from_videos()`

* **Purpose**: Extracts random frames from video files listed in a text file and 
               saves them as images.

* **Arguments**:
	* `desired_dir (str)`: Directory path where the video files are located 
                           and where images will be saved.
    * `video_file (str)`: File path of the text file containing names of video 
                          files.
		
* **Returns**: `str` The path save_dir\desired_highlight.

* **Note**: The `L.download_storyitem()`` function download videos and their
           thumbnails(images), the latter has reduced quality so extracting
           a random frame from the video for better quality.

## 5. [`drive`](./drive)

This folder contains the file(s) which interacts with Google Drive. The files are:

### 5.1 [`files_to_drive.py`](./drive/files_to_drive.py)

This script uploads images from a specified directory to Google Drive folders. The
defined functions are as follows:

#### 5.1.1 `upload_images()`


* **Purpose**: Uploads images to a Google Drive folder with specific name
               from `images_dir`.
* **Arguments**:
	* `dtm (googleapiclient.discovery.Resource)`: Authenticated Drive service 
	                                              resource.
	* `folder_ids (List[str])`: List of folder IDs to upload images to.
	* `images_dir (str)`: Directory path containing the images to upload.
		
* **Returns**: `None`


## 6. `metadata`

**Not uploaded here**

This folder contains metadata about the files downloaded from Instagram stories. This 
information will be useful for keeping track of the details and attributes of the 
downloaded content. It looks something like following:

```json
{
    "ID": {
        "typename": "GraphStoryImage",
        "date_utc": "YYYY-MM-DD HH:MM:SS",
        "url": "<omitted>",
        "is_video": false,
        "video_url": null
    },
}
```

## `miscellanous`

**Not uploaded here**

Contains `video_names.txt`, which contains the names of the video files, uploaded on 
stories. It is a comma separated values. For example,  "vid1.mp4, vid2.mp4,..."


## 7. `highlights`

**Not uploaded here**

Contains downloaded highlights here. Has subfolder with desired highlight name.