from os import path, mkdir, makedirs
from io import BytesIO
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from google.auth.credentials import Credentials
from googleapiclient.discovery import Resource
from concurrent.futures import ThreadPoolExecutor
from GoogleDriveClient import GoogleDriveClient
from FilesCreatedTime import get_actual_createdTime
from typing import List, Generator, Dict
from sys import exit


def chunk_list(files: List[Dict], 
    chunk_size: int) -> Generator[List[Dict], None, None]:
    
    """
    Splits a list (of dicts) into chunks of a specified size.

    Args:
        files (list): The list (of dicts) to split.
        chunk_size (int): The size of each chunk.

    Returns:
        generator: A generator yielding lists of chunks.
    """
    for i in range(0, len(files), chunk_size):
        yield files[i:i + chunk_size]


def manage_files(folder_name: str, files: List[Dict], creds: Credentials, 
    chunk_size: int = 500) -> str:
    
    """
    Manages the download and local storage of files from Google Drive.

    This function checks if the specified download folder exists, creates 
    it if it doesn't, and then downloads files from Google Drive based on 
    the provided files list. Each file is saved with an appropriate extension 
    derived from its MIME type.

    Args:
        folder_name (str): The name of the folder where files will be downloaded.
        files (list): A list of dictionaries, where each dictionary contains 
                      information about a file to be downloaded, including its 
                      'id' and 'mimeType'.
        creds (google.auth.credentials.Credentials): The Google Drive API credentials.
        chunk_size (int): The number of files per chunk to be processed by each 
                          service instance.

    Returns:
        str: The path to the folder where files have been downloaded.
    """
    
    # Create the download folder if it doesn't exist
    downloading_path = path.join("downloaded_folder", folder_name)
    if not path.exists(downloading_path):
        makedirs(downloading_path)
    
    # Split the list of files into chunks
    file_chunks = list(chunk_list(files, chunk_size))

    # Create a ThreadPoolExecutor to download files concurrently
    with ThreadPoolExecutor(max_workers=len(file_chunks)) as executor:
        futures = []
        for file_chunk in file_chunks:
            for file in file_chunk:
                service = build("drive", "v3", credentials=creds)
                fid = file["id"]
                fname = get_actual_createdTime(file)
                fext = file["mimeType"].split("/")[1]
                futures.append(executor.submit(download_file, service, fid, 
                    fname, fext, downloading_path))

        # Wait for all futures to complete
        for future in futures:
            future.result()

    # Final message before function terminates
    print(f"Total of {len(files)} files saved to {downloading_path}")

    # Return the download folder path
    return downloading_path


def download_file(service: Resource, fid: str, fname: str, fext: str, 
    downloading_path: str) -> None:
    
    """
    Downloads a file from Google Drive.

    Args:
        service (googleapiclient.discovery.Resource): The Google Drive API 
                                                       service instance.
        fid (str): The ID of the file to download.
        fname (str): The name of the file.
        fext (str): The extension of the file.
        downloading_path (str): The folder to save the downloaded file.

    Returns:
        None
    """
    
    # Print the file being downloaded
    print(f"File - {fid}_{fname}.{fext} is being downloaded.")

    # Download the file
    try:
        request = service.files().get_media(fileId=fid)
        fh = BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False

        # Download file in chunks
        while not done:
            status, done = downloader.next_chunk()

        # Adjust extension for HEIF files
        if fext == "heif":
            fext = "heic"
        
        # Generate the unique file path
        file_path = path.join(downloading_path, f"{fid}_{fname}.{fext}")
        with open(file_path, 'wb') as f:
            f.write(fh.getvalue())

    except HttpError as error:
        print(f"\n\n**** AN ERROR HAS OCCURRED: {error} ****")
        raise

    except Exception as error:
        print(f"\n\n**** AN UNEXPECTED ERROR OCCURRED: {error} ****")
        raise

    # Print success message
    print(f"File {fid}_{fname}.{fext} has been saved.\n")


def main():
    
    # Hardcoding values, so don't have to run the entire thing again
    token_filename = "token.json"
    creds_filename = "credentials.json"
    folder_name = "Test"
    extensions = ['image/jpeg', 'image/png', 'image/jpg', 'image/heic', 'image/heif']
    

    googledriveclient = GoogleDriveClient(token_filename, creds_filename)
    folder_ids = googledriveclient.get_folder_id(folder_name)
    files = googledriveclient.get_files_from_folder(folder_ids, extensions)
    print(files)
    downloading_path = manage_files(folder_name, files, googledriveclient.creds)
    print(downloading_path)

if __name__ == '__main__':
    main()