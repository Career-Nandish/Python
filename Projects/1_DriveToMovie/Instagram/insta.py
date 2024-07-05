import re
import cv2
import random
import emoji
import json
import instaloader
from os import path, mkdir, makedirs, listdir, remove
from pathlib import Path
from dateutil import parser
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload


def load_credentials():
    # Loading credentials from a text file
    with open("password.txt", "r") as file:
        credentials = json.load(file)
    return credentials["username"], credentials["password"]

def remove_emojis(text):
    # Removing emojis from the text
    return re.sub(r":\w+:", "", emoji.demojize(text))

def load_profile(USERNAME, PASSWORD):
    
    # initialize instaloader instance
    L = instaloader.Instaloader()
    
    # Login with your credentials
    L.login(USERNAME, PASSWORD)
    
    # Get profile
    profile = instaloader.Profile.from_username(L.context, USERNAME)
    
    return L, profile


def download_highlights(L, profile, desired_highlight, save_dir):

    # Dictionary to save highlight metadata
    highlight_dict = {}

    # Desired dir
    desired_dir = None

    # if save_dir doesn't exist, create
    if not path.exists(save_dir):
        mkdir(save_dir)

    # Iterate through highlights
    for highlight in L.get_highlights(profile.userid):
        
        title = remove_emojis(highlight.title) 

        # Only download stories from desired highlight
        if title == desired_highlight:

            # Desired dir path
            desired_dir = path.join(save_dir, title)

            # If desired_dir doesn't exist, create
            if not path.exists(desired_dir):
                makedirs(desired_dir)

            # Display message 
            print(f"Downloading highlight: {title} to {desired_dir}")
            
            # Iterating through all the items in the highlight
            for item in highlight.get_items():
                
                highlight_dict[item.mediaid] = {
                    'typename' : item.typename,
                    'date_utc' : str(item.date_utc),
                    'url' : item.url,
                    'is_video' : item.is_video,
                    'video_url' : item.video_url
                }
                
                # Download the item to the custom path
                L.download_storyitem(item, target=Path.cwd().joinpath(desired_dir))
    
    # Writing metadata to a json file
    if not path.exists("metadata"):
                makedirs("metadata")
    
    with open(path.join("metadata", 'metadata.json'), 'w') as file:
        json.dump(highlight_dict, file)

    # Display message
    print("Download completed.")

def remove_unnecessary_files(desired_dir):

    for filename in listdir(desired_dir):
        print(filename)
        # remove a compressed file, unwanted files
        if filename.endswith('.xz'):
            # Display message
            print(f"Deleting {filename} from {desired_dir}...")
            remove(path.join(desired_dir, filename))
    
    print("Unnecessary files removed.")
    return desired_dir

def get_same_file_names(desired_dir, video_file):

    filename_list = listdir(desired_dir)
    video_files_names = []
    
    for filename in filename_list:
        if filename.endswith('.jpg'):
            if (fname:=filename.replace('.jpg', '.mp4')) in filename_list:
                video_files_names.append(fname)

    with open(video_file, "w") as file:
        file.write(", ".join(video_files_names))


def extract_images_from_video(desired_dir, video_file):

    with open(video_file, "r") as file:
        filename_list = file.read().split(", ")

    for filename in filename_list:

        # Open the video file
        cap = cv2.VideoCapture(path.join(desired_dir, filename))
        
        # Get the total number of frames in the video
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # Select a random frame number
        random_frame_number = random.randint(0, total_frames - 1)
        
        # Set the video to the random frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, random_frame_number)
        
        # Read the frame
        ret, frame = cap.read()
        
        # Check if frame is read correctly
        if ret:
            # Save the frame as an image
            f = path.join(desired_dir, filename.replace(".mp4", ""))
            cv2.imwrite(f"{f}.jpg", frame)
            print(f"Saved frame {random_frame_number} as {f}")
        else:
            print("Failed to capture frame")
        
        # Release the video capture object
        cap.release()

        remove(path.join(desired_dir, filename))

    print("Images removed and New ones created.")

def main():
    save_dir = "highlights"
    desired_highlight = "THE ONE"
    new_path = path.join(save_dir, desired_highlight)
    video_file = "video_names.txt"

    if not path.exists(new_path):
        USERNAME, PASSWORD = load_credentials()
        L, profile = load_profile(USERNAME, PASSWORD)
        download_highlights(L, profile, desired_highlight, save_dir)
        remove_unnecessary_files(new_path)
        get_same_file_names(new_path, video_file)
    
    extract_images_from_video(new_path, video_file)

if __name__ == "__main__":
    main()