import sys
from os import path
from cowsay import get_output_string
sys.path.append(path.abspath("google_drive"))
from GoogleDriveClient import GoogleDriveClient, is_valid_name, take_arguements
from argparse import ArgumentParser
sys.path.append(path.abspath("file_handling"))
from FilesCreatedTime import get_actual_createdTime
from FileDownloader import manage_files
sys.path.append(path.abspath("image_processing"))
from ImageHandler import image_modifier
sys.path.append(path.abspath("video_processing"))
from VideoWriter import video_writer, video_enhancer
sys.path.append(path.abspath("audio_processing"))
from Audiofy import audiofy


def main():
	
	args = take_arguements()
	if is_valid_name(args.folder_name):
		print(get_output_string('cow', 'Starting the project'))
		googledriveclient = GoogleDriveClient(args.token_filename, args.creds_filename)
		folder_ids = googledriveclient.get_folder_id(args.folder_name)
		files = googledriveclient.get_files_from_folder(folder_ids, args.extensions)
		downloading_path = manage_files(args.folder_name, files, googledriveclient.creds)
		modified_folder_path = image_modifier(downloading_path)
		video_path = video_writer(modified_folder_path, args.duration_video_sec)
		final_result_path = audiofy(video_path, args.duration_video_sec)
		done_result_path = video_enhancer(final_result_path)
		print(get_output_string('cow', 'Ending the project'))
	else:
		print("==== Invalid Folder Name. ====")
		print("\nPlease ensure the Folder Name follows these rules:")
		print(is_valid_name.__doc__)

main()