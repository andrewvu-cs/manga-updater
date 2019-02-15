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

#I use mangadex.org as my choice of reading site
class mangabot(object):
    def __init__(self, mangas):
        self.manga_url = "https://www.mangadex.org"
        self.mangas = mangas
        #Srapes on google chrome 
        self.chromedriver = "/Users/andrewvu/Documents/chromedriver"
        self.myOptions = Options()
        self.driver = webdriver.Chrome(self.chromedriver, options = self.myOptions)
        self.driver.get(self.manga_url)
    

    def search_manga(self):
        #changes settings to find only English chapters on website
        self.change_settings(self.driver)

        directory_urls =[]
        latest_chapters = []
        chapter_urls = []

        for manga in self.mangas:
            search_input = self.driver.find_element_by_id("quick_search_input")
            search_input.send_keys(manga)

            time.sleep(3)

            search_button = self.driver.find_element_by_id("quick_search_button")
            search_button.click()

            time.sleep(3)

            #grabs directory url of specified manga
            manga_page = self.driver.find_element_by_link_text(manga)
            manga_page.click()
            directory_urls.append(self.driver.current_url)

            time.sleep(3)

            manga_chapter = self.driver.find_element_by_xpath('//*[@id="content"]/div[3]/div/div[2]/div/div/div[2]/a')
            manga_chapter.click()
            time.sleep(3)

            chapter = self.driver.find_element_by_id("jump-chapter").text
            print(chapter[0:15])
            latest_chapters.append(chapter[0:15])
            chapter_urls.append(self.driver.current_url)

        return directory_urls, latest_chapters, chapter_urls

    #Changes the settings to english
    def change_settings(self, driver):
        eng_settings = self.driver.find_element_by_xpath('//*[@id="homepage_cog"]/a/span')
        eng_settings.click()

        time.sleep(3)

        eng_settings_dropdown = self.driver.find_element_by_xpath('//*[@id="homepage_settings_form"]/div[2]/div/div/button/div/div/div')
        eng_settings_dropdown.click()

        time.sleep(3)

        eng_lang = self.driver.find_element_by_xpath('//*[@id="homepage_settings_form"]/div[2]/div/div/div/div[2]/ul/li[11]/a')
        eng_lang.click()
        time.sleep(3)

        save_button = self.driver.find_element_by_xpath('//*[@id="homepage_settings_button"]')
        save_button.click()
        time.sleep(3)

       


# search_items("Solo Leveling")