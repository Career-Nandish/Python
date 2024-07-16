import sys
from os import path, listdir
from dateutil import parser
from typing import List, Dict
from googleapiclient.http import MediaFileUpload


def upload_images(dtm, folder_ids: List[str], images_dir: str) -> None:
    
    """
    Uploads images to a Google Drive folder with specific name
    from images_dir.

    Args:
        dtm (googleapiclient.discovery.Resource): Authenticated Drive 
                                                  service resource.
        folder_ids (List[str]): List of folder IDs to upload images to.
        images_dir (str): Directory path containing the images to upload.

    Returns:
    - None
    """
    
    print("\n==== Uploading images to the Google Drive Folder ====\n")
    try:
        
        for index, image in enumerate(listdir(images_dir)):

            # Parse image file name to extract created date
            parsed_date = parser.parse(image, fuzzy=True)
            
            # Define metadata for the file
            file_metadata = {
                # Use filename without extension as name
                "name": image.split(".")[0],
                # Assign folder IDs as parents
                "parents": folder_ids,
                # Format created time
                "createdTime": parsed_date.strftime("%Y-%m-%dT%H:%M:%S") + "Z"  
            }

            # Prepare media upload
            media = MediaFileUpload(path.join(images_dir, image), 
                                    mimetype=f"image/{image.split('.')[1]}")
            
            # Upload the file to Google Drive
            file = dtm.service.files().create(body=file_metadata, 
                media_body=media, fields="id").execute()
            
            # Print file ID on successful upload
            print(f"File ID: {file.get('id')} uploaded")

        # Print total number of files uploaded
        print(f"Total of {index + 1} files saved.")
        print("\n==== DONE Uploading images to the Google Drive Folder ====\n")

    except Exception as error:
        print(f"""\n\n**** AN UNKNOWN ERROR HAS OCCURRED in 
            upload_images : {error} ****\n\n""")