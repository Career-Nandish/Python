import sys
from os import path
from argparse import ArgumentParser, Namespace
sys.path.append(path.abspath("insta"))
from insta import load_credentials, load_profile
from insta import download_highlights, remove_unnecessary_files
from insta import get_same_file_names, get_same_file_names



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


	args = take_arguements()
	new_path = path.join(args.dir_name, args.highlight_name)
	video_file = "video_names.txt"

	if not path.exists(new_path):
		USERNAME, PASSWORD = load_credentials()
		L, profile = load_profile(USERNAME, PASSWORD)
		download_highlights(L, profile, args.highlight_name, args.dir_name, 
			args.meta_dir)
		# remove_unnecessary_files(new_path)
		# get_same_file_names(new_path, video_file)

	#extract_images_from_video(new_path, video_file)


main()