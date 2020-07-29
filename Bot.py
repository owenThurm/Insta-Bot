from selenium import webdriver
import os
import time
from time import sleep
from utility_methods import randomCommentText 
from utility_methods import randomCommentTextMain
import random
import math

class InstagramBot:

    def __init__(self, username, password, brand, is_main):
        self.username = username
        self.password = password
        self.brand = brand
        self.is_main = is_main
        self.previousComments = open("Instagram_Comment_Names", "a")
        self.previousCommentsUsernames = open("Instagram_Comment_Names", "r").read().split(" ")
        self.driver = webdriver.Chrome('/Users/othurm/Desktop/Insta-Bot/chromedriver')
        sleep(random.random() * 3 + 3)
        self.login()
        sleep(random.random() * 3 + 3)
        self.search(self.brand)
        sleep(random.random() * 3 + 3)
        self.getFollowerList()

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
     self.driver.find_element_by_css_selector(
         "#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button").click()

    def search(self, searchText):
        sleep(math.floor(random.random() * 3 + 4))
        #click search bar
        self.driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > div").click()
        #type searchText
        searchBox = self.driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input")
        for char in searchText:
            sleep(random.random()/10)
            searchBox.send_keys(char)
        sleep(math.floor(random.random() * 3 + 3))
        #select first option
        self.driver.find_element_by_css_selector("span.Ap253").click()

    def getFollowerList(self):
        sleep(math.floor(random.random() * 3 + 2))
        #clicks the list of followers
        self.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(2) > a").click()

    def getFollowerAfterScroll(self, followerNum):
        sleep(math.floor(random.random() * 3 + 2))
        #gets the follower that corresponds to followerNum
        #self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(" + str(followerNum) + ") > div > div.t2ksc > div.enpQJ > div.d7ByH > a").click()
        self.driver.find_elements_by_css_selector("a.FPmhX")[followerNum].click()


    def getFollower(self, followerNum):
        sleep(math.floor(random.random() * 3 + 2))
        #gets the follower that corresponds to followerNum
        #self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(" + str(followerNum) + ") > div > div.Igw0E.IwRSH.YBx95.vwCYk > div > div > div > a").click()
        self.driver.find_elements_by_css_selector("a.FPmhX")[followerNum].click()
    def comment(self, commentText):
        try:
            sleep(math.floor(random.random() * 3 + 2))
            #click the latest post
            self.driver.find_element_by_css_selector("#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1) > a").click()
            try:
                sleep(math.floor(random.random() * 3 + 2))
                self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button").click()
                sleep(math.floor(random.random() * 2 + 1))
                self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span._15y0l > button").click()
                sleep(math.floor(random.random() * 3 + 2))
                commentBox = self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
                for char in commentText:
                    sleep(random.random()/10)
                    commentBox.send_keys(char)
                sleep(math.floor(random.random() * 3 + 2))
                self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > button").click()
                sleep(math.floor(random.random() * 3 + 2))
                self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button > svg").click()
                sleep(math.floor(random.random() * 3 + 2))
                self.driver.back()
                sleep(math.floor(random.random() * 3 + 1))
                self.driver.back()
            except:
                print('commenting on post failed')
                sleep(math.floor(random.random() * 3 + 2))
                #backs out of the post
                self.driver.back()
                sleep(math.floor(random.random() * 3 + 1))
                #backs out of the profile
                self.driver.back()
        except:
            print('sselecting latest post failed')
            sleep(math.floor(random.random() * 3 + 3))
            #backs out of the profile
            self.driver.back()

    def doCommentRound(self):
        j = 1
        i = 0
        scrolled = False
        while i <= 15:
            try:
                if(j > 5):
                    scrolled = True
                    target = self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(" + str(j) + ")")
                    self.driver.execute_script('arguments[0].scrollIntoView(true);', target) 
                if(scrolled):
                    self.getFollowerAfterScroll(j)
                else:
                    self.getFollower(j)  
                sleep(math.floor(random.random() * 3 + 3))    
                try:   
                    username = self.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > div.nZSzR > h2").text
                except:
                    username = self.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > div.nZSzR > h1").text    
                try:
                    if(self.followingUnder1500() and not self.alreadyCommented(username)):
                        self.previousComments.write(username + " ")
                        print('commented on ' + username)
                        if(self.is_main):
                            self.comment(randomCommentTextMain())
                        else:    
                            self.comment(randomCommentText())
                        print("comment number " + str(i) + " on account number " + str(j))
                        i+=1
                        j+=1
                    else:
                        j+=1
                        self.driver.back()
                except:
                    print('failed to comment')
                    self.driver.back()
                    j+=1    
            except:
                print('overall comment round failed')
                j+=1
            if(j > 300):
                break    
        self.previousComments.close()         


    def alreadyCommented(self, username):
        for commented_on_user in self.previousCommentsUsernames:
            if(commented_on_user == username):
                return True
        return False        


    def followingUnder1500(self):
        sleep(math.floor(random.random() * 3 + 2))
        return (int(ig_bot.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(3) > a > span").text.replace(',', '')) < 1500)
    
if __name__ == '__main__':
    #4th argument indicates whether or not the account is the main account
    ig_bot = InstagramBot('username', 'password', 'brand name', False)
    sleep(math.floor(random.random() * 3 + 2))
    ig_bot.doCommentRound()
