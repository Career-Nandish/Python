import time
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from selenium.common.exceptions import WebDriverException
from typing import Type, Union
import shutil
from pathlib import Path


def load_cw_credentials() -> str:
    
    print("\n==== Loading credentials for CODEWARS ====")
    cred_path = Path.cwd() / "CodeWars" / "credentials" / "credentials.txt"

    try:
        # Load credentials from the file
        with cred_path.open("r") as file:
            credentials = json.load(file)

        print("\n==== DONE Loading Credentials CODEWARS ====")
        # Return the username and password
        return credentials
    
    except FileNotFoundError as error:
        print(f"""\n\n**** Error: The credentials file does not exist, 
            {error} ****\n\n""")
    
    except json.JSONDecodeError as error:
        print(f"""\n\n**** Error: The credentials file is not a valid JSON, 
            {error} ****\n\n""")

    except KeyError as error:
        print(f"""\n\n**** Error: The credentials file does not contain the 
            key(s) 'email' or 'password', {error} ****\n\n""")

    except Exception as error:
        print(f"""\n\n**** AN UNKNOWN ERROR HAS OCCURRED in load_cw_credentials, 
            {error}****\n\n""")


def get_url_status(url: str) -> int:
    
    """
    Retrieve the HTTP status code for a given URL.

    This function makes an HTTP GET request to the specified URL and returns the 
    status code of the response. If the request fails or an error occurs, it 
    raises an exception and prints an appropriate error message.

    Args:
        url (str): The URL to get the status of.

    Returns:
        int: The HTTP status code of the URL response.

    Raises:
        requests.RequestException: If a network-related error occurs during the 
                                   request.
        Exception: For any other unexpected errors that may occur.
    """
   
    try:
        response = requests.get(url)
        return response.status_code
    
    except requests.RequestException as error:
        print(f"AN RequestException OCCURRED in get_url_status: {error}")
        raise

    except Exception as error:
        print(f"""\n\n**** AN UNKNOWN ERROR HAS OCCURRED in get_url_status, 
            {error}****\n\n""")


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