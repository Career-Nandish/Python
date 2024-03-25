from os import path
import io
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive"]


def token_refresh():
  """Shows basic usage of the Drive v3 API.
  Prints the names and ids of the first 10 files the user has access to.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    return creds
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())
    return creds


def get_folder_id(creds, folder_name):
  folder_ids, folder_names = [], []
  try:
    service = build("drive", "v3", credentials=creds)

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
        folder_names.extend(item.get('name'))
        folder_ids.extend(item.get('id'))

      return folder_ids
  
  except HttpError as error:
    # TODO(developer) - Handle errors from drive API.
    print(f"An error occurred: {error}")


def main():
  
  # Get credentials
  creds = token_refresh()
  folder_ids = get_folder_id(creds, 'Nee')


if __name__ == "__main__":
  main()