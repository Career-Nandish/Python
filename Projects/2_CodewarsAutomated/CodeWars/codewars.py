import os
import time
import random
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from typing import Type, Union

def load_cw_credentials() -> tuple[str, str]:
    
    """
    Loads EMAIL, PASSWORD from the ENVIRONMENT VARIABLES.

    Returns:
        tuple(str, str): tuple of EMAIL and PASSWORD.

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
        
        return cw_email, cw_passwd
    
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
                
                wait_time = delay * (2 ** (attempt - 1)) + random.uniform(0, 3)

                try:
                    # Calling the decorated function
                    return func(*args, **kwargs)
                
                # Catching requests related exceptions
                except retry_exceptions as e:
                    print(
                        f"\n\n**** ERROR: '@{func.__name__}' - ATTEMPT {attempt} FAILED: {e}. RETRYING IN {delay}S... ****\n\n"
                    )

                    # Display for user
                    print(f"\n==== Retrying '{func.__name__}' in {wait_time:.1f}s... ====")

                    # Slumber time
                    time.sleep(wait_time)
                
            # Raising if all attempts are exhausted
            raise RuntimeError(
                      f"\n\n**** ERROR: ALL {max_attempts} ATTEMPTS FAILED FOR '@{func.__name__}' ****\n\n"
                  )
        
        return wrapper
    
    return decorator


@retry()
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
    print("\n==== Fetching CODEWARS CSRF Token ====")
    
    # Start persistent session
    session = requests.Session()
    
    # Include header to seem genuine
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/117.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                  "image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Origin": "https://www.codewars.com"
    }

    # Connect to the URL
    response = session.get(url, headers=headers)
    
    # Retries network errors via decorator
    response.raise_for_status()  

    # Finding CSRF token 
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token_tag = soup.find("meta", attrs={"name": "csrf-token"})

    # Unable to find CSRF token
    if not csrf_token_tag or not csrf_token_tag.get("content"):
        raise RuntimeError(
                  "\n\n****ERROR: CSRF TOKEN NOT FOUND ON CODEWARS SIGN-IN PAGE ****\n\n"
              )

    # Extract the token
    csrf_token = csrf_token_tag["content"]

    # Display for users
    print("\n==== CODEWARS CSRF Token Extracted Successfully ====")

    return session, csrf_token

@retry()
def login_cw(
        session: requests.Session, 
        email: str, 
        password: str, 
        csrf_token: str,
        login_url: str = "https://www.codewars.com/users/sign_in"
    ) -> bool:
    
    """
    Attempts to log in to Codewars using a provided session, credentials,
    and CSRF token. Retries automatically for network errors.

    Args:
        session (requests.Session): Active HTTP session with headers set.
        email (str): User's Codewars account email.
        password (str): User's Codewars account password.
        csrf_token (str): CSRF token extracted from the sign-in page.
        login_url (str): Codewars sign-in endpoint. Defaults to 
                         "https://www.codewars.com/users/sign_in"

    Returns:
        bool: True if login succeeded, False if credentials or CSRF token failed.

    Raises:
        RuntimeError: If login page structure changes or expected markers are missing.
    """

    print("\n==== Attempting Login to CODEWARS ====")

    # Build form payload
    payload = {
        "user[email]": email,
        "user[password]": password,
        "authenticity_token": csrf_token
    }

    # Include referer to simulate normal behaviour
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/117.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                  "image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Origin": "https://www.codewars.com",
        "Referer": "https://www.codewars.com/users/sign_in"
    }

    # login post the payload
    response = session.post(login_url, data = payload, headers = headers, timeout = 10)
    response.raise_for_status()

    # Parse the response to verify login
    soup = BeautifulSoup(response.text, "html.parser")

    # Looking for ways to confirm the success of loggin-in
    dashboard_body = soup.find("body", id = "dashboard")
    button_sign_out = soup.find("a", class_ = "js-sign-out")
    a_username = soup.find("a", id = "header_profile_link")["href"]

    # username extract
    cw_username = a_username.split("/")[-1]

    # Login check using HTML tags
    if dashboard_body and button_sign_out and a_username:

        # display for user
        print(f"\n==== Successfully Logged in to CODEWARS as '{cw_username}' ====")
        return session, cw_username
    
    # Invalid credentials
    elif "Invalid Email or password" in response.text:
        raise RuntimeError(
                  "\n\n**** ERROR: LOGIN FAILED DUE TO INVALID CREDENTIALS ****\n\n"
              )
    
    # Token invalid/expired
    elif "authenticity_token" in response.text:
        raise RuntimeError(
                  "\n\n**** ERROR: LOGIN FAILED DUE TO INVALID OR EXPIRED CSRF TOKEN ****\n\n"
              )

    # Other potential error
    else:
        raise RuntimeError(
                  "\n\n**** ERROR: UNKNOWN ERROR OCCURRED IN 'login_cw'"
              )


def download_solutions():pass