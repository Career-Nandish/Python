"""
- Here lies the graveyard of functions.
- Function which were created to use but later deemed useless.
"""


def sort_files(self, files):
    """
    Sorting the list of files.

    Args:
        files (list): List of the files

    Returns:
        list: A list of files in the sorted order based on createdTime.
    """

    # Sorting files based on their createdTime
    return sorted(files, key=lambda d: d['createdTime'])


def handle_downloaded_files(self, download_folder_name, extensions):

    # Initialize list to store dimensions
    image_dimensions = []

    # Initialize lists to store video frames and their dimensions
    video_dimensions = []

    # Iterate over each file in the specified folder
    for filename in listdir(download_folder_name):

        # Checking the type of the file
        # Image File
        if filename.lower().endswith(
            tuple([k for k, v in extensions.items() if 'image' in v])
            ):
            
            # Display message
            print("Image file -", filename)

              # Load the image from the file
              img = cv2.imread(path.join(download_folder_name, filename))

              # Check if the image was loaded successfully
              if img is not None:

                  # Append the image dimensions (height, width) to the
                  # image_dimensions list
                  image_dimensions.append(img.shape[:2])

        # Video File
        elif filename.lower().endswith(tuple([k for k, v in extensions.items() if 'video' in v])):

            # Display message
            print("Video file -", filename)

              # Loading up the video
              cap = cv2.VideoCapture(path.join(download_folder_name, filename))

              # loop runs as long as the video file is successfully opened
              while cap.isOpened():

                # reads a frame from the video
                ret, frame = cap.read()

                # If frame wasn't read successfully, break
                if not ret:
                  break

                # Appending frame dimentions to the list video_dimentions
                video_dimensions.append(frame.shape[:2])
                break

              # Releases the video capture object after processing all frames
              cap.release()

        # Unknown File Type
        else:
            # Display message
            print(f"## UNSUPPORTED FILE TYPE ## - {filename}")

    # with open("Output.txt", "w") as text_file:
    #  text_file.write(string)
    # Returning all necessary variables
    return image_dimensions, video_dimensions


def largest_dimensions(self, image_dimensions, video_dimensions):
    """
    TODO - might add video support later
    """

    # Get the maximum dimensions
    transposed_dim = list(zip(*image_dimensions))

    # Max height
    max_h = max(transposed_dim[0])

    # Max width
    max_w = max(transposed_dim[1])

    return max_h, max_w

def calculate_mean_dimensions(self, dimensions):
    """
        Computes the mean height and width from a list of dimensions.

        Args:
            dimensions (list): A list of tuples containing image dimensions (height, width).

        Returns:
            tuple: A tuple containing the mean height and mean width.
    """

    # Mean Height
    mean_height = int(np.mean([dim[0] for dim in dimensions]))

    # Mean Width
    mean_width = int(np.mean([dim[1] for dim in dimensions]))

    # Returning mean dimensions
    return mean_height, mean_width