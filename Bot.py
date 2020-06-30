from selenium import webdriver
import os
import time
from time import sleep
from utility_methods import randomCommentText
import random
import math

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.previousComments = open("Instagram_Comment_Names", "a")
        self.previousCommentsUsernames = open("Instagram_Comment_Names", "r").read().split(" ")
        self.driver = webdriver.Chrome('/Users/othurm/Desktop/Insta-Bot/chromedriver')
        self.login()

    def login(self):
     self.driver.get('https://www.instagram.com/accounts/login/')
     sleep(math.floor(random.random() * 2 + 2))
     self.driver.find_element_by_name("username").send_keys(self.username)
     self.driver.find_element_by_name("password").send_keys(self.password)
     self.driver.find_element_by_css_selector(
         "#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button").click()

    def search(self, searchText):
        sleep(math.floor(random.random() * 2 + 4))
        #click search bar
        self.driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > div").click()
        #type searchText
        self.driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input").send_keys(searchText)
        sleep(math.floor(random.random() * 2 + 3))
        #select first option
        self.driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > div:nth-child(4) > div.drKGC > div > a:nth-child(1)").click()

    def getFollowerList(self):
        sleep(math.floor(random.random() * 2 + 2))
        #clicks the list of followers
        self.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(2) > a").click()

    def getFollowerAfterScroll(self, followerNum):
        sleep(math.floor(random.random() * 2 + 2))
        #gets the follower that corresponds to followerNum
        self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(" + str(followerNum) + ") > div > div.t2ksc > div.enpQJ > div.d7ByH > a").click()


    def getFollower(self, followerNum):
        sleep(math.floor(random.random() * 2 + 2))
        #gets the follower that corresponds to followerNum
        self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(" + str(followerNum) + ") > div > div.Igw0E.IwRSH.YBx95.vwCYk > div > div > div > a").click()    

    def comment(self, commentText):
       sleep(math.floor(random.random() * 2 + 2))
       #click the latest post
       self.driver.find_element_by_css_selector("#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1) > a").click()
       sleep(math.floor(random.random() * 2 + 2))
       self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span._15y0l > button").click()
       sleep(math.floor(random.random() * 2 + 2))
       self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea").send_keys(commentText)
       sleep(math.floor(random.random() * 2 + 2))
       self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > button").click()
       sleep(math.floor(random.random() * 2 + 2))
       self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button > svg").click()
       sleep(math.floor(random.random() * 2 + 2))
       self.driver.back()
       self.driver.back()

    def doCommentRound(self):
        j = 1
        i = 0
        scrolled = False
        while i <= 15:
            try:
                if(scrolled):
                    self.getFollowerAfterScroll(j)
                else:
                    self.getFollower(j)  
                sleep(math.floor(random.random() * 2 + 4)) 
                try:   
                    username = self.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > div.nZSzR > h2").text
                except:
                    username = self.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > div.nZSzR > h1").text    
                try:
                    if(self.followingUnder1500() and not self.alreadyCommented(username)):
                        self.previousComments.write(username + " ")
                        self.comment(randomCommentText())
                        print("comment number " + str(i) + " on account number " + str(j))
                        i+=1
                        j+=1
                    else:
                        j+=1
                        self.driver.back()
                except:
                    self.driver.back()
                    j+=1    
                if(j > 5):
                    scrolled = True
                    target = self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(" + str(j) + ")")
                    self.driver.execute_script('arguments[0].scrollIntoView(true);', target) 
            except:
                j+=1
        self.previousComments.close()         


    def alreadyCommented(self, username):
        for commented_on_user in self.previousCommentsUsernames:
            if(commented_on_user == username):
                return True
        return False        


    def followingUnder1500(self):
        sleep(math.floor(random.random() * 2 + 3))
        return (int(ig_bot.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(3) > a > span").text.replace(',', '')) < 1500)
    
if __name__ == '__main__':
    ig_bot = InstagramBot('owenthurm', 'Gandolf1')
    ig_bot.search("riot society")
    ig_bot.getFollowerList()
    sleep(2)
    ig_bot.doCommentRound()