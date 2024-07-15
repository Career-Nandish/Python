import sys
from os import path, listdir
from dateutil import parser
import datetime
from googleapiclient.http import MediaFileUpload

# Add the directory to sys.path
sys.path.append(path.abspath("..\\GoogleDrive\\google_drive"))

# Import the module
from GoogleDriveClient import GoogleDriveClient


def upload_images(dtm, folder_ids, images_dir):
    """
    Uploads images to a Google Drive folder.

    Args:
        folder_id: ID of the Google Drive folder.
        image_paths: List of paths to the images to upload.
    """
    count = 0
    for image in listdir(images_dir):
        count += 1
        parsed_date = parser.parse(image, fuzzy=True)
        file_metadata = {
            "name": image.split(".")[0],  
            "parents": folder_ids,
            "createdTime": parsed_date.strftime("%Y-%m-%dT%H:%M:%S") + "Z"
        }

        media = MediaFileUpload(path.join(images_dir,image), 
            mimetype=f"image/{image.split('.')[1]}")
        file = dtm.service.files().create(body=file_metadata, 
           media_body=media, fields="id").execute()
        
        print(f"File ID: {file.get('id')}")
    print(f"Total of {count} files saved.")

def main():
    dtm = DriveToMovie()
    # Get folder_ids for folder with folder_name from the drive
    folder_ids = dtm.get_folder_id("Nee")
    upload_images(dtm, folder_ids, path.join("highlights", "THE ONE"))

if __name__ == "__main__":
    main()