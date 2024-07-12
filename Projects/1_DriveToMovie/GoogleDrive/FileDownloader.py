from os import path, mkdir, makedirs
from io import BytesIO
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from concurrent.futures import ThreadPoolExecutor
from GoogleDriveClient import GoogleDriveClient
from FilesCreatedTime import get_actual_createdTime


def chunk_list(files, chunk_size):
    """
    Splits a list(of dicts) into chunks of a specified size.

    Args:
        files (list): The list(of dicts) to split.
        chunk_size (int): The size of each chunk.

    Returns:
        list: A list of chunks.
    """
    for i in range(0, len(files), chunk_size):
        yield files[i:i + chunk_size]

def manage_files(folder_name, files, creds, chunk_size=500):
    
    """
    Manages the download and local storage of files from Google Drive.

    This function checks if the specified download folder exists, creates 
    it if it doesn't, and then downloads files from Google Drive based on 
    the provided files list. Each file is saved with an appropriate extension 
    derived from its MIME type.

    Args:
        folder_name (str): The name of the drive folder.
        sorted_files (list): A list of dictionaries, where each dictionary 
                             contains information about a file to be downloaded, 
                            including its 'id' and 'mimeType'.
        chunk_size (int): The number of files per chunk to be processed by each service instance.

    Returns:
        str: The path to the folder where files have been downloaded.
    """

    # Check if folder exists or not, if not create a new one
    downloading_path = f"downloaded_folder/{folder_name}"
    if not path.exists("downloaded_folder"):
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
            print("\nWait for all futures to complete\n")
            future.result()

    # Final message before function terminates
    print(f"Total of {len(files)} files saved to {downloading_path}")

    # Return the download folder name
    return downloading_path


def download_file(service, fid, fname, fext, downloading_path):
    
    """
    Downloads a file from Google Drive.

    Args:
    - service (googleapiclient.discovery.Resource): The Google Drive API service instance.
    - file_id (str): The ID of the file to download.
    - index (int): The index of the file in the list.
    - extension (str): The extension of the file.
    - download_folder_name (str): The folder to save the downloaded file.

    Returns:
    - str: The path to the downloaded file.
    """
    # Print the file count
    print(f"File - {fid}_{fname}.{fext} is being downloaded.")

    # Download the file
    try:
        request = service.files().get_media(fileId=fid)
        fh = BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False

        # Status Bar (Just in case for a big file)
        while not done:
            status, done = downloader.next_chunk()

        # Annoying iphone, change your camera setting guys please.
            ## Under Settings > Camera > Formats, click on Most Compatible.
        if fext == "heif":
            fext = "heic"
        
        # Save the file to the local folder with the right extension
        ## fname was derived from createdTime and some files have
        ## save createdTimes so appending fileid will make the names
        ## Unique and won't overwrite the files.
        file_path = f"{downloading_path}/{fid}_{fname}.{fext}"
        with open(file_path, 'wb') as f:
            f.write(fh.getvalue())

    except HttpError as error:
        print(f"\n\n**** AN ERROR HAS OCCURRED: {error} ****")
        raise

    except Exception as error:
        print(f"\n\n**** AN UNEXPECTED ERROR OCCURRED: {error} ****")
        raise

    # Print Index - Number of files
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

if __name__ == '__main__':
    main()