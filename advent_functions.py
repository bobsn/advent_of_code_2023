import os
import requests


def get_text(current_day: int)-> list:
    """Reads the file of the day, and returns it as a list.

    Args:
        current_day (int): Day of the advent.

    Returns:
        list: List containing the input of the day.
    """
    filename = 'Day_' + str(current_day) + '.txt'
    with open(os.path.join('input', filename)) as f:
        text = f.readlines()

    text = [line.replace('\n', '') for line in text]
    return text


def get_lines(current_day: int):
    filename = 'Day_' + str(current_day) + '.txt'
    with open(os.path.join('input', filename)) as f:
        for line in f: 
            yield line.replace('\n', '')           


def scrape_info_from_website(day):
    url = f'https://adventofcode.com/2023/day/{day}/input'
    request = requests.get(url) 
    # TODO: Find out how to log in
    return request
