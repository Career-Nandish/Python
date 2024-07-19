## 1. [GoogleDrive](./GoogleDrive)

GoogleDrive does

* Looks for the specified folder from the drive
* List all the desired files(here images) from the specified folder
* Downloads all the desired files on the local machine.
* Performs image alterations on the images.
* Using all the images created a video in chronological order.
* Appends audio to the created video file.
* Modifies video(with audio) to make it compatible for social media upload.

### Directory Structure

```bash
GoogleDrive
    │   main.py
    │   requirements.txt
    │
    ├───audio_processing
    │       Audiofy.py
    │
    ├───credentials
    │       credentials.json
    │       token.json
    │
    ├───file_handling
    │       FileDownloader.py
    │       FilesCreatedTime.py
    │
    ├───google_drive
    │       GoogleDriveClient.py
    │
    ├───image_processing
    │       ImageHandler.py
    │
    ├───miscellaneous
    │       unused.py
    │
    └───video_processing
            VideoWriter.py
```

## 2. [Instagram](./Instagram)

Instagram does

* Downloads images/videos from the specific highlight name
* Modifies the downloaded images and videos
* Uploads the downloded images to the drive(in a specific folder)

```bash
Instagram
    │   main.py
    │   requirements.txt
    │
    ├───credentials
    │       credentials.json
    │       password.txt
    │       token.json
    │
    ├───drive
    │       files_to_drive.py
    │
    ├───insta
    │       insta.py
    │
    ├───metadata
    │       metadata.json
    │
    └───miscellaneous
            video_names.txt
```


## 3. [gitignore](/.gitignore)

Tells git to ignore certain files and folders. 