from GoogleDriveClient import GoogleDriveClient, is_valid_name, take_arguements
from argparse import ArgumentParser
from FilesCreatedTime import get_actual_createdTime
from FileDownloader import manage_files
from ImageHandler import image_modifier
from VideoWriter import video_writer
from Audiofy import audiofy


def main():
	args = take_arguements()
	if is_valid_name(args.folder_name):
		googledriveclient = GoogleDriveClient(args.token_filename, args.creds_filename)
		folder_ids = googledriveclient.get_folder_id(args.folder_name)
		files = googledriveclient.get_files_from_folder(folder_ids, args.extensions)
		downloading_path = manage_files(args.folder_name, files, googledriveclient.creds)
		modified_folder_path = image_modifier(downloading_path)
		video_path = video_writer(modified_folder_path)
		final_result_path = audiofy(video_path)

	else:
		print("==== Invalid Folder Name. ====")
		print("\nPlease ensure the Folder Name follows these rules:")
		print(is_valid_name.__doc__)

main()