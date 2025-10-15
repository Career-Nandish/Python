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


def codewars_token_session(
        url: str = "https://www.codewars.com/users/sign_in"
    ) -> tuple[requests.Session, str]:
    
    """
    Fetch the Codewars login page and extract CSRF token.

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
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        }

        # Fetch the login page
        response = session.get(url, headers = headers)

        # raise HTTPError if not 200 OK
        response.raise_for_status()  

        # Parse HTML to extract CSRF token
        soup = BeautifulSoup(response.text, "html.parser")
        csrf_token_tag = soup.find("meta", attrs = {"name": "csrf-token"})

        if not csrf_token_tag or not csrf_token_tag.get("content"):
            raise RuntimeError("Unable to locate CSRF token on sign-in page.")

        csrf_token = csrf_token_tag["content"]

        print("\n==== CSRF Token Extracted Successfully ====")
        return session, csrf_token

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Network or request error while fetching sign-in page: {e}") from e

    except Exception as e:
        raise RuntimeError(f"Unexpected error in fetch_signin_page: {e}") from e


def codewars_login(
    creds,
    username,
    default_driver=webdriver.Chrome,
    main_url="https://www.codewars.com/users/sign_in"
    ):
    tabs = {}
    driver = default_driver()
    driver.get(main_url)
    tabs["cw_main"] = driver.current_window_handle
    uname = driver.find_element(By.ID, "user_email")
    uname.send_keys(creds["email"])
    time.sleep(0.5)
    pwd = driver.find_element(By.ID, "user_password")
    pwd.send_keys(creds["password"])
    time.sleep(0.5)
    # Find the button by its type attribute
    submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    time.sleep(0.5)
    submit_button.click()
    time.sleep(2)
    driver.switch_to.new_window("tab")
    driver.get(f"https://www.codewars.com/users/{username}/completed_solutions")
    tabs["cw_solutions"] = driver.current_window_handle
    time.sleep(1)
    driver.switch_to.window(tabs["cw_main"])
    driver.close()
    driver.switch_to.window(tabs["cw_solutions"])
    time.sleep(1)
    driver.quit()