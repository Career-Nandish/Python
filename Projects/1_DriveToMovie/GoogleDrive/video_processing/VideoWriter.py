import cv2
from os import path, mkdir, listdir

def video_writer(download_folder_name: str, duration: int, 
    vid_name: str = "video.mp4", max_h: int = 1080, max_w: int = 1920, 
    codec: str = 'mp4v') -> str:
    
    """
    Writes a video file from downloaded images in a specific folder using OpenCV.

    Args:
        download_folder_name (str): Name of the folder where image files are located.
        duration (int): Duration (in seconds) of the video, used to calculate fps. 
        vid_name (str): Name of the output video file. Defaults to "video.mp4".
        max_h (int, optional): Maximum height of the images. Defaults to 1080.
        max_w (int, optional): Maximum width of the images. Defaults to 1920.
        codec (str, optional): Codec for video compression. Defaults to 'mp4v'.
        
    Returns:
        str: Path where the video is saved.

    Note:
        max_h and max_w are given default values because these are the maximum 
        dimensions that codecs support.
    """
    
    # Path to save video
    video_path = "resources\\videos"
    
    try:
        # If the directory doesn't exist, create it
        if not path.exists(video_path):
            mkdir(video_path)

        # Choose the codec for video writing
        fourcc = cv2.VideoWriter_fourcc(*codec)
        
        # Sorting the filenames based on their filename (number)
        sorted_files = sorted(listdir(download_folder_name), 
            key=lambda x: int(x.split('.')[0]))

        # Total files
        total_files = len(sorted_files)
        
        # Calculate fps from duration
        fps = 1 if total_files <= duration else total_files // duration

        # Create a VideoWriter object
        video_writer = cv2.VideoWriter(path.join(video_path, vid_name), 
            fourcc=fourcc, fps=fps, frameSize=(max_w, max_h))
        
        for filename in sorted_files:
            try:
                # Display message
                print(f"==== Writing {filename} to the video. ====")

                # Read the image file
                final_img = cv2.imread(path.join(download_folder_name, filename))

                # TO see if all the images are included in the video - manual check
                #cv2.putText(final_img, filename, (400, 500), cv2.FONT_HERSHEY_SIMPLEX, 
                #    4, (255, 255, 255), 4)

                # Check if the image was loaded successfully
                if final_img is None:
                    print(f"\n\n**** WARNING: FAILED TO LOAD IMAGE FILE {filename}. Skipping. ****")
                    continue

                # Writing the frame
                video_writer.write(final_img)

                # Deleting the image from memory
                del final_img

            except Exception as error:
                print(f"\n\n**** ERROR PROCESSING FILE '{filename}': {error} ****")

        # Release the VideoWriter object
        video_writer.release()

        # Return the path where the video is saved
        return path.join(video_path, vid_name)
    
    except Exception as error:
        print(f"\n\n**** ERROR IN video_writer: {error} ****")
        return None