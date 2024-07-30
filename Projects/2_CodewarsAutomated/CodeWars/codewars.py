import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from selenium.common.exceptions import WebDriverException
from typing import Type, Union
import shutil
from pathlib import Path


def get_webdriver() -> Union[
                           Type[webdriver.Chrome], 
                           Type[webdriver.Firefox], 
                           Type[webdriver.Edge]
                       ]:
    
    """
    Get an available web driver on the system.

    This function checks the system PATH for the presence of browser 
    drivers (Chrome, Firefox, Edge) and returns the WebDriver class of 
    an available browser.

    Returns:
        Type[webdriver.WebDriver]: The WebDriver class of the available 
                                   browser (e.g., webdriver.Chrome).

    Raises:
        ValueError: If no compatible drivers are found.
        Exception: For any other unexpected errors.
    """
    
    try:
        # Define a dictionary mapping browser names to their respective driver 
        # executable names, add yours here!
        drivers = {
            webdriver.Chrome: "chromedriver",
            webdriver.Firefox: "geckodriver",
            webdriver.Edge: "msedgedriver",
        }

        # Create a dictionary of available drivers by checking if they exist 
        # in the system PATH using shutils
        available_drivers = {
            browser: driver for browser, driver in drivers.items() \
                if shutil.which(driver) is not None
        }
        
        # If no drivers are found, raise an error
        if not available_drivers:
            raise ValueError

        # else return a driver
        return next(iter(available_drivers))

    except ValueError as e:
        print("\n\n**** NO COMPATIBLE DRIVERS FOUND in get_webdriver. ****\n\n")
        raise

    except Exception as e:
        print(f"""\n\n****AN UNEXPECTED ERROR OCCURRED IN get_webdriver
            ****: {e}\n\n""")
        raise

def load_cw_credentials() -> str:
    
    print("\n==== Loading credentials for CODEWARS ====")
    cred_path = Path.cwd() / "CodeWars" / "credentials" / "credentials.txt"

    try:
        # Load credentials from the file
        with cred_path.open("r") as file:
            credentials = json.load(file)

        print("\n==== DONE Loading Credentials CODEWARS ====")
        # Return the username and password
        return credentials["email"], credentials["password"]
    
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

def codewars_navigate(
    selected_driver,
    creds, 
    main_url="https://www.codewars.com/users/sign_in",
    solutions_url=""
    ):
    tabs = {}
    driver = webdriver.Chrome()
    driver.get(main_url)
    tabs["codewars_login"] = driver.current_window_handle
    uname = driver.find_element(By.ID, "user_email")
    uname.send_keys(creds["email"])
    pwd = driver.find_element(By.ID, "user_password")
    pwd.send_keys(creds[password])
    time.sleep(2)
    driver.quit()