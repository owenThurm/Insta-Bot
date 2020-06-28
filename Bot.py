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


    def search(self, searchText):
        sleep(2)
        self.driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > div").click()
        self.driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input").send_keys(searchText)
        sleep(3)
        self.driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > div:nth-child(4) > div.drKGC > div > a:nth-child(1)").click()


    def getFollower(self, followerNum):
        sleep(2)
        self.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(2) > a").click()
        sleep(3)

        #Failed Attempts to get the followers
        print(self.driver.find_elements_by_class_name("FPmhX notranslate  _0imsa "))
        self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(2) > div > div.Igw0E.IwRSH.YBx95.vwCYk").find_element_by_class_name("FPmhX notranslate  _0imsa ").click()

    #def comment(self, commentText):
    #    sleep(2)
    #    self.driver.find_element_by_css_selector().click


if __name__ == '__main__':
    ig_bot = InstagramBot('upcomingstreetwearfashion', '3070349')
    ig_bot.search("movingtomars")
    ig_bot.getFollower(1)






