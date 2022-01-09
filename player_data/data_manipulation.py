import pandas
import pandas as pd
from datetime import datetime


def create_player_data_frame() -> pandas.DataFrame:
    """
    This function creates pandas.DataFrame with specific column names and return it
    :return: pandas.DataFrame object
    """
    return pd.DataFrame(columns=["FIRST NAME", "LAST NAME", "TEAM", "NUMBER", "POSITION",
                                 "HEIGHT(METER)", "WEIGHT(KG)", "COUNTRY", "LAST ATTENDED", "AGE(YEARS)",
                                 "BIRTHDATE", "DRAFT", "EXPERIENCE(YEARS)"])


def casting_birthday_to_date(birthday: str):
    """
    This function gets string birthday and parse it to date.
    Example: September 19, 1999 -> 9/19/1999
    We need to extract from the month only the 3 FIRST LETTERS (because of the format)
    and datetime.strptime to parsing the string to date
    :param birthday: player birthday type string
    :return:
    """
    # Example: 'March 5, 2000' -> 'Mar 5, 2000'
    birthday = birthday[0: 3:] + birthday[birthday.find(" ")::]
    # casting from string to time
    return datetime.strptime(birthday, '%b %d, %Y').date()


def clean_and_parsing_data(player_data_frame: pandas.DataFrame) -> pandas.DataFrame:
    """
    This function gets pandas.DataFrame object and clean and organize the following columns:
    - HEIGHT: take only the Meter size. Example: 6\'8" (2.03m) -> 2.03
    - WEIGHT: take only the Kilo size. Example: 225lb (102kg) -> 102
    - AGE: delete "AGE" string. Example: September 19, 1999 -> 9/19/1999
    - BIRTHDATE: parse the string to date. Example: September 19, 1999 -> 9/19/1999
    :param player_data_frame: the original pandas.DataFrame before clean up
    :return: return clean and organize pandas.DataFrame object
    """
    # cleaning the data
    player_data_frame["HEIGHT(METER)"] = player_data_frame["HEIGHT(METER)"].apply(lambda cell: cell.split("(")[1][:-2])
    player_data_frame["WEIGHT(KG)"] = player_data_frame["WEIGHT(KG)"].apply(lambda cell: cell.split("(")[1][:-3])
    player_data_frame["AGE(YEARS)"] = player_data_frame["AGE(YEARS)"].apply(lambda cell: cell.split(" ")[0])
    player_data_frame["BIRTHDATE"] = player_data_frame["BIRTHDATE"].apply(casting_birthday_to_date)
    player_data_frame["EXPERIENCE(YEARS)"] = player_data_frame["EXPERIENCE(YEARS)"].apply(
        lambda cell: 0 if cell == "Rookie" else cell.split(" ")[0])

    # casting the types
    player_data_frame["HEIGHT(METER)"] = player_data_frame["HEIGHT(METER)"].astype(float)
    player_data_frame["WEIGHT(KG)"] = player_data_frame["WEIGHT(KG)"].astype(float)
    player_data_frame["AGE(YEARS)"] = player_data_frame["AGE(YEARS)"].astype(int)
    player_data_frame["EXPERIENCE(YEARS)"] = player_data_frame["EXPERIENCE(YEARS)"].astype(int)
    player_data_frame['BIRTHDATE'] = pd.to_datetime(player_data_frame['BIRTHDATE'], format='%Y-%m-%d')

    return player_data_frame
