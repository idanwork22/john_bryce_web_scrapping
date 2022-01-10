"""
    Created by: Idan Chen
    Date: 08/01/2022
    This project takes the  status of each NBA player,
    cleans the data and writes it to csv file.

    The idea is to go to "https://www.nba.com/players" url where all the players are located
    in some sort of table, get there class to get list of elements,
    and get the href of each element for going to second page where all the important data
    is located (points, rebound, assist, height and exc...)
"""
from player_data import data_manipulation as data
from web_scrapping import scraping
from web_scrapping import web_driver

"""
    IGAL - DONT FORGET TO CHANGE YOU WEBDRIVER LOCATION AT 'CONFIG.INI' !!!
"""


def main():
    # create pandas.DataFrame object for saving all players data
    players_dataframe = data.create_player_data_frame()
    # create connection to the webdriver and put the url inside the browser
    browser = web_driver.load_web_driver()
    # click on select all for seeing all the players in the table -> IF YOU WANT ALL PAGES: which_page = 'All'
    scraping.click_on_select_all_pages(browser=browser, which_page='1')

    # run on every player in the list
    for href_player in scraping.get_player_page_href(browser):
        # extract the data
        player_dict_data = scraping.extract_data_from_player(href_player)
        if player_dict_data:
            players_dataframe.loc[len(players_dataframe)] = player_dict_data
    players_dataframe = data.clean_and_parsing_data(players_dataframe)
    players_dataframe.to_csv("NBA players data.csv", index=False, encoding='utf-8')
    print("finish")
    browser.quit()


if __name__ == '__main__':
    main()
