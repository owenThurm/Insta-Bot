from selenium import webdriver
import os
import time

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome('/Users/othurm/Desktop/Insta-Bot/chromedriver')
        login()


def login(self):
    self.driver.get('https://www.instagram.com/accounts/login/')
    self.driver.find_element_by_name('username').send_keys(self.username)
    self.driver.find_element_by_name('password').send_keys(self.password)
    


if __name__ == '__main__':
    ig_bot = InstagramBot('upcomingstreetwearfashion', 'MagicJohnson32!')






