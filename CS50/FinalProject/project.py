import os
import shutil
import argparse
import sys

def organize_files(directory: str) -> None:
    """
    Organizes files in a directory into respective folders based on their types.
    
    Args:
    - directory (str): Path to the directory containing files to organize.
    
    Returns:
    - None
    """
    try:
        # Define folder names for different types of files and counters
        extensions = {
            # all images
            "Images": [".jpg", ".jpeg", ".png", ".gif"],
            # documents
            "Documents": [".pdf", ".docx", ".xlsx", ".pptx"],
            # videos
            "Videos": [".mp4", ".avi", ".mov"],
            # all other extensions
            "Others": []  
        }

        # To keep track of how many files were moved per category
        counts = {category: 0 for category in extensions}

        if not os.path.exists(directory):
            print(f"Error: The directory '{directory}' does not exist.")
            raise FileNotFoundError
        else:
            if os.listdir(directory):
                # Create folders if they don"t exist
                for folder in extensions:
                    folder_path = os.path.join(directory, folder)
                    os.makedirs(folder_path, exist_ok=True)
        
        # Organize files into respective folders
        for filename in os.listdir(directory):

            # create the file path
            file_path = os.path.join(directory, filename)

            # to check if the file_path is actually a file
            if os.path.isfile(file_path):

                # extract the extension
                file_extension = os.path.splitext(filename)[1].lower()

                # init the flag moved to false
                moved = False

                # iterate over all files in the directory given
                for category, ext_list in extensions.items():
                    # if file ext in the catgeory
                    if file_extension in ext_list:

                        # choose the destination based on ext
                        destination_folder = os.path.join(directory, category)

                        # Move the file to the destination folder
                        shutil.move(file_path, destination_folder)

                        # display for users
                        print(f"Moved {filename} to {category} folder.")

                        # update the counts and the moved flag
                        counts[category] += 1
                        moved = True

                        # once moved break the loop
                        break
                
                if not moved:
                    # if doesn't match any extension, move to "others"
                    destination_folder = os.path.join(directory, "Others")
                    shutil.move(file_path, destination_folder)

                    # display for users
                    print(f"Moved {filename} to 'Others' folder.")

                    # update the count
                    counts["Others"] += 1
        
        # Print information about files moved to each category
        print(f"Files in '{directory}' have been organized successfully:")
        
        # Category wise info
        for category, count in counts.items():
            print(f"- {category}: {count} file(s)")
    
    except FileNotFoundError as error:
        print(f"Error: Directory '{directory}' not found.")
    
    except Exception as error:
        print(f"An error occurred: {error}")

def main():

    try:
        # Setup argument parser
        parser = argparse.ArgumentParser(description="File Organizer Tool")
        parser.add_argument("directory", type=str, 
            help="Path to the directory to organize")
        
        # Parse command line arguments
        args = parser.parse_args()
        directory = args.directory
        
        # Validate if directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")
        
        # Organize files in the specified directory
        organize_files(directory)
    
    except argparse.ArgumentError as error:
        print(f"ArgumentError: {error}")
    
    except FileNotFoundError as error:
        print(f"FileNotFoundError: {error}")
    
    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()