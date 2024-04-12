from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from os import path
from os import mkdir
from io import BytesIO
from googleapiclient.http import MediaIoBaseDownload
from cv2 import imread


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

    def __init__(self):
        
        """
        Initializes DriveToMovie class by setting up API credentials and service.
        """

        # Scope required for Google Drive API access
        self.SCOPES = ["https://www.googleapis.com/auth/drive"]

        # user token file
        self.token_filename = "token.json"
        
        # API credentials
        self.creds_filename = "credentials.json"

        # Token generator
        self.creds = self.token_generator(self.token_filename, self.creds_filename)

        # Initiate service of Google Drive
        self.service = build("drive", "v3", credentials=self.creds)

        # Print
        print("Connection to the Google Drive has been established.")

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
            
            ### Load the user token
            creds = Credentials.from_authorized_user_file(token_filename, self.SCOPES)

            ### Return the credentials/token
            return creds

        ## If user token doesn't exist/or isn't valid
        if not creds or not creds.valid:

            ### Check the validity of the user token, refresh if expired
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())

            ### If not exists then create a new user token and save it for future use
            else:
                flow = InstalledAppFlow.from_client_secrets_file(creds_filename, self.SCOPES)
                creds = flow.run_local_server(port=0)

            ### Saving the user token
            with open(token_filename, "w") as token:
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
            print(f"Searching for folders with name - {folder_name}...")
            response = self.service.files().list(
                q = f"name = '{folder_name}' and \
                      mimeType = 'application/vnd.google-apps.folder'",
                spaces = "drive",
                fields = "nextPageToken, files(id, name)",
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

    def get_files_from_folder(self, folder_id):
        """
        Retrieves files from a specified Google Drive folder.

        Args:
        - folder_id (str): The ID of the Google Drive folder.

        Returns:
        - list: A list of files in the specified folder.
        """
        page_token = None
        files = []
        while True:
            print(f"Searching for image files in the folder - {folder_id}...")
            response = self.service.files().list(
                q = "'{}' in parents and not name contains 'raw'".format(folder_id),
                pageSize = 1000,
                fields = "nextPageToken, files(id, name, mimeType, createdTime, modifiedTime, parents)",
                pageToken = page_token
            ).execute()
            page_token = response.get('nextPageToken', None)
            files.extend(response.get('files', []))
            if not page_token:
                break
        
        return files

    def sort_files(self, files):
      sorted_files = sorted(files, key=lambda d: d['createdTime'])
      return sorted_files

    def manage_files(self, folder_name, sorted_files):

      # Check if folder exists or not, if not create a new one
      if not path.exists(folder_name):
        mkdir(folder_name)

      # Iterate through the list of file_id's
      for index in range(0, len(sorted_files)):

        # Print the file count
        print(f"Image {index + 1} is being downloaded.")
        
        # Download the file
        request = self.service.files().get_media(fileId=sorted_files[index]['id'])
        fh = BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        
        # Status Bar (Just in case for a big file)
        while done is False:
            status, done = downloader.next_chunk()

        # Retrieve the extension of the file - it could be png, jpeg, jpg etc
        extension = sorted_files[index]['mimeType'].split("/")[1]

        # Save the file to the local folder with the right extension
        with open(f"{folder_name}/{index + 1}.{extension}", 'wb') as f:
            f.write(fh.getvalue())

        # Print Index - Number of files
        print(f"File {index + 1}.{extension} has been saved.")

      return folder_name


class ImageHandler(DriveToMovie):

    def image_loader(self, folder_name):
      images = []
      for filename in listdir(folder_name):
        img = cv2.imread(path.join(folder_name,filename))
        if img is not None:
          images.append(img)
      return images

    def

def main():
    """
    Main function to demonstrate DriveToMovie class usage.
    """
    files = []
    print("Initiating Connection to the Google Drive...")
    dtn = DriveToMovie()
    folder_ids = dtn.get_folder_id(folder_name = 'Nee1')
    for fold_id in folder_ids:
      files.extend(dtn.get_files_from_folder(fold_id))
    sorted_files = dtn.sort_files(files)
    dtn.manage_files("downloaded_files", sorted_files)
    
if __name__ == "__main__":
    main()
