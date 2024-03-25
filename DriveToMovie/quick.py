from os import path
import io
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload




class DriveToMovie:


  def __init__(self):

    # If modifying these scopes, delete the file token.json.
    self.SCOPES = ["https://www.googleapis.com/auth/drive"]
    # API Token file and API credentials file
    self.token_filename = "token.json" 
    # API Credentials file
    self.creds_filename = "credentials.json" 
    # Loading creds
    self.creds = self.token_generator(self.token_filename, self.creds_filename)


  def token_generator(self, token_filename, creds_filename):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if path.exists(token_filename):
      creds = Credentials.from_authorized_user_file(token_filename, self.SCOPES)
      return creds
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
            creds_filename, self.SCOPES
        )
        creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open(token_filename, "w") as token:
        token.write(creds.to_json())
      return creds


  def get_folder_id(self, creds, folder_name):
    folder_ids, folder_names = [], []
    try:
      service = build("drive", "v3", credentials=self.creds)

      response = (
            service.files()
            .list(
              q = f"name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder'",
                spaces="drive",
                fields="nextPageToken, files(id, name)",
                pageToken=None,
            )
            .execute()
        )

      items = response.get('files', [])  
      
      if not items:
        print("No files found.")
        return folder_ids
      
      else:
        print("Folder Name \t\t Folder ID")
        for item in items:
          print(f"{item['name']} \t\t ({item['id']})")
          folder_names.append(item.get('name'))
          folder_ids.append(item.get('id'))

        return folder_ids
    
    except HttpError as error:
      # TODO(developer) - Handle errors from drive API.
      print(f"An error occurred: {error}")


def main():
  
  dtn = DriveToMovie()
  folder_ids = dtn.get_folder_id(dtn.creds, 'Nee')
  print(folder_ids)


if __name__ == "__main__":
  main()