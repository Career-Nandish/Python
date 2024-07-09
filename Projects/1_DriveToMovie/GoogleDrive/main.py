from GoogleDriveClient import GoogleDriveClient, is_valid_name
from argparse import ArgumentParser
from FilesCreatedTime import get_actual_createdTime


def take_arguements():
	parser = ArgumentParser(
		description="List files from folder IDs with given folder name on the Google Drive."
		)
	parser.add_argument(
		"-t",
		"--token_filename", 
		type=str, 
		default="token.json", 
		help="User token file."
		)
	parser.add_argument(
		"-c",
		"--creds_filename", 
		type=str, 
		default="credentials.json", 
		help="User credential file(API keys). Must be a .json File."
		)
	parser.add_argument(
    	"-f",
    	"--folder_name", 
    	type=str,
    	required=True,
    	help="Name of the Google Drive Folder with desired files."
    	)
	parser.add_argument(
    	"-e",
    	"--extensions",
    	nargs='+',
    	default=['image/jpeg', 'image/png', 'image/jpg', 'image/heic', 'image/heif'],
    	help="List of MIME types/extensions of the desired files."
    	)

	return parser.parse_args()


def main():
	args = take_arguements()
	if is_valid_name(args.folder_name):
		googledriveclient = GoogleDriveClient(args.token_filename, args.creds_filename)
		folder_ids = googledriveclient.get_folder_id(args.folder_name)
		files = googledriveclient.get_files_from_folder(folder_ids, args.extensions)
	else:
		print("==== Invalid Folder Name. ====")
		print("\nPlease ensure the Folder Name follows these rules:")
		print(is_valid_name.__doc__)

main()