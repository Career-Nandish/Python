import json
from github import Github, GithubException, AuthenticatedUser
from github import ContentFile
from pathlib import Path
from typing import Union


def load_gh_credentials() -> str:
    
    """
    Loads PERSONAL ACCESS TOKEN from a text file.

    Reads a JSON file located in the "credentials" directory and extracts the 
    PERSONAL ACCESS TOKEN.

    Returns:
        str: PERSONAL ACCESS TOKEN.

    Raises:
    FileNotFoundError: If the file does not exist.
    json.JSONDecodeError: If the file content is not a valid JSON.
    KeyError: If the required keys (here "PAT") are not found 
              in the JSON file.
    
    """
    print("\n==== Loading credentials for GITHUB ====")
    cred_path = Path.cwd() / "GitHub" / "credentials" / "credentials.txt"

    try:
        # Load credentials from the file
        with cred_path.open("r") as file:
            credentials = json.load(file)

        print("\n==== DONE Loading Credentials for GITHUB ====")
        # Return the username and password
        return credentials["PAT"]
    
    except FileNotFoundError as error:
        print(f"""\n\n**** Error: The credentials file does not exist, 
            {error} ****\n\n""")
    
    except json.JSONDecodeError as error:
        print(f"""\n\n**** Error: The credentials file is not a valid JSON, 
            {error} ****\n\n""")

    except KeyError as error:
        print(f"""\n\n**** Error: The credentials file does not contain the 
            key "PAT", {error} ****\n\n""")

    except Exception as error:
        print(f"""\n\n**** AN UNKNOWN ERROR HAS OCCURRED in load_gh_credentials, 
            {error}****\n\n""")


def get_github_user(PAT: str) -> AuthenticatedUser:
    
    """
    Authenticate with GitHub using a personal access token (PAT) and retrieve the 
    authenticated user's information.

    Args:
        PAT (str): Personal Access Token for GitHub authentication.

    Returns:
        AuthenticatedUser: An object representing the authenticated GitHub user.

    Raises:
        ValueError: If the provided PAT is empty or invalid.
        GithubException: If there is an issue with the authentication or GitHub API call.
    """
    
    try:

        # Check if PAT is an empty string or not
        if not PAT:
            raise ValueError

        # Authenticate with GitHub
        # Retrieve and return the authenticated user
        return Github(PAT).get_user()

    except ValueError as e:
        # Handle exceptions related to GitHub API issues
        print("\n\n**** PERSONAL ACCESS TOKEN MUST NOT BE EMPTY. ****\n\n")
        raise
    
    except GithubException as e:
        # Handle exceptions related to GitHub API issues
        print(f"\n\n**** AN ERROR HAS OCCURRED WHILE ACCESSING GITHUB: {e} ****\n\n")
        raise

    except Exception as e:
        # Handle other potential exceptions
        print(f"\n\n****AN UNEXPECTED ERROR OCCURRED IN get_github_user ****: {e}\n\n")
        raise


def check_folder_exists(
        user: AuthenticatedUser, 
        repo_name: str = "Python",
        project_path: str = "Projects/2_CodewarsAutomated",
        folder_name: str = "Generated",
        file_name: str = "CodewarsAutomated.md"
    ) -> Union[ContentFile.ContentFile, str]:
    
    """
    Check if a specific folder and file exist in a GitHub repository.

    Args:
        user (AuthenticatedUser): The authenticated GitHub user.
        repo_name (str): The name of the repository. Defaults to "Python".
        project_path (str): The path of the project within the repository. 
                            Defaults to "Projects/2_CodewarsAutomated".
        folder_name (str): The name of the folder to check within the project 
                           path. Defaults to "Generated".
        file_name (str): The name of the file to check within the folder. Defaults 
                         to "CodewarsAutomated.md".

    Returns:
        Union[ContentFile.ContentFile, str]: The ContentFile if found, otherwise the 
                                             path of the file as a string.
    """

    # Try block for error handling
    try:
        
        # Display for user
        print(f"\n==== Searching for repository : '{repo_name}'. ====")
        
        # Check if Repository exits
        repo = user.get_repo(repo_name)
        
        # Display for user
        print(f"\n==== Repository : '{repo_name}' found. ====")

        # Path desired
        path_d = f"{project_path}/{folder_name}/{file_name}"
        
        print(f"\n==== Searching for '{path_d}'. ====")

        # Check if path exists
        contents = repo.get_contents(f"""{project_path}/{folder_name}/
            {file_name}""")

        print(f"\n==== File '{path_d}' has been found. ====")

        return contents

    except GithubException as e:

        # Try to find what type of error it is using url data
        documentation_url = e.data.get("documentation_url")

        # Check what kind of error we have encountered
        ## First if the directory doesn't exist
        if "content" in documentation_url:
            print(f"""\n\n**** DIRECTORY '{project_path}' DOESN'T EXIST IN THE 
                REPOSITORY '{repo_name}'. ****\n\n""")
        
        ## Second if the repository doesn't exist
        elif "repository" in documentation_url:
            print(f"""\n\n**** REPOSITORY '{repo_name}' DOESN'T EXIST UNDER 
                GITHUB USER '{user.login}'. ****\n\n""")

        else:
            print(f"\n\n**** AN ERROR OCCURRED: {e.data.get('message', 
                'Unknown error')} ****\n\n")

    except Exception as e:
        # Handle other potential exceptions
        print(f"""\n\n****AN UNEXPECTED ERROR OCCURRED IN check_folder_exists 
            ****: {e}\n\n""")
        raise
    
    finally:
        # Finally block
        print(f"\n==== File '{path_d}' has not been found. Returning Path. ====")
        return path_d