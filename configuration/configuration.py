"""
    Created by: Idan Chen
    Last modified: 09/01/2022
    Purpose: Connect to config.ini file and extract values
"""
from configparser import ConfigParser
import os


def get_config():
    config = ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
    return config


# web driver
def get_web_driver():
    config = get_config()
    return config.get("web_driver", "web_driver_location")


# url
def get_home_url():
    config = get_config()
    return config.get("url", "home_url")


# table page
def get_table_class_id():
    config = get_config()
    return config.get("table_page", "table_class_id")


def get_next_page_button_xpath():
    config = get_config()
    return config.get("table_page", "next_page_xpath")


def get_player_href():
    config = get_config()
    return config.get("table_page", "player_href")


def get_select_which_page():
    config = get_config()
    return config.get("table_page", "select_page_xpath")


# player page
def get_first_name_xpath():
    config = get_config()
    return config.get("player_page", "first_name_xpath")


def get_last_name_xpath():
    config = get_config()
    return config.get("player_page", "last_name_xpath")


def get_team_number_position_xpath():
    config = get_config()
    return config.get("player_page", "team_number_position_xpath")


def get_extra_information_field_mame_xpath():
    config = get_config()
    return config.get("player_page", "extra_information_field_mame_xpath")


def get_extra_information_value_xpath():
    config = get_config()
    return config.get("player_page", "extra_information_value_xpath")
