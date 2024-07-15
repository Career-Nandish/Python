from os import path, mkdir
from moviepy.editor import VideoFileClip, AudioFileClip

def audiofy(video_path: str, audio_name: str = "audio.mp3", 
    output_name: str = "final.mp4") -> str:
    
    """
    Adds an audio track to a video file and saves the output.

    Args:
        video_name (str): The name of the video file to which the 
                          audio will be added.
        audio_name (str): The name of the audio file to be added to 
                          the video.
        output_name (str): The name of the output video file with the 
                           added audio.

    Returns:
        str: The path to the output video file path.

    Raises:
        FileNotFoundError: If the video or audio file is not found.
        Exception: For any other exceptions that may occur during processing.
    """

    final_path = "resources\\final"
    audio_path = "resources\\audios"

    try:
        # Load video and audio clips
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(path.join(audio_path, audio_name))

        # Set the audio of the video clip
        video_clip = video_clip.set_audio(audio_clip)

        # If the directory doesn't exist, create it
        if not path.exists(final_path):
            mkdir(final_path)

        # Define output file path
        output_path = path.join(final_path, output_name)

        # Write the merged video with audio
        video_clip.write_videofile(output_path, codec='libx264', audio_codec='mp3')

        # Close the clips
        video_clip.close()
        audio_clip.close()

        return output_path

    except FileNotFoundError as ferror:
        print(f"\n\n**** FILE NOT FOUND: {ferror} ****")
        return None
    
    except Exception as error:
        print(f"\n\n**** ERROR IN audiofy: {error}")
        return None