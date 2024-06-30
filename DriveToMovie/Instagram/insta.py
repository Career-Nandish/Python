import re
import emoji
import json
import instaloader
from os import path, mkdir, makedirs
from pathlib import Path

def load_credentials():
    with open("password.txt", "r") as file:
        credentials = json.load(file)
    return credentials["username"], credentials["password"]

def remove_emojis(text):
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


    # if save_dir doesn't exist, create
    if not path.exists(save_dir):
        mkdir(save_dir)
    count = 1
    # Iterate through highlights
    for highlight in L.get_highlights(profile.userid):
        
        title = remove_emojis(highlight.title)
        desired_dir = path.join(save_dir, title)
        if title == desired_highlight:
            if not path.exists(desired_dir):
                makedirs(desired_dir)
            print(f"Downloading highlight: {title} to {desired_dir}")
            print(dir(L))
            
            for item in highlight.get_items():
                # Print metadata
                print(f"Metadata for story item:")
                print(f"ID: {item.mediaid}")
                print(f"Type: {item.typename}")
                print(f"Date: {item.date_utc}")
                print(f"URL: {item.url}")
                print(f"Caption: {item.caption}")
                count+=1
                # Download the item to the custom path
                
                L.download_storyitem(item, target=Path.cwd().joinpath(desired_dir))
        
    print("Download completed.", count)

    return 1

def main():
    USERNAME, PASSWORD = load_credentials()
    
    L, profile = load_profile(USERNAME, PASSWORD)

    save_dir = "highlights"

    desired_highlight = "THE ONE"

    metadata = download_highlights(L, profile, desired_highlight, save_dir)

if __name__ == "__main__":
    main()