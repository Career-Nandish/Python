import re
import cv2
import random
import emoji
import json
import instaloader
from os import path, mkdir, makedirs, listdir, remove
from pathlib import Path
from dateutil import parser
from typing import Tuple, Any, Dict, Optional

def load_credentials() -> Tuple[str, str]:
    
    """
    Loads credentials from a text file.

    Reads a JSON file located in the "credentials" directory and extracts the 
    username and password.

    Returns:
    Tuple[str, str]: A tuple containing the username and password.

    Raises:
    FileNotFoundError: If the file does not exist.
    json.JSONDecodeError: If the file content is not a valid JSON.
    KeyError: If the required keys ("username" and "password") are not found 
              in the JSON file.
    """
    print("\n==== Loading Credentials ====\n")
    try:
        # Load credentials from the file
        with open(path.join("credentials", "password.txt"), "r") as file:
            credentials = json.load(file)

        print("\n==== DONE Loading Credentials ====\n")
        # Return the username and password
        return credentials["username"], credentials["password"]
    
    except FileNotFoundError as error:
        print(f"\n\n**** Error: The credentials file does not exist, {error} ****\n\n")
    
    except json.JSONDecodeError as error:
        print(f"\n\n**** Error: The credentials file is not a valid JSON, {error} ****\n\n")

    except KeyError as error:
        print(f"""\n\n**** Error: The credentials file does not contain the 
                 required keys 'username' and 'password', {error} ****\n\n""")

    except Exception as error:
        print(f"\n\n**** AN UNKNOWN ERROR HAS OCCURRED, {error}****\n\n")


def remove_emojis(text: str) -> str:
    
    """
    Removes emojis from a given text string.

    This function converts all emojis in the input text to their respective 
    text representation using `emoji.demojize`, and then removes them using 
    a regular expression.

    Args:
    - text (str): The input text containing emojis.

    Returns:
    - str: The text with emojis removed.
    """
    
    # Convert emojis to text representation and remove them using regex
    return re.sub(r":\w+:", "", emoji.demojize(text))


def load_profile(USERNAME: str, 
    PASSWORD: str) -> Tuple[instaloader.Instaloader, 
                            instaloader.Profile]:
    
    """
    Loads an Instagram profile using provided credentials.

    Initializes an Instaloader instance, logs in with the given username and 
    password, and retrieves the profile.

    Args:
    - USERNAME (str): The Instagram username.
    - PASSWORD (str): The Instagram password.

    Returns:
    - Tuple[instaloader.Instaloader, instaloader.Profile]: A tuple containing 
          the Instaloader instance and the profile.

    Raises:
    - instaloader.exceptions.ConnectionException: If there is a connection error.
    - instaloader.exceptions.BadCredentialsException: If the credentials are incorrect.
    - instaloader.exceptions.TwoFactorAuthRequiredException: If two-factor authentication 
                                                             is required.
    - instaloader.exceptions.ProfileNotExistsException: If the profile does not exist.
    """
    print("\n==== Loading the Profile ====\n")
    try:
        # Initialize Instaloader instance
        L = instaloader.Instaloader()

        # Login with the provided credentials
        L.login(USERNAME, PASSWORD)

        # Get the profile
        profile = instaloader.Profile.from_username(L.context, USERNAME)

        print("\n==== DONE Loading the Profile ====\n")
        return L, profile
    
    except instaloader.exceptions.ConnectionException as error:
        print(f"\n\n**** Error: Unable to connect to Instagram, {error} ****\n\n")
        
    except instaloader.exceptions.BadCredentialsException as error:
        print(f"\n\n**** Error: Incorrect Username or Password, {error} ****\n\n")
        
    except instaloader.exceptions.TwoFactorAuthRequiredException as error:
        print(f"\n\n**** Error: Two-factor authentication is required, {error} ****\n\n")
        
    except instaloader.exceptions.ProfileNotExistsException as error:
        print(f"\n\n**** Error: The profile does not exist, {error} ****\n\n")

    except Exception as error:
        print(f"\n\n**** AN UNKNOWN ERROR HAS OCCURRED, {error}****\n\n")
        

def download_highlights(L: instaloader.Instaloader, profile: instaloader.Profile, 
    desired_highlight: str, save_dir: str, metadata_dir:str) -> str:
    
    """
    Downloads Instagram highlight stories and saves them to the specified 
    directory.

    This function iterates through the highlights of the given profile, 
    identifies the desired highlight by its title, and downloads all the 
    items (stories) in that highlight to a specified directory. Additionally, 
    it saves metadata of the downloaded items to a JSON file.

    Args:
    - L (instaloader.Instaloader): The Instaloader instance.
    - profile (instaloader.Profile): The Instagram profile instance.
    - desired_highlight (str): The title of the highlight to download.
    - save_dir (str): The directory where the highlight stories will be saved.
    - metadata_dir (str) : The directory where the metadata will be saved.

    Returns:
    - str: The path save_dir\desired_highlight.
    """

    try:
        # Dictionary to save highlight metadata
        highlight_dict: Dict[str, Dict[str, Any]] = {}

        # Desired directory path
        desired_dir: Optional[str] = None

        # If save_dir doesn't exist, create it
        if not path.exists(save_dir):
            mkdir(save_dir)
        
        print("\n==== Searching through all highlights ====\n")

        # Iterate through highlights
        for highlight in L.get_highlights(profile.userid):
            
            # Remove emojis and other special characters from
            # the title of the highlight
            title = remove_emojis(highlight.title)

            # Only download stories from the desired highlight
            if title == desired_highlight:
                
                print(f"Match Found: {title}\n")
                
                # Desired directory path
                desired_dir = path.join(save_dir, title)

                # If desired_dir doesn't exist, create it
                 if not path.exists(desired_dir):
                    makedirs(desired_dir)

                # Display message
                print(f"Downloading highlight: {title} to {desired_dir}")

                # Iterating through all the items in the highlight
                for item in highlight.get_items():
                    highlight_dict[item.mediaid] = {
                        'typename': item.typename,
                        'date_utc': str(item.date_utc),
                        'url': item.url,
                        'is_video': item.is_video,
                        'video_url': item.video_url
                    }

                    # Download the item to the custom path
                    try:
                        L.download_storyitem(item, 
                            target=Path.cwd().joinpath(desired_dir))
                    except Exception as error:
                        print(f"\n\n**** ERROR DOWNLOADING ITEM {item.mediaid}: {error} ****\n\n")

                print(f"DONE Downloading highlight: {title} to {desired_dir}")
        
        # Writing metadata to a JSON file
        if not path.exists(metadata_dir):
            makedirs(metadata_dir)

        with open(path.join(metadata_dir, 'metadata.json'), 'w') as file:
            json.dump(highlight_dict, file, indent=4)

        # Display message
        print("\n==== All Highlights are downloaded. ====\n")
        return desired_dir

    except Exception as error:
        print(f"\n\n**** AN UNKNOWN ERROR OCCURRED: {error} ****\n\n")

def remove_unnecessary_files(desired_dir: str) -> str:
    
    """
    Removes unnecessary files from the specified directory.

    This function iterates through all files in the given directory and 
    deletes any file that ends with the '.xz' extension. It prints the 
    name of each file it processes and confirms when the removal is complete.

    Args:
    - desired_dir (str): The directory from which unnecessary files should 
                         be removed.

    Returns:
    - str: The path to the directory after cleanup.
    """
    print("\n==== Removing Unnecessary Files ====\n")
    
    try:
        for filename in listdir(desired_dir):

            print(f"Handling file - {filename}")
            
            # remove a compressed file, unwanted files
            if filename.endswith('.xz'):
                
                try:
                    
                    # Display message
                    print(f"\tDeleting {filename} from {desired_dir}...")
                    
                    # deleting the file
                    remove(path.join(desired_dir, filename))
                
                except Exception as error:
                    print(f"\n\n**** ERROR DELETING FILE {filename}: {error} ****\n\n")
        
        # display
        print("\n====DONE Removing Unnecessary Files ====\n")
        
        return desired_dir
    
    except Exception as error:
        print(f"\n\n**** AN UNKNOWN ERROR HAS OCCURRED: {error} ****\n\n")

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