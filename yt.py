from selenium import webdriver
from selenium.webdriver.common.by import By


def get_link(song):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    search_query = song.split()
    print(search_query)

    final_query = ""

    for word in search_query:
        final_query += word + "+"

    driver.get(
        'https://www.youtube.com/results?search_query={}'.format(final_query))
    select = driver.find_element(
        By.CSS_SELECTOR, 'div#contents ytd-item-section-renderer>div#contents a#thumbnail')
    return select.get_attribute('href')
