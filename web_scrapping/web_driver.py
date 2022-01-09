"""
    Created by: Idan Chen
    Last modified: 09/01/2022
    Purpose: Responsible to all the webdriver setup
"""
from selenium import webdriver
from configuration import configuration


def load_web_driver():
    """
    This function create new webdriver and put url to load the browser
    :return: returns new loaded webdriver
    """
    browser = webdriver.Chrome(configuration.get_web_driver())
    # put the url inside the browser
    browser.get(configuration.get_home_url())
    return browser
