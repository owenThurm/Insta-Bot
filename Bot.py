from selenium import webdriver
import os
import time
from time import sleep
from utility_methods import randomCommentText

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
        #click search bar
        self.driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > div").click()
        #type searchText
        self.driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input").send_keys(searchText)
        sleep(3)
        #select first option
        self.driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > div:nth-child(4) > div.drKGC > div > a:nth-child(1)").click()

    def getFollowerList(self):
        sleep(2)
        #clicks the list of followers
        self.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(2) > a").click()

    def getFollower(self, followerNum):
        sleep(2)
        #gets the follower that corresponds to followerNum
        self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(" + str(followerNum) + ") > div > div.Igw0E.IwRSH.YBx95.vwCYk > div > div > div > a").click()

    def comment(self, commentText):
       sleep(2)
       #click the latest post
       self.driver.find_element_by_css_selector("#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1) > a").click()
       sleep(2)
       self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span._15y0l > button").click()
       sleep(2)
       self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea").send_keys(commentText)
       sleep(2)
       self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > button").click()
       sleep(2)
       self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button > svg").click()
       sleep(2)
       self.driver.back()
       self.driver.back()

    #Authenticates a user profile: sorts out people who are following > 1500 and people who have already been commented on
    #Assumes that the bot is already on a user profile.
    def authenticateTarget(self):
        sleep(2)   
        if(self.followingUnder1500()):
            return False
        else:
             return True    

    def doCommentRound(self):
        j = 1
        i = 0
        while i < 15:
            self.getFollower(j)
            if(self.authenticateTarget):
                self.comment(randomCommentText())
                i+=1
                j+=1
            else:
                j+=1    

    def followingUnder1500(self):
        return (int(ig_bot.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(3) > a > span").text.replace(',', '')) < 1500)
    

if __name__ == '__main__':
    ig_bot = InstagramBot('username', 'password')
    ig_bot.search("movingtomars")
    ig_bot.getFollowerList()
    sleep(2)
    ig_bot.doCommentRound()
    print(randomCommentText())








