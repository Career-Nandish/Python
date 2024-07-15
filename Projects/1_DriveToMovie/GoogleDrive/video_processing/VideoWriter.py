import cv2
import subprocess
from os import path, mkdir, listdir

def video_writer(download_folder_name: str, duration: int, 
    vid_name: str="video.mp4", max_h: int=1080, max_w: int=1920, 
    codec: str='mp4v') -> str:
    
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
    print("\n==== Writing images to the video ====\n")
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
                print(f"Writing {filename} to the video.")

                # Read the image file
                final_img = cv2.imread(path.join(download_folder_name, filename))

                # TO see if all the images are included in the video - manual check
                #cv2.putText(final_img, filename, (400, 500), cv2.FONT_HERSHEY_SIMPLEX, 
                #    4, (255, 255, 255), 4)

                # Check if the image was loaded successfully
                if final_img is None:
                    print(f"\n\n**** WARNING: FAILED TO LOAD IMAGE FILE {filename}. Skipping. ****\n\n")
                    continue

                # Writing the frame
                video_writer.write(final_img)

                # Deleting the image from memory
                del final_img

            except Exception as error:
                print(f"\n\n**** ERROR PROCESSING FILE '{filename}': {error} ****\n\n")

        # Release the VideoWriter object
        video_writer.release()

        print("\n==== DONE writing images to the video ====\n")
        # Return the path where the video is saved
        return path.join(video_path, vid_name)
    
    except Exception as error:
        print(f"\n\n**** ERROR IN video_writer: {error} ****\n\n")
        return None


def video_enhancer(result_path: str, bitrate: str ="15000k", 
    aspect_ratio: int=1920) -> str:
    
    """
    Enhances a video by adding padding to maintain the specified aspect ratio
    and setting a specified bitrate using FFmpeg.

    Args:
        result_path (str): The path to the input video file.
        bitrate (str, optional): The target video bitrate. 
                                 Defaults to "15000k".
        aspect_ratio (int, optional): The target aspect ratio for the 
                                      output video. Defaults to 1920.

    Returns:
        str: The path to the enhanced video file.
    """
    
    # Split the input path to create the output path
    path_split = result_path.split("\\")
    output_file = "\\".join(path_split[:-1]) + "\\enhanced_" + path_split[-1]

    # ffmpeg command to add padding, maintain aspect ratio, and set bitrate
    ffmpeg_command = [
        # use ffmpeg
        "ffmpeg", "-i", result_path,
        
        # change aspect ratio
        "-vf", f"scale=w={aspect_ratio}:h={aspect_ratio}:force_original_aspect_ratio=decrease,"
               # padding
               f"pad={aspect_ratio}:{aspect_ratio}:(ow-iw)/2:(oh-ih)/2",
        # chosen bitrate
        "-b:v", bitrate,
        # output file
        "-c:a", "copy", output_file,
        # hide unwanted stuff
        "-nostats", "-loglevel", "0",
        
    ]

    try:
        print("\n==== Video Enhancement ====\n")
        print(f"Input video: {result_path}")
        print(f"Output video: {output_file}")
        print(f"Bitrate: {bitrate}")
        print(f"Aspect ratio: {aspect_ratio}")

        print("Enhancing the video...")
        # Run the ffmpeg command
        subprocess.run(ffmpeg_command, check=True)

        print("\n==== Video enhancement completed successfully. ====")
        print(f"==== Enhanced video saved at: {output_file} ====\n")

    except subprocess.CalledProcessError as error:
        print(f"\n\n**** AN ERROR OCCURRED WHILE ENHANCING THE VIDEO: {error} ****\n\n")
        raise

    return output_file