import json
from github import Github, GithubException, AuthenticatedUser
from pathlib import Path


def load_credentials() -> str:
    
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
    print("\n==== Loading credentials ====")
    cred_path = Path.cwd() / "GitHub" / "credentials" / "credentials.txt"

    try:
        # Load credentials from the file
        with cred_path.open("r") as file:
            credentials = json.load(file)

        print("\n==== DONE Loading Credentials ====")
        # Return the username and password
        return credentials["PAT"]
    
    except FileNotFoundError as error:
        print(f"\n\n**** Error: The credentials file does not exist, {error} ****\n\n")
    
    except json.JSONDecodeError as error:
        print(f"\n\n**** Error: The credentials file is not a valid JSON, {error} ****\n\n")

    except KeyError as error:
        print(f"""\n\n**** Error: The credentials file does not contain the key "PAT", 
            {error} ****\n\n""")

    except Exception as error:
        print(f"\n\n**** AN UNKNOWN ERROR HAS OCCURRED in load_credentials, {error}****\n\n")


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
        print(f"\n\n****AN UNEXPECTED ERROR OCCURRED ****: {e}\n\n")
        raise