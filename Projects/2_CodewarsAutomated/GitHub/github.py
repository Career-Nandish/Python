import os
from github import Github, GithubException, AuthenticatedUser
from github import ContentFile
from typing import Union


def load_gh_credentials() -> str:
    
    """
    Loads PERSONAL ACCESS TOKEN from the ENVIRONMENT VARIABLES.

    Returns:
        str: PERSONAL ACCESS TOKEN.

    Raises:
        EnvironmentError : if variable hasn't been set or it's missing.
        RuntimeError: Potential runtime errors.
    
    """
    print("\n==== Loading credentials for GITHUB ====")
    
    try:
        # Load PAT from ENVIRONMENT VARIABLES
        PAT = os.environ["GITHUB_PAT"]

        # Display for user
        print("\n==== Done Loading Credentials for GITHUB ====")
        
        return PAT 
    
    except KeyError as e:
        raise EnvironmentError(
            "\n\n**** ERROR: ENVIRONMENT VARIABLE GITHUB_PAT IS MISSING! ****\n\n"
            )

    except Exception as e:
        raise RuntimeError(
                  f"\n\n**** ERROR: AN UNKNOWN ERROR HAS OCCURRED IN 'load_gh_credentials' : {e} ****\n\n"
              ) from e


def get_github_user(PAT: str) -> AuthenticatedUser:
    
    """
    Authenticate with GitHub using a Personal Access Token (PAT) 
    and return the authenticated user object.

    Args:
        PAT (str): Personal Access Token for GitHub authentication.

    Returns:
        AuthenticatedUser: The authenticated GitHub user.

    Raises:
        ValueError: If the provided PAT is empty.
        GithubException: If authentication fails or GitHub API call errors occur.
        RuntimeError: Potential runtime errors.
    """
    
    try:

        # Check if PAT is an empty string or not
        if not PAT:
            raise ValueError(
                      "\n\n**** ERROR: PERSONAL ACCESS TOKEN MUST NOT BE EMPTY. ****\n\n"
                  )

        # Authenticate with GitHub and return the user
        return Github(PAT).get_user()
    
    except GithubException as e:

        # Token Permissions
        if e.status == 403:
            raise GithubException(
                      f"\n\n**** ERROR: ACCESS FORBIDDEN - CHECK YOUR GITHUB TOKEN PERMISSIONS : {e} ****\n\n"
                  ) from e

        # Token invalid/expired
        elif e.status == 401:
            raise GithubException(
                      f"\n\n**** ERROR: UNAUTHORIZED — INVALID OR EXPIRED GITHUB TOKEN : {e} ****\n\n"
                  ) from e

        # other exceptions under Github
        else:
            # Handle exceptions related to GitHub API issues
            raise GithubException(
                      f"\n\n**** ERROR: ERROR AUTHENTICATING WITH GITHUB: {e} ****\n\n"
                  ) from e

    except Exception as e:
        # Handle other potential runtime exceptions
        raise RuntimeError(
                  f"\n\n**** ERROR: AN UNEXPECTED ERROR OCCURRED IN 'get_github_user': {e} ****\n\n"
              ) from e


def check_folder_exists(
        user: AuthenticatedUser, 
        repo_name: str = "Python",
        folder_name: str = "CodewarsSolutions",
        file_name: str = "CodewarsAutomated.md"
    ) -> Union[ContentFile.ContentFile, str]:
    
    """
    Check if a specific folder and file exist in a GitHub repository.

    Args:
        user (AuthenticatedUser): The authenticated GitHub user.
        repo_name (str): The name of the repository. Defaults to "Python".
        folder_name (str): The name of the folder to check within the project 
                           path. Defaults to "CodewarsSolutions".
        file_name (str): The name of the file to check within the folder. Defaults 
                         to "CodewarsAutomated.md".

    Returns:
        Union[ContentFile.ContentFile, str]: The ContentFile if found, otherwise the 
                                             path of the file as a string.

    Raises:
        GithubException: If authentication fails or GitHub API call errors occur.
        RuntimeError: Potential runtime errors.
    """

    # Path desired
    path_d = f"{folder_name}/{file_name}"

    # Try block for error handling
    try:

        # Display for user
        print(f"\n==== Searching for repository : '{repo_name}'. ====")
        
        # Check if Repository exits
        repo = user.get_repo(repo_name)
        
        # Display for user
        print(f"\n==== Repository : '{repo_name}' found. ====")        
        print(f"\n==== Searching for '{repo_name}/{path_d}'. ====")

        # Check if path exists
        contents = repo.get_contents(path_d)

        print(f"\n==== File '{repo_name}/{path_d}' has been found. ====")

        return contents

    except GithubException as e:

        # Existance check
        if e.status == 404:
            print(f"\n==== File or folder '{path_d}' does not exist in repository '{repo_name}'. ====")
            return f"{repo_name}/{path_d}"
        
        # Token Permissions
        elif e.status == 403:
            raise GithubException(
                      f"\n\n**** ERROR: ACCESS FORBIDDEN - CHECK YOUR GITHUB TOKEN PERMISSIONS : {e} ****\n\n"
                  ) from e

        # Token invalid/expired
        elif e.status == 401:
            raise GithubException(
                      f"\n\n**** ERROR: UNAUTHORIZED — INVALID OR EXPIRED GITHUB TOKEN : {e} ****\n\n"
                  ) from e

        # other exceptions under Github
        else:
            # Handle exceptions related to GitHub API issues
            raise GithubException(
                      f"\n\n**** ERROR: ERROR COMMUNICATING WITH GITHUB: {e} ****\n\n"
                  ) from e

    except Exception as e:
        # Handle other potential exceptions
        raise RuntimeError(
                  f"\n\n****ERROR: AN UNEXPECTED ERROR OCCURRED IN 'check_folder_exists' : {e} ****\n\n"
              )


def init_project(user: AuthenticatedUser, path_d: str) -> None:

    """
    Initialize the Project folder(CodewarsSolutions) and the project file
    (CodewarsAutomated.md).

    Args:
        user (AuthenticatedUser): The authenticated GitHub user.
        path_d (str): The path of {repo}/{folder}/{file}, defaults to
                    "Python"/"CodewarsSolutions"/"CodewarsAutomated.md".

    Returns:
        None.

    Raises:
    """
    
    # Get repo, folder name and file name from path
    repo_name, folder_name, file_name = path_d.split("/")

    # Getting the repo details
    repo = user.get_repo(repo_name)

    try:
        repo.create_file(
            path = f'{folder_name}/{file_name}',
            message = f"Create {path}",
            content = content,
            branch = "main" 
        )

    # Handle Github related exceptions
    except GithubException as e:
        raise GithubException(
                      f"\n\n**** ERROR: ERROR COMMUNICATING WITH GITHUB: {e} ****\n\n"
                  ) from e

    except Exception as e:
        # Handle other potential exceptions
        raise RuntimeError(
                  f"\n\n****ERROR: AN UNEXPECTED ERROR OCCURRED IN 'init_project' : {e} ****\n\n"
              )
