from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Crawler import initState
from logger import LoggerHandler
from FormExtractor import getFormFieldValue
import time
import logging
import logging.config


class Globals:
    '''
    Contains initialization of all the global variables
    '''

    def __init__(self):
        self.formFieldValues = getFormFieldValue("submit_form2.html")
        self.bannedUrls = []


def main():
    '''
    crawls the demo website http://127.0.0.1:81/login/login.php
    with login credentials
    email = vinaysharma@gmail
    password = vinaykool
    '''
    logger = LoggerHandler(__name__)
    globalVariables = Globals()

    # add banned Urls
    # globalVariables.bannedUrls.append("http://127.0.0.1:81/login/profile.html")

    #driver = webdriver.PhantomJS()
    driver = webdriver.Chrome()
    logger.info("FireFox is Launched")
    driver.get("http://127.0.0.1:81/login/login.php")
    assert "Login Form" in driver.title

    email = driver.find_element_by_name("e-mail")
    email.send_keys("vinaysharma@gmail")
    password = driver.find_element_by_name("Password")
    password.send_keys("vinaykool")
    password.send_keys(Keys.RETURN)
    # time.sleep(5)

    # print driver.page_source
    print driver.current_url, driver.title

    # Store the values of the Form to be filled
    #formValues = getFormFieldValue("submit_form2.html")

    # move the controller to Initiate Crawler Activity
    logger.info("Initiating the Crawler")
    initState(
        driver.page_source,
        driver.current_url,
        driver.title,
        driver,
        globalVariables)

    #assert "Welcome, " in driver.page_source
    driver.close()


if __name__ == '__main__':
    main()
