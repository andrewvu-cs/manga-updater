import requests
# Beautiful soup can extract data from html pages.
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import re
import time

# class MangaBot(object):
#     def __init__(self, items):
        # self.manga_url = "https://www.mangadex.org"
        # self.items = items
        # self.
def search_items(item):
    manga_url = "https://www.mangadex.org"
    chromedriver = "/Users/andrewvu/Documents/chromedriver"
    myOptions = Options()
    driver = webdriver.Chrome(chromedriver, options = myOptions)

    driver.get(manga_url)
    
    change_settings(driver)

    search_input = driver.find_element_by_id("quick_search_input")
    search_input.send_keys(item)

    time.sleep(3)

    search_button = driver.find_element_by_id("quick_search_button")
    search_button.click()

    time.sleep(3)

    manga_page = driver.find_element_by_link_text(item)
    manga_page.click()

    time.sleep(3)

    manga_chapter = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div/div[2]/div/div/div[2]/a')
    manga_chapter.click()
    time.sleep(3)

    chapter = driver.find_element_by_id("jump-chapter").text
    print(chapter[0:6])
    latest_chapter = chapter[0:6]

    url = driver.current_url
    print(url)

def change_settings(driver):
    eng_settings = driver.find_element_by_xpath('//*[@id="homepage_cog"]/a/span')
    eng_settings.click()

    time.sleep(3)

    eng_settings_dropdown = driver.find_element_by_xpath('//*[@id="homepage_settings_form"]/div[2]/div/div/button/div/div/div')
    eng_settings_dropdown.click()

    time.sleep(3)

    eng_lang = driver.find_element_by_xpath('//*[@id="homepage_settings_form"]/div[2]/div/div/div/div[2]/ul/li[11]/a')
    eng_lang.click()
    time.sleep(3)

    save_button = driver.find_element_by_xpath('//*[@id="homepage_settings_button"]')
    save_button.click()
    time.sleep(3)


search_items("Solo Leveling")