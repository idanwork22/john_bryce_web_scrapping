"""
    Created by: Idan Chen
    Last modified: 09/01/2022
    Purpose: Do web scraping on a web page by using selenium
"""
from configuration import configuration
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def get_player_page_href(browser) -> list:
    """
    This function finds all the td elements with class id of 'primary text RosterRow_primaryCol__19xPQ'
    using xpath method, and returns the list of the elements.
    The function gets from every player his href because his value takes as to
    more detailed page with a lot of value.
    :param browser: the webdriver browser object
    :return: list of href
    """
    table = browser.find_element_by_class_name(configuration.get_table_class_id())
    return [tr.get_attribute("href") for tr in
            table.find_elements_by_xpath(configuration.get_player_href())]


def click_on_select_all_pages(browser, which_page='All'):
    """
    This function click on option button by his class
    and choose the option 'all' for getting all the players
    in one page, in one big table
    :param which_page: which page we want to extract data
    :param browser: the browser type 'webdriver.chrome.webdriver.WebDrive'
    :return: only update the screen
    """

    select = Select(browser.find_element_by_xpath(configuration.get_select_which_page()))
    select.select_by_visible_text(which_page)
    # put sleep for 1 second for let the page update before moving on
    time.sleep(1)


def get_basic_player_data(browser) -> dict:
    """
    This function gets browser and extract the basic player information:
    First name, last name, team name, shirt number and position.
    becuse of the architecture of the html page, we can't extract this
    data with the class id like we do with all the other player data
    :param browser: the web driver loaded with url
    :return: dict, key: fields name, value: the data
    """
    first_name = browser.find_element_by_xpath(configuration.get_first_name_xpath()).get_attribute("innerText")
    last_name = browser.find_element_by_xpath(configuration.get_last_name_xpath()).get_attribute("innerText")
    team_number_position = browser.find_element_by_xpath(configuration.get_team_number_position_xpath()) \
        .get_attribute("innerText")
    # the data is not clean. Example: Memphis Grizzlies | #4 | Center
    # we need to extract all the data we want and delete spaces
    team, number, position = [cell.strip() for cell in team_number_position.split("|")]
    number = number.replace("#", "")
    print({"FIRST NAME": first_name, "LAST NAME": last_name, "TEAM": team, "NUMBER": number, "POSITION": position})
    return {"FIRST NAME": first_name, "LAST NAME": last_name, "TEAM": team, "NUMBER": number, "POSITION": position}


def extract_data_from_player(href: str):
    """
    This function gets a href and creates new webdriver and
    extract all the necessary data from the page and then returns
    it to the user
    :param href: url type string
    :return: return list of player data
    """
    key_class = configuration.get_extra_information_field_mame_xpath()
    value_class = configuration.get_extra_information_value_xpath()
    browser = webdriver.Chrome(configuration.get_web_driver())
    browser.get(href)
    try:
        player_data = get_basic_player_data(browser)
        keys = [key.get_attribute("innerText") for key in browser.find_elements_by_class_name(key_class)]
        values = [value.get_attribute("innerText") for value in browser.find_elements_by_class_name(value_class)]
        more_player_information_dict = dict(zip(keys, values))
        player_data.update(more_player_information_dict)
        # print to the console
        for key, value in player_data.items():
            print(f'KEY:{key}\nVALUE: {value} \n ')
        browser.quit()
        # return only the values as a list, we don't need the key (use dict only for printing and debugging)
        return list(player_data.values())
    except Exception as e:
        print(e)
        return []
