from selenium import webdriver
import os
import time
from time import sleep

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('/Users/othurm/Desktop/Insta-Bot/chromedriver')
        self.login()


    def login(self):
     self.driver.get('https://www.instagram.com/accounts/login/')
     sleep(2)
     self.driver.find_element_by_name("username").send_keys(self.username)
     self.driver.find_element_by_name("password").send_keys(self.password)
     self.driver.find_element_by_css_selector(
         "#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button").click()


if __name__ == '__main__':
    ig_bot = InstagramBot('upcomingstreetwearfashion', '3070349')






