import os
import time
import random
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from typing import Type, Union

# Colors for the banners for difficulty levels of the problem questions
BANNERS = {
              "1": "8A2BE2",
              "2": "darkblue",
              "3": "blue",
              "4": "skyblue",
              "5": "important",
              "6": "FFFF00",
              "7": "white",
              "8": "lightgrey",
          }

BASE_URL = "https://www.codewars.com"

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

    # Headers
    headers = {
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/117.0.0.0 Safari/537.36",
              "Accept": "text/html, */*; q=0.01",
              "Accept-Language": "en-US,en;q=0.9",
              "Connection": "keep-alive",
              "Origin": "https://www.codewars.com"
          }

    # Display for user
    print("\n==== Fetching CODEWARS CSRF Token ====")
    
    # Start persistent session
    session = requests.Session()    

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


    # Header
    headers = {
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/117.0.0.0 Safari/537.36",
              "Accept": "text/html, */*; q=0.01",
              "Accept-Language": "en-US,en;q=0.9",
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

@retry()
def download_cw_solutions(
    cw_session: requests.Session,
    cw_username: str,
    cw_token: str,
    gContent: str | None,
    first_run: bool
) -> list[dict] | None:
    """
    Download all completed Codewars solutions for a given user 
    using XHR pagination.

    This function fetches solutions page by page (simulating scrolling),
    parses them with BeautifulSoup, and collects all kata solutions 
    into a list.

    Args:
        cw_session (requests.Session): Authenticated session for Codewars.
        cw_username (str): Codewars username.
        cw_token (str): Codewars session token or API token.
        gContent (str | None): GitHub content flag.
        first_run (bool): True if this is the first run (controls setup behavior).

    Returns:
        list[dict] | None: A list of parsed solutions, or None if no solutions found.

    Raises:
        RuntimeError: If parsing or unexpected structure errors occur.
    """
    
    # Headers for GET
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/117.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Origin": "https://www.codewars.com",
        "Referer": "https://www.codewars.com/dashboard",
        "X-Requested-With": "XMLHttpRequest"
    }

    # If Github content is found, scrap parts of the solutions
    # not all of them
    if gContent:
        print("\n==== Checking GITHUB content ====")
        return None

    # If no Github content, first run and download all
    print("\n==== Downloading CODEWARS solutions ====")

    solutions = []
    page = 0

    try:
        while True:
            # Different URLs based on pages
            download_url = (
                f"https://www.codewars.com/users/{cw_username}/completed_solutions"
                if page == 0
                else f"https://www.codewars.com/users/{cw_username}/completed_solutions?page={page}"
            )

            print(f"\n== Fetching page {page}: {download_url} ==")

            # Getting data from the url
            response = cw_session.get(download_url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            # If there's no solutions from user
            if not soup.find("div", class_="list-item-solutions"):
                print(f"\n==== CODEWARS user '{cw_username}' has no more solutions ====")
                break

            # Parse the solutions from current page
            parsed = parse_cw_solutions(cw_session, soup, headers)
            
            if not parsed:
                print(f"\n** Warning: No valid solutions parsed from page {page} **\n")
            else:
                solutions.extend(parsed)

            # Check if more pages exist
            if soup.find("div", class_="js-infinite-marker"):
                page += 1
                time.sleep(5)
            else:
                print("\n== No more pages left ==")
                break

    except Exception as e:
        raise RuntimeError(
            "\n\n**** ERROR : UNEXPECTED ERROR OCCURRED IN 'download_cw_solutions' ****\n\n"
        ) from e

    # Display for user
    print("\n==== Done downloading CODEWARS solutions ====")
    return solutions


def parse_cw_solutions(
        cw_session: requests.Session, 
        soup: BeautifulSoup,
        headers: dict
    ) -> list[dict]:
    """
    Parse a BeautifulSoup object to extract Codewars kata details.

    Args:
        cw_session (requests.Session): Authenticated session for Codewars.
        soup (BeautifulSoup): Parsed HTML soup from the Codewars page.
        headers (dict): A dict of headers.

    Returns:
        list[dict]: Parsed kata solution info.
    """

    # Empty results list
    results = []

    # Selecting the solutions div
    solution_divs = soup.select("div.list-item-solutions")

    # if no such div is found throw an error
    if not solution_divs:
        raise RuntimeError("\n\n**** NO SOLUTIONS FOUND(no div called list-item-solutions) IN PARSED SOUP OBJECT ****\n\n")

    # Looping through all the divs
    for div in solution_divs:
        try:

            # Difficulty
            diff_tag = div.select_one(".inner-small-hex span")
            difficulty = diff_tag.get_text(strip=True) if diff_tag else None

            # Kata URL
            a_tag = div.select_one(".item-title a")
            kata_title = a_tag.text.strip() if a_tag else None
            kata_url = f"{BASE_URL}{a_tag['href']}" if a_tag and a_tag.has_attr("href") else None

            # Language
            lang_tag = div.find("h6")
            language = lang_tag.text.strip(":") if lang_tag else None

            # Fetch kata description
            kata_desc, kata_keywords = fetch_cw_kata_description(
                                           cw_session, kata_url, headers, language
                                       )

            print(kata_desc, kata_keywords)

            # Code
            code_tag = div.select_one("code.mb-5px[data-language]")
            code = code_tag.text if code_tag else None

            # Submission time
            time_tag = div.select_one("time-ago")
            date = time_tag["datetime"] if time_tag and time_tag.has_attr("datetime") else None

            # If title and code is not found skip the solution,
            if not (kata_title and code):
                print("\n** Warning: Skipping incomplete solution (missing title or code) **\n")
                continue

            results.append({
                "title": kata_title,
                "description": kata_desc,
                "url": kata_url,
                "difficulty": difficulty,
                "language": language,
                "code": code,
                "date": date
            })

            time.sleep(5)

        except Exception as e:
            raise RuntimeError(f"\n\n**** ERROR PARSING <div class='list-item-solutions'> in 'parse_cw_solutions' ****\n\n")

    return results


@retry()
def fetch_cw_kata_description(
        cw_session: requests.Session,
        kata_url: str,
        headers: dict,
        language: str
    ) -> str:

    try:    

        # kata url loads content dynamically, so have to 
        # fetch the data from train page
        train_url = f"{kata_url}/train/{language.lower()}"

        # Getting data from the url
        response = cw_session.get(train_url, headers = headers)
        response.raise_for_status()

        print(response.text)

        # parse the data
        soup = BeautifulSoup(response.text, "html.parser")

        # Description and Keyword
        desc_div = soup.find("div", id = "description")
        keyword_div = soup.find_all("div", class_ = "keyword-tag")
        keywords = []
        
        for div in keyword_div:
            keywords.append(div.text)

        return desc_div.decode_contents(), ", ".join(keywords)

    
    except Exception as e:
        raise RuntimeError(
            f"\n\n**** ERROR FETCHING KATA DESCRIPTION in 'fetch_cw_kata_description' ****\n\n"
        )
