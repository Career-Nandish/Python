import re
from argparse import ArgumentParser, Namespace
from os import path, listdir, makedirs
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from typing import List, Dict, Generator

class GoogleDriveClient:

    """
    A class to interact with Google Drive API.

    Attributes:
    - SCOPES (list): The scopes required for Google Drive API access.
    - token_filename (str): The filename for storing user tokens.
    - creds_filename (str): The filename for API credentials.
    - creds (Credentials): The Google OAuth2 credentials object.
    - service: The Google Drive API service object.

    Class variables:
    - extensions (dict) : The dictionary of desired extensions. 
    """

    def __init__(self, token_filename: str, creds_filename: str) -> None:
       
        """
        Initializes DriveToMovie class by setting up API credentials and service.
        """
        
        # Scope required for Google Drive API access
        self.SCOPES = ['https://www.googleapis.com/auth/drive']

        # user token file
        self.token_filename = token_filename

        # API credentials
        self.creds_filename = creds_filename

        # Token generator
        self.creds = self.token_generator(self.token_filename, self.creds_filename)

        # Initiate service of Google Drive
        self.service = build('drive', 'v3', credentials=self.creds)

    def token_generator(self, token_filename: str, creds_filename: str) -> Credentials:
        
        """
        Generates and manages Google OAuth2 tokens.

        Args:
        - token_filename (str): The filename for storing user tokens.
        - creds_filename (str): The filename for API credentials.

        Returns:
        - Credentials: The generated or loaded Google OAuth2 credentials object.

        Note - 1. Make sure to save your Drive API credentials(API key) to the same 
               directory and pass the name of that as creds_filename.
               2. At first, you won't have token.json, you'd need to run this code
               to generate that file. It will basically ask you to log into your google
               account and ask for other permissions. Once you have the file, the following
               code won't regenerate it unless and until the token is expired or invalid 
               or corrupted. 
        """

        # Initialize creds to None
        creds = None

        # Path to files
        token_file_path = path.join("credentials", token_filename)
        creds_file_path = path.join("credentials", creds_filename)
        
        # Check whether token for user already exists or not
        # If exists use the existing token
        if path.exists(token_file_path):

            print(f"\n==== Existing Token File - {token_file_path} found. ====")
            print(f"==== Loading the token(s) from - {token_file_path}. ====")
            # Load the user token
            creds = Credentials.from_authorized_user_file(token_file_path, 
                self.SCOPES)
            print("==== Token loaded. ====")

            # Return the credentials/token
            return creds

        # If user token doesn't exist/or isn't valid
        if not creds or not creds.valid:

            # Check the validity of the user token, refresh if expired
            if creds and creds.expired and creds.refresh_token:
                print("\n==== Refreshing the token... ====")
                creds.refresh(Request())

            # If not exists then create a new user token and save it for future
            # use
            else:
                print("\n==== Token File doesn't exist, building a new one. ====")
                flow = InstalledAppFlow.from_client_secrets_file(
                    creds_file_path, self.SCOPES)
                creds = flow.run_local_server(port=0)

            # Saving the user token
            print(f"==== Saving the token file as {token_filename}. ====")
            with open(token_file_path, 'w') as token:
                token.write(creds.to_json())

            # Return the credentials
            return creds

    def get_folder_id(self, folder_name: str) -> List[str]:
        
        """
        Retrieves the folder IDs for a given folder name.

        Args:
        - folder_name (str): The name of the folder(s) to search for.

        Returns:
        - list: A list of folder ID(s) corresponding to the provided folder name.

        Note - If you have multiple folders to look for with different names, just
               create a new function to iterate through them or modify the existing
               code.  
        """

        # Initialise folder_ids
        folder_ids = []

        # Try block
        try:

            # Get the list of folders from the drive with folder_name, define mimeType for
            # filtering
            print(f'\n==== Searching for folders with name - {folder_name}... ====')

            # Execute service request entry
            response = self.service.files().list(
                q=f"name = '{folder_name}' and \
                      mimeType = 'application/vnd.google-apps.folder'",
                spaces='drive',
                fields='nextPageToken, files(id, name)',
                pageToken=None
            ).execute()

            # Using get method to get the files attribute from the resonse
            # generator
            items = response.get("files", [])

            # Check if files have been found or not, if any
            if not items:
                print(f"==== No folders with {folder_name} found in the drive. ====")
            else:
                # If folders found, print their name and IDs
                print("The following folder(s) have been found:\n")
                print("Folder Name \t\t Folder ID")

                # Iterate through items
                for item in items:

                    # Print folder info
                    print(f"{item['name']} \t\t ({item['id']})")

                    # Appending to the folder_id list
                    folder_ids.append(item.get('id'))

        except HttpError as error:
            print(f"\n\n****AN ERROR HAS OCCURRED ****: {error}")
            raise

        except Exception as error:
            print(f"\n\n****AN UNEXPECTED ERROR OCCURRED ****: {error}")
            raise

        # Returning folder ids
        return folder_ids

    def get_files_from_folder(self, folder_ids: List[str], 
        extensions: List[str]) -> List[Dict[str, str]]:
        
        """
        Retrieves files from specified Google Drive folders.

        Args:
        - folder_ids (list): List of folder IDs in Google Drive.
        - extensions (list): List of file extensions to search for.

        Returns:
        - list: A list of files in the specified folders.
        """
        
        # Initialize files list
        files = []

        try:
            # Loop through each folder ID
            for folder_id in folder_ids:
                
                # Initialize page_token for pagination
                page_token = None  

                while True:
                    # Combine mimeType queries with 'or'
                    mime_query_string = " or ".join(f"mimeType='{e}'" for e in extensions)

                    # Display search message
                    print(f"\n==== Searching for image and video files in the folder - {folder_id}... ====")

                    # Execute service request query
                    response = self.service.files().list(
                        q=f"('{folder_id}' in parents) and \
                            (not name contains 'raw') and \
                            ({mime_query_string})",
                        pageSize=100,
                        fields='nextPageToken, files(id, name, mimeType, createdTime, \
                                modifiedTime, parents)',
                        pageToken=page_token
                    ).execute()

                    # Extend files list with results from current page
                    files.extend(response.get('files', []))

                    # Update page_token for the next page
                    page_token = response.get('nextPageToken', None)

                    # If no more pages, break out of loop
                    if not page_token:
                        break

        except HttpError as error:
            print(f"\n\n**** AN ERROR HAS OCCURRED: {error} ****")
            raise

        except Exception as error:
            print(f"\n\n**** AN UNEXPECTED ERROR OCCURRED: {error} ****")
            raise

        # Return the list of files retrieved
        return files

def is_valid_name(fname: str) -> bool:
    
    """
    Checks if the provided file/folder name is valid for Windows OS.

    Args:
    - fname (str): The file/folder name to check.

    Returns:
    - bool: True if the file/folder name is valid, False otherwise.
    
    Notes:
    A valid file/folder name:
    - Does not contain any special characters like <>:"/\|?*
    - Does not start or end with a space
    - Does not exceed 255 characters in length
    """
    
    # Check if file name is not empty and does not exceed the character limit
    if not fname or len(fname) > 255:
        return False

    # Prohibited characters
    prohibited_chars = r'[<>:"/\\|?*]'

    if re.search(prohibited_chars, fname):
        return False

    # Reserved names
    reserved_names = [
        "CON", "PRN", "AUX", "NUL", "COM1", "LPT1", "COM2", 
        "LPT2", "COM3", "LPT3", "COM4", "LPT4", "COM5", 
        "LPT5", "COM6", "LPT6", "COM7", "LPT7", "COM8", 
        "LPT8", "COM9", "LPT9"
    ]

    # Split the file name to separate the base name and the extension
    base_name = fname.split('.')[0]

    if base_name.upper() in reserved_names:
        return False

    return True


def take_arguements() -> Namespace:
    
    """
    Parses command-line arguments for the script.

    Returns:
    - Namespace: The parsed arguments as a Namespace object.
    """
    
    # Init ArgumentParser
    parser = ArgumentParser(
        description="List files from folder IDs with given folder name on the Google Drive."
    )

    # Add arguments
    parser.add_argument(
        "-t",
        "--token_filename", 
        type=str, 
        default="token.json", 
        help="User token file."
    )
    parser.add_argument(
        "-c",
        "--creds_filename", 
        type=str, 
        default="credentials.json", 
        help="User credential file(API keys). Must be a .json File."
    )
    parser.add_argument(
        "-f",
        "--folder_name", 
        type=str,
        required=True,
        help="Name of the Google Drive Folder with desired files."
    )
    parser.add_argument(
        "-d",
        "--duration_video_sec", 
        type=int,
        required=True,
        help="Duration of the desired video(in secs)."
    )
    parser.add_argument(
        "-b",
        "--bitrate", 
        type=str,
        default="15000k",
        help="Bitrate of the video enhancer."
    )
    parser.add_argument(
        "-e",
        "--extensions",
        nargs='+',
        default=['image/jpeg', 'image/png', 'image/jpg', 'image/heic', 'image/heif'],
        help="List of MIME types/extensions of the desired files."
    )

    # Return Namespace object
    return parser.parse_args()
