import requests
import json
from github import Github
from typing import Tuple
from pathlib import Path



def load_credentials() -> Tuple[str, str]:
    
    """
    Loads credentials from a text file.

    Reads a JSON file located in the "credentials" directory and extracts the 
    client ID and client secret.

    Returns:
    Tuple[str, str]: A tuple containing the user_login and password.

    Raises:
    FileNotFoundError: If the file does not exist.
    json.JSONDecodeError: If the file content is not a valid JSON.
    KeyError: If the required keys ("user_login" and "password") are not found 
              in the JSON file.
    
    """
    print("\n==== Loading Credentials ====\n")
    cred_path = Path.cwd() / "GitHub" / "credentials" / "credentials.txt"

    try:
        # Load credentials from the file
        with cred_path.open("r") as file:
            credentials = json.load(file)

        print("\n==== DONE Loading Credentials ====\n")
        # Return the username and password
        return credentials["user_login"], credentials["password"]
    
    except FileNotFoundError as error:
        print(f"\n\n**** Error: The credentials file does not exist, {error} ****\n\n")
    
    except json.JSONDecodeError as error:
        print(f"\n\n**** Error: The credentials file is not a valid JSON, {error} ****\n\n")

    except KeyError as error:
        print(f"""\n\n**** Error: The credentials file does not contain the 
                 required keys 'user_login' and 'password', {error} ****\n\n""")

    except Exception as error:
        print(f"\n\n**** AN UNKNOWN ERROR HAS OCCURRED in load_credentials, {error}****\n\n")