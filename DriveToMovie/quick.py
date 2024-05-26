from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from os import path, listdir, mkdir
from io import BytesIO
from googleapiclient.http import MediaIoBaseDownload
from cv2 import cv2, imdecode
import numpy as np

class DriveToMovie:
    
    """
    A class to interact with Google Drive API.

    Attributes:
    - SCOPES (list): The scopes required for Google Drive API access.
    - token_filename (str): The filename for storing user tokens.
    - creds_filename (str): The filename for API credentials.
    - creds (Credentials): The Google OAuth2 credentials object.
    - service: The Google Drive API service object.
    """

    def __init__(self, ran):
        
        """
        Initializes DriveToMovie class by setting up API credentials and service.
        """
        # Scope required for Google Drive API access
        self.SCOPES = ['https://www.googleapis.com/auth/drive']

        # user token file
        self.token_filename = 'token.json'
        
        # API credentials
        self.creds_filename = 'credentials.json'

        if ran == 0:
          # Token generator
          self.creds = self.token_generator(self.token_filename, self.creds_filename)

          # Initiate service of Google Drive
          self.service = build('drive', 'v3', credentials=self.creds)


    def token_generator(self, token_filename, creds_filename):
        
        """
        Generates and manages Google OAuth2 tokens.

        Args:
        - token_filename (str): The filename for storing user tokens.
        - creds_filename (str): The filename for API credentials.

        Returns:
        - Credentials: The generated or loaded Google OAuth2 credentials object.
        """

        # Initialize creds to None
        creds = None

        # Check whether token for user already exists or not
        ## If exists use the existing token
        if path.exists(token_filename):
            
            print("Existing Token File found")

            ### Load the user token
            creds = Credentials.from_authorized_user_file(token_filename, self.SCOPES)

            ### Return the credentials/token
            return creds

        ## If user token doesn't exist/or isn't valid
        if not creds or not creds.valid:

            ### Check the validity of the user token, refresh if expired
            if creds and creds.expired and creds.refresh_token:
                print("Refreshing the token")
                creds.refresh(Request())

            ### If not exists then create a new user token and save it for future use
            else:
                print("Token File doesn't exist, building a new one")
                flow = InstalledAppFlow.from_client_secrets_file(creds_filename, self.SCOPES)
                creds = flow.run_local_server(port=0)

            ### Saving the user token
            print("Saving the token file", token_filename)
            with open(token_filename, 'w') as token:
                token.write(creds.to_json())

            ### Return the credentials
            return creds

    def get_folder_id(self, folder_name):
        
        """
        Retrieves the folder IDs for a given folder name.

        Args:
        - folder_name (str): The name of the folder to search for.

        Returns:
        - list: A list of folder IDs corresponding to the provided folder name.
        """
        
        # Initialise folder_ids
        folder_ids = []

        # Try block
        try:

            ## Get the list of folders from the drive with folder_name, define mimeType for
            ## filtering
            print(f'Searching for folders with name - {folder_name}...')
            response = self.service.files().list(
                q = f"name = '{folder_name}' and \
                      mimeType = 'application/vnd.google-apps.folder'",
                spaces = 'drive',
                fields = 'nextPageToken, files(id, name)',
                pageToken = None
            ).execute()
            
            ## Using get method to get the files attribute from the resonse generator
            items = response.get('files', [])

            ## Check if files have been found or not, if any
            if not items:
                print(f"No folders with {folder_name} found in the drive.")
                return None
            else:
                ### If folders found, print their name and IDs
                print("The following folder(s) have been found:\n")
                print("Folder Name \t\t Folder ID")
                
                ### Iterate through items 
                for item in items:

                    #### Print folder info
                    print(f"{item['name']} \t\t ({item['id']})")
                    
                    #### Appending to the folder_id list
                    folder_ids.append(item.get('id'))
                
                return folder_ids

        
        except HttpError as error:
            print(f"An error occurred: {error}")

    def get_files_from_folder(self, folder_id, extensions):
        """
        Retrieves files from a specified Google Drive folder.

        Args:
        - folder_id (str): The ID of the Google Drive folder.
        - extensions (list): List of extensions of the desired file

        Returns:
        - list: A list of files in the specified folder.
        """

        # Initialize page_token, Can be used for pagination
        page_token = None

        # List of files
        files = []

        # Looping through the service response until there are no files left
        while True:

            # Display the message 
            print(f"Searching for image and video files in the folder - {folder_id}...")
            
            # Executing service request query
            response = self.service.files().list(
                q = "'{}' in parents and \
                     not name contains 'raw' and \
                     mimeType in '{','.join(extensions)}'".format(folder_id),
                pageSize = 1000,
                fields = 'nextPageToken, files(id, name, mimeType, createdTime, modifiedTime, parents)',
                pageToken = page_token
            ).execute()

            # Setting up page_token for the next page
            page_token = response.get('nextPageToken', None)

            # Attaching files to the list
            files.extend(response.get('files', []))

            # If no pages left, break
            if not page_token:
                break
        
        # Returning the files
        return files

    def sort_files(self, files):

      """
        Sorting the list of files.

        Args:
        - files (list): List of the files

        Returns:
        - list: A list of files in the sorted order based on createdTime.
        """

      # Sorting files based on their createdTime
      sorted_files = sorted(files, key=lambda d: d['createdTime'])

      # Returning the sorted files
      return sorted_files

    def manage_files(self, download_folder_name, sorted_files):

      # Check if folder exists or not, if not create a new one
      if not path.exists(download_folder_name):
        mkdir(download_folder_name)

      # Iterate through the list of file_id's
      for index in range(0, len(sorted_files)):

        # Print the file count
        print(f"File {index + 1} is being downloaded.")
        
        # Download the file
        request = self.service.files().get_media(fileId=sorted_files[index]['id'])
        fh = BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        
        # Status Bar (Just in case for a big file)
        while done is False:
            status, done = downloader.next_chunk()

        # Retrieve the extension of the file - it could be png, jpeg, jpg etc
        extension = sorted_files[index]['mimeType'].split('/')[1]

        # Save the file to the local folder with the right extension
        with open(f"{download_folder_name}/{index + 1}.{extension}", 'wb') as f:
            f.write(fh.getvalue())

        
        # If we want to read all the dimensions, take mean and then save the file with
          # mean of the dimensions.  
        # img = cv2.imdecode(np.frombuffer(fh.getbuffer(), np.uint8), 1)
        # print(img.shape)

        # Print Index - Number of files
        print(f"File {index + 1}.{extension} has been saved.\n")

      # Final message before function terminates
      print(f"Total of {index} files saved")

      # Change return value                                           -- TODO
      return download_folder_name

    def image_loader(self, download_folder_name):
      """
      Loads images from a specified folder and returns a list of images and their dimensions.

      Args:
          download_folder_name (str): The path to the folder containing the images to load.

      Returns:
          tuple: A tuple containing two elements:
              - images (list): A list of loaded images(NdArray).
              - image_dimensions (list): A list of tuples, where each tuple contains the dimensions 
                (height, width, channel) of the corresponding image.
      """

      # Initialize lists to store images and their dimensions
      images, image_dimensions = [], []

      # Iterate over each file in the specified folder
      for filename in listdir(download_folder_name):
          
          # Print the current filename
          #print(filename)
          
          # Load the image from the file
          img = cv2.imread(path.join(download_folder_name, filename))
          
          # Check if the image was loaded successfully
          if img is not None:

              # Converting grayscale images into RGB
              if len(img.shape) == 2:
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

              # Append the image to the images list
              images.append(img)
              
              # Append the image dimensions (height, width, channel) to the image_dimensions list
              image_dimensions.append(img.shape)
      
      # Return the list of images and their dimensions
      return images, image_dimensions

    def manage_images(self, image, dims):


def main():
    """
    Main function to demonstrate DriveToMovie class usage.
    """
    download_folder_name = 'downloaded_files'
    ran = 0
    files = []

    # Check if we have already ran the program before and 
    # folder called downloaded_files exists or not
    if not path.exists(download_folder_name):

      # Display the message
      print(f"Folder {download_folder_name} doesn't exist. The files haven't been downloaded.\n\n")

      # Initiate the Class
      print("Initiating Connection to the Google Drive...")
      dtn = DriveToMovie(ran)
      print("Connection to the Google Drive has been established.")

      # Take user input here for which folder to access from the drive          TODO
      folder_name = 'Nee1'
      file_extensions = [".jpeg", ".jpg", ".png", ".mp4", ".avi", ".mov"]

      # Get folder_ids for folder with folder_name from the drive
      folder_ids = dtn.get_folder_id(folder_name)

      # Iterate through folder_ids of interest, adding them to the list
      for fold_id in folder_ids:
        files.extend(dtn.get_files_from_folder(fold_id, file_extensions))

      # Sort the files based on metadata of the file : createdTime
      sorted_files = dtn.sort_files(files)

      # After sorting, save the files in the desired folder locally
      dtn.manage_files(download_folder_name, sorted_files)

    else:
      # Display the msg
      print(f"\nFolder {download_folder_name} exists. The files have already been downloaded.\n")

      # Set ran to 1
      ran = 1

      # Initiate the Class
      dtn = DriveToMovie(ran)

      # Loading the downloaded files and their dimensions
      images, image_dim = dtn.image_loader(download_folder_name)



    
if __name__ == "__main__":
    main()
