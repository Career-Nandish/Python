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
    │   requirements.txt
    │   main.py
    │
    ├───credentials
    │       credentials.json
    │       token.json
    │
    ├───resources   
    │       │
    │       │
    │       ├───audio
    │       │       audio.mp3
    │       │
    │       ├───video
    │       │       video.mp4
    │       │
    │       ├───final
    │       │       final.mp4
    │       │       enhanced_final.mp4
    │       │
    │       └──downloaded_folder
    │                  │
    │                  │
    │                  ├───DriveFolderName
    │                  │       image1.jpg
    │                  │       image2.jpg
    │                  │           .
    │                  │           .
    │                  │
    │                  └───modified_DriveFolderName
    │                          1.jpg
    │                          2.jpg
    │                            .
    │                            .
    │
    ├───google_drive
    │       GoogleDriveClient.py
    │
    ├───file_handling
    │       FileDownloader.py
    │       FilesCreatedTime.py
    │
    ├───image_processing
    │       ImageHandler.py
    │
    ├───video_processing
    │       VideoWriter.py
    │
    ├───audio_processing
    │       Audiofy.py
    │
    └───miscellaneous
            notes.txt
            unused.py
    
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
    ├───highlights
    │       │
    │       └──highlight_name
    │              image1.jpg
    │              image2.jpg
    │                  .
    │                  .
    │
    └───miscellaneous
            video_names.txt
```

## 3. [Environment](./environment.yml)

Can be used to recreate the environment. 

```bash
conda env_name create -f environment.yml
```

## 4. [gitignore](./.gitignore)

Tells git to ignore certain files and folders. 