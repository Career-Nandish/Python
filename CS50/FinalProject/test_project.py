import os
import pytest
import subprocess

# Define a temporary directory for testing
TEST_DIRECTORY = "./test_directory"
EMPTY_DIRECTORY = "./empty_directory"
NON_EXISTENT_DIRECTORY = "./non_existent_directory"

def setup_module(module):

    # temporary directory and add some files
    os.makedirs(TEST_DIRECTORY, exist_ok=True)
    open(os.path.join(TEST_DIRECTORY, "test_image.jpg"), "w").close()
    open(os.path.join(TEST_DIRECTORY, "test_document.pdf"), "w").close()
    open(os.path.join(TEST_DIRECTORY, "test_video.mp4"), "w").close()
    open(os.path.join(TEST_DIRECTORY, "test_other.html"), "w").close()


    # empty directory
    os.makedirs(EMPTY_DIRECTORY, exist_ok=True)

def teardown_module(module):
    
    def remove_dir(dir):
        # remove the temporary directory and its contents
        if os.path.exists(dir):
            
            # windows
            if os.name == 'nt':
                subprocess.run(['cmd', '/c', 'rd', '/s', '/q', dir[2:]], check=True)
            
            # Unix-like systems
            else:  
                subprocess.run(['rm', '-rf', f'{dir}/*'], check=True)
            
            # display for devs
            print(f"Contents of directory '{dir}' removed.")
        else:
            # display for devs
            print(f"Directory '{dir}' does not exist.")

    remove_dir(TEST_DIRECTORY)
    remove_dir(EMPTY_DIRECTORY)
    remove_dir(NON_EXISTENT_DIRECTORY)

def test_organize_files():
    
    # Test organize_files function via subprocess
    command = ["python", "project.py", TEST_DIRECTORY]

    # Run the project.py using subprocess
    result = subprocess.run(command, capture_output=True, text=True)

    # Check if files are correctly moved to respective folders
    assert os.path.exists(os.path.join(TEST_DIRECTORY, "Images", 
        "test_image.jpg"))
    assert os.path.exists(os.path.join(TEST_DIRECTORY, "Documents", 
        "test_document.pdf"))
    assert os.path.exists(os.path.join(TEST_DIRECTORY, "Videos", 
        "test_video.mp4"))
    assert os.path.exists(os.path.join(TEST_DIRECTORY, "Others", 
        "test_other.html"))


def test_empty_directory():
    
    """
    Test the function with an empty directory.
    """
    
    command = ["python", "project.py", EMPTY_DIRECTORY]
    result = subprocess.run(command, capture_output=True, text=True)

    # Check if the function runs without error and no directories are created
    assert os.path.exists(EMPTY_DIRECTORY)

    # Directory should remain empty
    assert len(os.listdir(EMPTY_DIRECTORY)) == 0  

def test_non_existent_directory():
    
    """
    Test the function with a non-existent directory.
    """
    command = ["python", "project.py", NON_EXISTENT_DIRECTORY]
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Check if the function raises a FileNotFoundError
    assert "FileNotFoundError" in result.stdout

def test_only_specified_file_types_moved():
    
    """
    Test that only files with specified extensions are moved to their respective folders.
    """
    
    # Add a file with an unspecified extension
    open(os.path.join(TEST_DIRECTORY, "test_unspecified.xyz"), "w").close()
    
    # Run the project.py script using subprocess
    command = ["python", "project.py", TEST_DIRECTORY]
    result = subprocess.run(command, capture_output=True, text=True)

    # Check if the file with unspecified extension is moved to "Others"
    assert os.path.exists(os.path.join(TEST_DIRECTORY, "Others", 
        "test_unspecified.xyz"))

if __name__ == "__main__":
    pytest.main()