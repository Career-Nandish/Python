import cv2
import time
import sys
import numpy as np
from PIL import Image
from io import BytesIO
from cv2 import imdecode
from concurrent import futures
from os import path, listdir, mkdir
from pillow_heif import register_heif_opener, open_heif
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from concurrent.futures import ThreadPoolExecutor
from moviepy.editor import VideoFileClip, AudioFileClip


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

    def __init__(self, ran=0):
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
        # If exists use the existing token
        if path.exists(token_filename):

            print("Existing Token File found")

            # Load the user token
            creds = Credentials.from_authorized_user_file(
                token_filename, self.SCOPES)

            # Return the credentials/token
            return creds

        # If user token doesn't exist/or isn't valid
        if not creds or not creds.valid:

            # Check the validity of the user token, refresh if expired
            if creds and creds.expired and creds.refresh_token:
                print("Refreshing the token")
                creds.refresh(Request())

            # If not exists then create a new user token and save it for future
            # use
            else:
                print("Token File doesn't exist, building a new one")
                flow = InstalledAppFlow.from_client_secrets_file(
                    creds_filename, self.SCOPES)
                creds = flow.run_local_server(port=0)

            # Saving the user token
            print("Saving the token file", token_filename)
            with open(token_filename, 'w') as token:
                token.write(creds.to_json())

            # Return the credentials
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

            # Get the list of folders from the drive with folder_name, define mimeType for
            # filtering
            print(f'Searching for folders with name - {folder_name}...')
            response = self.service.files().list(
                q=f"name = '{folder_name}' and \
                      mimeType = 'application/vnd.google-apps.folder'",
                spaces='drive',
                fields='nextPageToken, files(id, name)',
                pageToken=None
            ).execute()

            # Using get method to get the files attribute from the resonse
            # generator
            items = response.get('files', [])

            # Check if files have been found or not, if any
            if not items:
                print(f"No folders with {folder_name} found in the drive.")
                return None
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
            print(
                f"Searching for image and video files in the folder - {folder_id}...")

            # Combine mimeType queries with 'or'
            mime_query_string = " or ".join(f"mimeType='{extensions[e]}'" for e in extensions)

            # Executing service request query
            response = self.service.files().list(
                q=f"('{folder_id}' in parents) and \
                      (not name contains 'raw') and \
                      ({mime_query_string})",
                pageSize=1000,
                fields='nextPageToken, files(id, name, mimeType, createdTime, modifiedTime, parents)',
                pageToken=page_token
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
      for i in files:print(i)

      # Sorting files based on their createdTime
      sorted_files = sorted(files, key=lambda d: d['createdTime'])

      # Returning the sorted files
      return sorted_files

    def chunk_list(self, lst, chunk_size):
        """
        Splits a list into chunks of a specified size.

        Args:
            lst (list): The list to split.
            chunk_size (int): The size of each chunk.

        Returns:
            list: A list of chunks.
        """
        for i in range(0, len(lst), chunk_size):
            yield lst[i:i + chunk_size]
    
    def manage_files(self, download_folder_name, sorted_files, chunk_size=500):
        """
        Manages the download and local storage of files from Google Drive.

        This function checks if the specified download folder exists, creates it if it doesn't, and
        then downloads files from Google Drive based on the provided sorted_files list. Each file is
        saved with an appropriate extension derived from its MIME type.

        Args:
            download_folder_name (str): The path to the folder where files will be downloaded and saved.
            sorted_files (list): A list of dictionaries, where each dictionary contains information
                                 about a file to be downloaded, including its 'id' and 'mimeType'.
            chunk_size (int): The number of files per chunk to be processed by each service instance.

        Returns:
            str: The path to the folder where files have been downloaded.
        """

        # Check if folder exists or not, if not create a new one
        if not path.exists(download_folder_name):
            mkdir(download_folder_name)

        # Split the list of files into chunks
        file_chunks = list(self.chunk_list(sorted_files, chunk_size))

        # Create a ThreadPoolExecutor to download files concurrently
        with ThreadPoolExecutor(max_workers=len(file_chunks)) as executor:
            futures = []
            for chunk_index, file_chunk in enumerate(file_chunks):
                for index, file_info in enumerate(file_chunk):
                    service = build('drive', 'v3', credentials=self.creds)
                    file_id = file_info['id']
                    extension = file_info['mimeType'].split('/')[1]
                    futures.append(executor.submit(self.download_file, service, file_id, index + chunk_index * chunk_size, extension, download_folder_name))

            # Wait for all futures to complete
            for future in futures:
                print("\nWait for all futures to complete\n")
                future.result()

        # Final message before function terminates
        print(f"Total of {len(sorted_files)} files saved")

        # Return the download folder name
        return download_folder_name

    def download_file(self, service, file_id, index, extension, download_folder_name):
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
        print(f"File {index + 1} is being downloaded.")

        # Download the file
        request = service.files().get_media(fileId=file_id)
        fh = BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False

        # Status Bar (Just in case for a big file)
        while not done:
            status, done = downloader.next_chunk()

        # Annoying iphone, change your camera setting guys please.
            ## Under Settings > Camera > Formats, click on Most Compatible.
        if extension == "heif":
            extension = "heic"
        
        # Save the file to the local folder with the right extension
        file_path = f"{download_folder_name}/{index + 1}.{extension}"
        with open(file_path, 'wb') as f:
            f.write(fh.getvalue())

        # Print Index - Number of files
        print(f"File {index + 1}.{extension} has been saved.\n")
        return file_path


    def handle_downloaded_files(self, download_folder_name, extensions):
      
      """
      unused function
      """

      # Initialize list to store dimensions
      image_dimensions = []

      # Initialize lists to store video frames and their dimensions
      video_dimensions = []

      # Iterate over each file in the specified folder
      for filename in listdir(download_folder_name):

        # Checking the type of the file
        # Image File
        if filename.lower().endswith(
            tuple([k for k, v in extensions.items() if 'image' in v])
            ):

          # Display message
          print("Image file -", filename)

          # Load the image from the file
          img = cv2.imread(path.join(download_folder_name, filename))

          # Check if the image was loaded successfully
          if img is not None:

              # Append the image dimensions (height, width) to the
              # image_dimensions list
              image_dimensions.append(img.shape[:2])

        # Video File
        elif filename.lower().endswith(tuple([k for k, v in extensions.items() if 'video' in v])):

          # Display message
          print("Video file -", filename)

          # Loading up the video
          cap = cv2.VideoCapture(path.join(download_folder_name, filename))

          # loop runs as long as the video file is successfully opened
          while cap.isOpened():

            # reads a frame from the video
            ret, frame = cap.read()

            # If frame wasn't read successfully, break
            if not ret:
              break

            # Appending frame dimentions to the list video_dimentions
            video_dimensions.append(frame.shape[:2])
            break

          # Releases the video capture object after processing all frames
          cap.release()

        # Unknown File Type
        else:
            # Display message
            print(f"## UNSUPPORTED FILE TYPE ## - {filename}")

      #with open("Output.txt", "w") as text_file:
      #  text_file.write(string)
      # Returning all necessary variables
      return image_dimensions, video_dimensions

    def largest_dimensions(self, image_dimensions, video_dimensions):

      """
        unused function
        TODO - might add video support later

      """

      # Get the maximum dimensions
      transposed_dim = list(zip(*image_dimensions))

      # Max height
      max_h = max(transposed_dim[0])

      # Max width
      max_w = max(transposed_dim[1])

      return max_h, max_w

    def calculate_mean_dimensions(self, dimensions):
      """
        unused function
        Computes the mean height and width from a list of dimensions.

        Args:
            dimensions (list): A list of tuples containing image dimensions (height, width).

        Returns:
            tuple: A tuple containing the mean height and mean width.
      """

      # Mean Height
      mean_height = int(np.mean([dim[0] for dim in dimensions]))

      # Mean Width
      mean_width = int(np.mean([dim[1] for dim in dimensions]))

      # Returning mean dimensions
      return mean_height, mean_width

    def image_alteration(self, image_path, filename,
            max_h, max_w, total_files):

        """
        Alters an image by resizing, padding, and blending it with a grayscale version.

        Args:
            image_path (str): Path to the input image.
            filename (str): The name of the file, used to determine the desaturation ratio.
            max_h (int): Maximum height of the resized image.
            max_w (int): Maximum width of the resized image.
            total_files (int): Total number of files, used to determine the desaturation ratio.

        Returns:
            final_img (numpy.ndarray): The altered image.
        """

        # Final image
        final_img = None
        
        # Annoying Iphone images, OMG!
        if filename.split(".")[1] == "heic":
            # Use pillow-heif extension
            img_t = open_heif(image_path, convert_hdr_to_8bit=False, bgr_mode=True)
            img = np.asarray(img_t)
            
        else:
            # Load the image from the file
            img = cv2.imread(image_path)

        # Check if the image was loaded successfully
        if img is not None:
            
            if len(img.shape) == 2:
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            
            # Actual image dimensions
            img_h, img_w = img.shape[:2]

            # Calculate scaling factors for width and height
            scale_width = max_w / img_w
            scale_height = max_h / img_h

            # Determine scaling factor to fit within max_width and max_height
            scale = min(scale_width, scale_height)

            # Calculate new dimensions after scaling
            new_w = int(img_w * scale)
            new_h = int(img_h * scale)

            # Resize the image
            resized_img = cv2.resize(img, (new_w, new_h))

            # Calculate padding
            top = (max_h - new_h) // 2
            bottom = max_h - new_h - top
            left = (max_w - new_w) // 2
            right = max_w - new_w - left

            # Add padding to resized image
            pad_img = cv2.copyMakeBorder(resized_img, top, bottom, left, right, 
                cv2.BORDER_CONSTANT)

            # Calculate the ratio of desaturation based on the number of images
            # From 1 (full color) to 0 (grayscale)
            ratio = (int(filename.split('.')[0])) / total_files  
            
            # Desaturate the image
            d_img = cv2.cvtColor(pad_img, cv2.COLOR_BGR2GRAY)

            # Channels
            cd_img = cv2.merge((d_img, d_img, d_img))
            
            # Blend the original and desaturated image based on the ratio
            final_img = cv2.addWeighted(pad_img, 1 - ratio, cd_img, ratio, 0)

            # Deleting
            del img, resized_img, d_img, cd_img

        else:
            print(f"## Unsupported File -  {filename} ##")

        return final_img


    def video_writer(self, vid_name, download_folder_name, duration, 
        max_h = 1080, max_w = 1920, codec='mp4v'):
      """
      Writes a video file from downloaded images from a specific folder 
      using OpenCV.

      Args:
          vid_name (str): Name of the output video file.
          download_folder_name (str): Name of the folder where files are located.
          duration (int): Duration(in seconds) of the video, used to calculate fps.
          max_h (int, optional): Maximum height of the images. Defaults to 1080.
          max_w (int, optional): Maximum width of the images. Defaults to 1920.
          codec (str, optional): Codec for video compression. Defaults to 'XVID'.
        
      Returns:
          vid_name (str)

      Note:
          max_h, max_w were given default value because these are the max dimensions
          codecs support.
      """

      # if directory doesn't exist, create
      if not path.exists("videos"):mkdir("videos")

      # Choose the codec for video writing
      fourcc = cv2.VideoWriter_fourcc(*codec)
      
      # Sorting the filenames based on their filename(number)
      sorted_files = sorted(listdir(download_folder_name), key = lambda x:int(x.split('.')[0]))

      # Total files
      total_files = len(sorted_files)
      
      # Calculate fps from duration
      fps = 1 if total_files <= duration else round(total_files/duration)

      # Create a VideoWriter object
      video_writer = cv2.VideoWriter(path.join("videos", vid_name), fourcc=fourcc, fps=fps,
        frameSize=(max_w, max_h))
      
      for filename in sorted_files:
        
        # Display message
        print("File -", filename)

        # Performing image alterations
        final_img = self.image_alteration(path.join(download_folder_name, filename), filename,
            max_h, max_w, total_files)
        
        # Writing the frame
        video_writer.write(final_img)

        # deleting 
        del final_img

        
      # Release the VideoWriter object
      video_writer.release()

      # Return video name -- TODO change
      return vid_name

    def audiofy(self, video_name, audio_name, output_name):
        
        # Load video and audio clips
        video_clip = VideoFileClip(path.join("videos", video_name))
        audio_clip = AudioFileClip(path.join("audios", audio_name))

        # Set the audio of the video clip
        video_clip = video_clip.set_audio(audio_clip)

        # if directory doesn't exist, create
        if not path.exists("final"):mkdir("final")

        # Define output file path
        output_path = path.join("final", output_name)

        # Write the merged video with audio
        video_clip.write_videofile(output_path, codec='libx264', audio_codec='mp3')

        # Close the clips
        video_clip.close()

def main():
    """
    Main function to demonstrate DriveToMovie class usage.
    """
    download_folder_name = 'downloaded_files'
    ran = 0
    files = []
    # Take user input here for which folder to access from the drive          TODO
    folder_name = 'Nee1'
    extensions = {
        '.jpeg': 'image/jpeg',
        '.jpg': 'image/jpg',
        '.png': 'image/png',
        '.heic': 'image/heic',
        '.heif': 'image/heif',
        # '.mp4': 'video/mp4',
        # '.avi': 'video/avi',
        # '.mov': 'video/mov'
    }

    # Check if we have already ran the program before and 
    # folder called downloaded_files exists or not
    if not path.exists(download_folder_name):

      # Display the message
      print(f"Folder {download_folder_name} doesn't exist. The files haven't been downloaded.\n\n")

      # Initiate the Class
      print("Initiating Connection to the Google Drive...")
      dtn = DriveToMovie(ran)
      print("Connection to the Google Drive has been established.")

      # Get folder_ids for folder with folder_name from the drive
      folder_ids = dtn.get_folder_id(folder_name)

      # Iterate through folder_ids of interest, adding them to the list
      for fold_id in folder_ids:
        files.extend(dtn.get_files_from_folder(fold_id, extensions))

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

    # Loading up files and their dimensions
    #image_dimensions, video_dimensions = dtn.handle_downloaded_files(download_folder_name, 
    #    extensions)
    
    #max_h, max_w = dtn.largest_dimensions(image_dimensions, 
    #    video_dimensions)

    ultimate_video = dtn.video_writer("video.mp4", download_folder_name, duration = 90)
    dtn.audiofy("video.mp4", "audio.mp3", "final.mp4")


    
if __name__ == "__main__":
    main()