from selenium import webdriver
import os
import time
from time import sleep
from utility_methods import randomCommentText
from utility_methods import randomCommentTextMain
from datetime import datetime
import random
import math


introText = u'''Hey what’s good, hope you’re doing well during these hard times!
At Genuine Aesthetic we’re all about supporting the streets! We work with homeless shelters to feed and clothe the homeless and displaced who have been cruelly neglected during these difficult times.
Let us know what you think about the brand \u270C If you like our gear and would like to support our cause give us a follow and share the brand! It goes a long way to support our mission! \u2764'''


class InstagramBot:

    def __init__(self, username, password, brand, is_main):
        self.username = username
        self.password = password
        self.brand = brand
        self.is_main = is_main
        #self.previousComments = open("Instagram_Comment_Names", "a")
        #self.previousCommentsUsernames = open("Instagram_Comment_Names", "r").read().split(" ")
        self.driver = webdriver.Chrome()
        sleep(random.random() * 3 + 3)
        self.login()
        sleep(random.random() * 3 + 3)


    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(math.floor(random.random() * 3 + 2))
        username_field = self.driver.find_element_by_name("username")
        for char in self.username:
            sleep(random.random()/10)
            username_field.send_keys(char)
        password_field = self.driver.find_element_by_name("password")
        for char in self.password:
            sleep(random.random()/10)
            password_field.send_keys(char)
        #self.driver.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button").click()
        self.driver.find_elements_by_xpath("//*[text()='Log In']")[0].click()



    def isFollower(self,username):
        # Go to page of DMer
        self.driver.find_elements_by_class_name("sqdOP")[1].click()
        sleep(2)
        return self.driver.find_element_by_class_name("_5f5mN").text.strip() != "Follow"

    def getOneRequest(self):
        # click Requests
        self.driver.find_elements_by_class_name("gtFbE")[0].click()
        sleep(3)
        # click first request
        self.driver.find_elements_by_class_name("R19PB")[0].click()
        sleep(3)
        #doesFollow = self.isFollower(self.driver.find_elements_by_class_name("m7ETg")[1].text)
        #print("doesFollow: " + str(doesFollow))
        #sleep(5)
        # click Accept
        self.driver.find_elements_by_class_name("nmMym")[2].click()
        sleep(3)
        # click General
        self.driver.find_elements_by_xpath("//*[text()='General']")[0].click()
        sleep(2)
        # Send DM in textbox
        textarea = self.driver.find_element_by_tag_name("textarea")
        for char in introText:
            sleep(random.random()/10)
            textarea.send_keys(char)

        sleep(2)
        print("Sending intro reply...")
        self.driver.find_element_by_xpath("//*[text()='Send']").click()
        sleep(2)


    def do_dm_round(self,num_dms=5):
        # click dm's button
        self.driver.find_element_by_class_name("xWeGp").click()
        sleep(3)
        for i in range(num_dms):
            self.getOneRequest()









if __name__ == '__main__':
    #4th argument indicates whether or not the account is the main account
    user1 = 'username'
    user1_pass = 'password'
    main1 = 'username'
    main1_pass = 'password'



    ig_bot = InstagramBot(main1,main1_pass,'',True)
    sleep(math.floor(random.random() * 3 + 2))
    ig_bot.do_dm_round(5)
