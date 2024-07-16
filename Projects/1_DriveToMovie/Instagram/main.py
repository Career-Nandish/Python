import sys
from os import path
from argparse import ArgumentParser, Namespace

# Import functions from insta\insta.py
sys.path.append(path.abspath("insta"))
from insta import load_credentials, load_profile
from insta import download_highlights, remove_unnecessary_files
from insta import get_same_file_names, extract_images_from_videos

# Import functions from drive\files_to_drive.py
sys.path.append(path.abspath("drive"))
from files_to_drive import upload_images

# Import class from ..\GoogleDrive\google_drive.py
sys.path.append(path.abspath("..\\GoogleDrive\\google_drive"))
from GoogleDriveClient import GoogleDriveClient


def take_arguements() -> Namespace:
    
    """
    Parses command-line arguments for the script.

    Returns:
    - Namespace: The parsed arguments as a Namespace object.
    """
    
    # Init ArgumentParser
    parser = ArgumentParser(
        description="Download images/videos from given highlights"
    )

    # Add arguments
    parser.add_argument(
        "-n",
        "--highlight_name", 
        type=str,
        required=True, 
        help="The name of the desired highlight. <CASE-SENSITIVE>"
    )
    parser.add_argument(
        "-g",
        "--gdrive_folder", 
        type=str,
        required=True,
        help="""The name of the Google Drive folder where to save images/videos from 
                the highlight. <CASE-SENSITIVE>"""
    )
    parser.add_argument(
        "-d",
        "--dir_name", 
        type=str, 
        default="highlights", 
        help="Directory to save images/videos from the highlights"
    )
    parser.add_argument(
        "-m",
        "--meta_dir", 
        type=str,
        default="metadata",
        help="Directory to save metadata of the files"
    )
    parser.add_argument(
        "-t",
        "--token_filename", 
        type=str, 
        default="token.json", 
        help="User token file for Google Drive"
    )
    parser.add_argument(
        "-c",
        "--creds_filename", 
        type=str, 
        default="credentials.json", 
        help="User credential file(API keys) for Google Drive"
    )

    # Return Namespace object
    return parser.parse_args()


def main():

	# Take command line arguments
	args = take_arguements()

	# desired dir path
	desired_dir = path.join(args.dir_name, args.highlight_name)
	
	# INSTAGRAM PART
	## if not highlight\desired_highlight exists
	if not path.exists(desired_dir):

		## Load the credentials
		USERNAME, PASSWORD = load_credentials()

		## Load instagram profile
		L, profile = load_profile(USERNAME, PASSWORD)

		## From the loaded profile, download specific highlight
		desired_dir = download_highlights(L, profile, args.highlight_name, 
			args.dir_name, args.meta_dir)

		## remove unnecessary files
		_ = remove_unnecessary_files(desired_dir)

		## Video file names from the highlights
		video_file_path = get_same_file_names(desired_dir)

		## extract images from videos
		_ = extract_images_from_videos(desired_dir, video_file_path)


	# GOOGLE DRIVE PART
	## Make an instance of drive client
	gdc = GoogleDriveClient(args.token_filename, args.creds_filename)

	## Get folder_ids for folder with folder_name from the drive
	folder_ids = gdc.get_folder_id(args.gdrive_folder)

	## Upload images to the google drive
	upload_images(gdc, folder_ids, desired_dir)

main()