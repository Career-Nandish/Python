import os
import time
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from typing import Type, Union



def load_cw_credentials() -> dict:
    
    """
    Loads EMAIL, PASSWORD from the ENVIRONMENT VARIABLES.

    Returns:
        dict: dictionary of EMAIL and PASSWORD.

    Raises:
    EnvironmentError : if variable hasn't been set or it's missing.
    RuntimeError: Potential runtime errors.
    
    """

    # Display for user
    print("\n==== Loading credentials for CODEWARS ====")
    
    try:
        # Load Credentials from ENVIRONMENT VARIABLES
        cw_email = os.environ["CODEWARS_EMAIL"]
        cw_passwd = os.environ["CODEWARS_PASSWORD"]

        # Display for user
        print("\n==== Done Loading Credentials for CODEWARS ====")
        
        return {"email" : cw_email, "password" : cw_passwd}
    
    # If not variable not found
    except KeyError as e:
        raise EnvironmentError("\n\n**** ERROR: ONE OR MORE ENVIRONMENT VARIABLE(s) IS MISSING! ****\n\n")

    # Other potential runtime errors
    except Exception as e:
        raise RuntimeError(
                  f"\n\n**** AN UNKNOWN ERROR HAS OCCURRED IN load_cw_credentials : {e} ****\n\n"
              ) from e


def retry(
        max_attempts:int = 5, 
        delay:int|float = 15, 
        retry_exceptions = (
            requests.exceptions.RequestException,
        )
    ):
    
    """
    Decorator to retry a function multiple times upon encountering 
    specified exceptions.

    This decorator wraps a function and automatically retries it if 
    it raises an exception listed in `retry_exceptions`. 
    It also retries for unexpected exceptions, logging each attempt, 
    until the maximum number of attempts is reached.

    Args:
        max_attempts(int): Maximum number of times to attempt the function. 
                           Default is 5.
        delay(int|float): Delay in seconds between retries. 
                          Default is 15 seconds.
        retry_exceptions(tuple): A tuple of exception classes to retry on. 
                                 Default is `requests.exceptions.RequestException`.

    Returns:
        Callable: A wrapped function that retries on failure.

    Raises:
        RuntimeError: If all attempts fail, the last exception is raised as a 
                      RuntimeError.
    """
    # Decorator
    def decorator(func):

        # Wrapper
        def wrapper(*args, **kwargs):

            # Looping till maximum attempts
            for attempt in range(1, max_attempts + 1):
                
                try:
                    # Calling the decorated function
                    return func(*args, **kwargs)
                
                # Catching requests related exceptions
                except retry_exceptions as e:
                    print(
                        f"\n\n **** ERROR: ATTEMPT {attempt} FAILED: {e}. RETRYING IN {delay}S... ****\n\n"
                    )
                    # Slumber time
                    time.sleep(delay)
                
                # Catching other potential errors
                except Exception as e:
                    print(
                        f"\n\n **** ERROR: ATTEMPT {attempt} ENCOUNTERED UNEXPECTED ERROR: {e}. RETRYING IN {delay}S... ****\n\n"
                    )
                    # Slumber time
                    time.sleep(delay)
            
            # Raising if all attempts are exhausted
            raise RuntimeError(
                      f"\n\n **** ERROR: ALL {max_attempts} ATTEMPTS FAILED FOR {func.__name__}. ****\n\n"
                  )
        
        return wrapper
    
    return decorator


@retry(retry_exceptions = (requests.exceptions.RequestException, KeyError, IndexError))
def start_cw_session(
        url: str = "https://www.codewars.com/users/sign_in"
    ) -> tuple[requests.Session, str]:
    
    """
    Stars the session(pesistent) and extract CSRF token.

    Args:
        url (str): URL of the Codewars sign-in page. Defaults to
                   "https://www.codewars.com/users/sign_in"

    Returns:
        tuple[requests.Session, str]: A tuple containing:
            - The active `requests.Session` object (to preserve cookies for login).
            - The extracted CSRF token string.

    Raises:
        RuntimeError: If the page cannot be fetched or the token is missing.
    """

    # Display for user
    print("\n==== Fetching Codewars CSRF Token ====")
    
    try:
        # Create a persistent session
        session = requests.Session()

        # Add browser-like headers
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept": "*/*"
        }

        # Fetch the login page
        response = session.get(url, headers = headers)

        # raise HTTPError if not 200 OK
        response.raise_for_status()  

        # Parse HTML to extract CSRF token
        soup = BeautifulSoup(response.text, "html.parser")
        csrf_token_tag = soup.find("meta", attrs = {"name": "csrf-token"})

        if not csrf_token_tag or not csrf_token_tag.get("content"):
            raise RuntimeError(
                      f"\n\n**** ERROR: UNABLE TO LOCATE CSRF TOKEN ON SIGN-IN PAGE. ****\n\n"
                  )

        # Extracting only token from the tag
        csrf_token = csrf_token_tag["content"]

        # Display for user
        print("\n==== CSRF Token Extracted Successfully ====")
        
        return session, csrf_token

    except requests.exceptions.RequestException as e:
        raise RuntimeError(
                  f"\n\n**** ERROR: NETWORK OR REQUEST ERROR WHILE FETCHING SIGN-IN PAGE: {e} ****\n\n"
              ) from e

    except Exception as e:
        raise RuntimeError(
                  f"\n\n**** ERROR: Unexpected error in 'start_cw_session': {e} ****\n\n"
              ) from e