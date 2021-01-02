from selenium import webdriver
import os
import time
from time import sleep
from utility_methods import randomCommentText
from utility_methods import randomCommentTextMain
from datetime import datetime
import random
import math


#import PySimpleGUI as sg

introText = u"Hey what’s up, hope you're doing well \u2764 At Genuine Aesthetic we’re all about supporting the streets! We work with homeless shelters to feed and clothe the homeless and displaced who have been cruelly neglected during these difficult times \u2764. If you like our gear and would like to support us, give us a follow and share the brand. Let us know what you think about our clothing or your favorite design of ours!"

introTextAlreadyFollows = u"Hey what’s up, hope you're doing well \u2764 At Genuine Aesthetic we’re all about supporting the streets! We work with homeless shelters to feed and clothe the homeless and displaced who have been cruelly neglected during these difficult times \u2764. If you like our gear and value our mission, share the brand. Let us know what you think about our clothing or your favorite design of ours!"

sellText = u"Thanks for the support! You can check out our full premium streetwear collection at genaes.com \u2764 We really like your style and we think you’ll love our quality so feel free to use the code “GetGA” for 25% off at checkout if anything catches your eye \u270C Best of luck during times like this and be sure to stay safe! \u270A The code expires in 1 week so order soon!"

class InstagramBot:

    def __init__(self, username, password, brand, is_main):
        self.username = username
        self.password = password
        self.brand = brand
        self.is_main = is_main
        self.previousComments = open("Instagram_Comment_Names", "a")
        self.previousCommentsUsernames = open("Instagram_Comment_Names", "r").read().split(" ")
        #self.driver = webdriver.Firefox('/Users/thedg/Desktop/Insta-Bot/geckodriver.exe')
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
        print("Stripped: " + self.driver.find_element_by_class_name("_5f5mN").text.strip())
        return self.driver.find_element_by_class_name("_5f5mN").text.strip() != "Follow"

    def getOneRequest(self):
        # click Requests
        self.driver.find_elements_by_class_name("gtFbE")[0].click()
        sleep(3)
        # click first request
        self.driver.find_elements_by_class_name("R19PB")[0].click()
        sleep(3)
        doesFollow = self.isFollower(self.driver.find_elements_by_class_name("m7ETg")[1].text)
        print("doesFollow: " + str(doesFollow))
        self.driver.back()
        sleep(2)
        # click Accept
        self.driver.find_elements_by_class_name("nmMym")[2].click()
        sleep(3)
        # click General
        self.driver.find_elements_by_xpath("//*[text()='General']")[0].click()
        sleep(2)
        # Send DM in textbox
        textarea = self.driver.find_element_by_tag_name("textarea")

        if (not doesFollow):
            for char in introText:
                sleep(random.random()/10)
                textarea.send_keys(char)
        else:
            for char in introTextAlreadyFollows:
                sleep(random.random()/10)
                textarea.send_keys(char)

        sleep(2)
        print("Sending intro reply...")
        self.driver.find_element_by_xpath("//*[text()='Send']").click()
        sleep(2)


    def sell_dms(self):
        # Click General
        self.driver.find_elements_by_xpath("//*[text()='General']")[0].click()
        sleep(2)
        # Get unread messages
        people_to_sell = self.driver.find_elements_by_class_name("_41V_T")
        print(people_to_sell)
        for person in people_to_sell:
            person.click()
            # Send DM in textbox
            textarea = self.driver.find_element_by_tag_name("textarea")
            for char in sellText:
                sleep(random.random()/10)
                textarea.send_keys(char)

            sleep(2)
            print("Sending intro reply...")
            self.driver.find_element_by_xpath("//*[text()='Send']").click()
            sleep(2)



    def do_dm_round(self,mode="intro", num_dms = 5):
        '''
        DM's people in requests or general to introduce them or to sell them
        "intro" mode is for sending dms to Requests
        "sell" mode is for sending codes ti General
        '''

        # click dm's button
        self.driver.find_element_by_class_name("xWeGp").click()
        sleep(2)

        if (mode == "intro"):
            sleep(3)
            for i in range(num_dms):
                self.getOneRequest()
        else:
            sleep(3)
            self.sell_dms()



if __name__ == '__main__':
    main1 = 'user'
    main1_pass = 'pass'

    ig_bot = InstagramBot(main1,main1_pass,'hufworldwide',True)
    sleep(math.floor(random.random() * 3 + 2))
    ig_bot.do_dm_round("intro",1)
    #ig_bot.do_dm_round("sell")
