from selenium import webdriver
import os
import time
from time import sleep
from utility_methods import randomCommentText
from utility_methods import randomCommentTextMain
import random
import math
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from threading import Thread
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PROXY = "91.229.245.187:21289" #HOST:PORT
PROXY_USERNAME = "bobdill32984"
PROXY_PASSWORD = "1pntv8iqkb"

class InstagramBot:

    def __init__(self, username, password, brand, is_main):
        self.username = username
        self.password = password
        self.brand = brand
        self.is_main = is_main
        self.previousComments = open("Instagram_Comment_Names", "a")
        self.previousCommentsUsernames = open("Instagram_Comment_Names", "r").read().split(" ")
        
    
        
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.headless = True
        #chrome_options.add_argument("--headless") # Runs Chrome in headless mode.
        #chrome_options.add_argument('--no-sandbox') # Bypass OS security model
        #chrome_options.add_argument('--disable-gpu')  # applicable to windows os only
        #chrome_options.add_argument('start-maximized') # 
        #chrome_options.add_argument('disable-infobars')
        #chrome_options.add_argument("--disable-extensions")
        #chrome_options.add_argument('--proxy-server=%s' % PROXY)
        
        
        chrome_options.add_argument("--window-size=1920x1080")
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        chrome_options.add_argument(f'user-agent={user_agent}')
        self.driver = webdriver.Chrome(options=chrome_options)#,seleniumwire_options=options)
        sleep(random.random() * 3 + 3)
        
        # Login to Your Account
        self.login()
        # Goes the URL of target brand
        self.get_brand()
        # Click on list of followers
        self.getFollowerList()
        
        

    def login(self):
        try:
            #self.driver.get("https://whatismyipaddress.com/")
            #self.driver.save_screenshot("screenie1.png")
            self.driver.get('https://www.instagram.com/accounts/login/')
            
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[text()='Log In']"))
                )
                sleep(random.random() * 2)
            except Exception as e:
                print("Failed to land on login page>>>")
                print(e)
                
            username_field = self.driver.find_element_by_name("username")
            username_field.send_keys(self.username)
            sleep(0.1 + random.random())
            password_field = self.driver.find_element_by_name("password")   
            password_field.send_keys(self.password)
            #self.driver.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button").click()
            self.driver.find_elements_by_xpath("//*[text()='Log In']")[0].click()
            # Wait until we truly logged in and landed in home page
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
                )
                sleep(random.random() * 2)
            except Exception as e:
                print("Failed to land in homepage>>>")
                print(e)
     
        except:
            print("Login failed....")
            #self.driver.save_screenshot("screenshot.png")
            #self.driver.close()


    def search(self, searchText):
        print("IN SEARCH>>>>>")
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
    
    def get_brand(self):
        print(f"Going here: https://www.instagram.com/{self.brand}/")
        self.driver.get(f"https://www.instagram.com/{self.brand}/")
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "-nal3 "))
            )
            sleep(random.random() / 2 + 0.1)
        except Exception as e:
            print("Failed to wait for followers>>>")
            print(e)
            #self.driver.quit()
        

    def getFollowerList(self):
        #clicks the list of followers
        self.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(2) > a").click()
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "m82CD"))
            )
            sleep(random.random() / 2 + 0.1)
        except Exception as e:
            print("Failed to wait for followers>>>")
            print(e)

    # def getFollowerAfterScroll(self, followerNum):
    #     #sleep(math.floor(random.random() * 3 + 2))
    #     #gets the follower that corresponds to followerNum
    #     #self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(" + str(followerNum) + ") > div > div.t2ksc > div.enpQJ > div.d7ByH > a").click()
    #     try:
    #         element = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.CSS_SELECTOR, f"a.FPmhX:nth-child({followerNum})"))
    #         )
    #         sleep(random.random() / 2 + 0.1)
    #     except Exception as e:
    #         print("Failed to wait for followers>>>")
    #         print(e)
    #     self.driver.find_elements_by_css_selector("a.FPmhX")[followerNum].click()


    def getFollower(self, followerNum):
        #sleep(math.floor(random.random() * 3 + 2))
        #gets the follower that corresponds to followerNum
        #self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(" + str(followerNum) + ") > div > div.Igw0E.IwRSH.YBx95.vwCYk > div > div > div > a").click()
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "._0imsa"))
            )
            sleep(random.random() / 2 + 0.1)
        except Exception as e:
            print("Failed to wait for followers>>>")
            print(e)
        self.driver.find_elements_by_css_selector("a.FPmhX")[followerNum].click()
        

    def comment(self, commentText):
        try:
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "-nal3 "))
                )
                sleep(random.random() / 2 + 0.1)
            except Exception as e:
                print("Failed to wait for person's profile to load>>>")
                print(e)
                
            #click the latest post
            print("Selecting latest post...")
            self.driver.find_element_by_css_selector("#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1) > a > div.eLAPa").click()
            #self.driver.find_element_by_css_selector("#react-root > section > main > div > div._2z6nI > article > div > div > div.NnQ7C.weEfm > div.v1Nh3.kIKUG ._bz0w > a > div.eLAPa").click()
            try:
                print("Post selected...")
                try:
                    element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//*[text()='Post']"))
                    )
                    sleep(random.random() / 2 + 0.1)
                except Exception as e:
                    print("Failed to wait for person's profile to load>>>")
                    print(e)
                #if (not self.alreadyLiked()):
                if (True):
                    self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button").click()
                    print("Media liked.")
                    sleep(math.floor(random.random() * 2 + 1))
                    #print("here2")
                    self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span._15y0l > button").click()
                    sleep(math.floor(random.random() * 3 + 2))
                    commentBox = self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
                    commentBox.send_keys(commentText)
                    print("Media commented.")
                    sleep(math.floor(random.random() * 3 + 2))
                    # Hit the post button
                    self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > button").click()
                    sleep(math.floor(random.random() * 3 + 2))
                    #self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button > svg").click()
                    #print("Final click thing.")
                    #sleep(math.floor(random.random() * 3 + 2))
                    print("Commented: " + commentText)
                    self.driver.back()
                    sleep(math.floor(random.random() * 3 + 1))
                    self.driver.back()
                    return True
                else:
                    self.driver.back()
                    sleep(math.floor(random.random() * 3 + 1))
                    self.driver.back()
                    return False
            except:
                print('Commenting on post failed')
                sleep(math.floor(random.random() * 3 + 2))
                #backs out of the post
                self.driver.back()
                sleep(math.floor(random.random() * 3 + 1))
                #backs out of the profile
                self.driver.back()
                return False
        except:
            print('Selecting latest post failed')
            sleep(math.floor(random.random() * 3 + 3))
            #backs out of the profile
            self.driver.back()
            return False


    def doCommentRound(self):
        j = 1
        i = 0
        scrolled = False
        ac = ActionChains(self.driver)
        dms = self.driver.find_element_by_class_name("xWeGp")
        while i < 13:
            try:
                if(j > 5):
                    scrolled = True
                    target = self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(" + str(j) + ")")
                    self.driver.execute_script('arguments[0].scrollIntoView(true);', target)
                
                # Check if user was previously commented on
                username = self.driver.find_elements_by_class_name("_0imsa")[j].text
                print("Got username text: " + username)
                if (self.alreadyCommented(username)):
                    j += 1
                    continue
                
                # Click on follower from list of followers
                self.getFollower(j)
                print("\nGot follower no cap")
                
                # try:
                #     username = self.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > div.nZSzR > h2").text
                #     print("Got username: " + username)
                # except:
                #     username = self.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > div.nZSzR > h1").text
                #     print("Got username: " + username)
                try:
                    if(self.followingUnder1500() and not self.alreadyCommented(username)):
                        if(self.is_main):
                            if(self.comment(randomCommentTextMain())):
                                i+=1
                                print('Commented on ' + username)
                                print("Comment number " + str(i) + " on account number " + str(j))
                                self.previousComments.write(username + " ")
                                print("Added username " + username)
                        else:
                            if(self.comment(randomCommentText())):
                                i+=1
                                print('Commented on ' + username)
                                print("Comment number " + str(i) + " on account number " + str(j))
                                self.previousComments.write(username + " ")
                                print("Added username " + username)
                        #i+=1
                        j+=1
                    else:
                        j+=1
                        self.driver.back()

                except:
                    print('Unable to comment')
                    self.driver.back()
                    j+=1
            except:
                print('Overall comment round failed.')
                # posts = self.driver.find_element_by_xpath("//*[contains(text(), 'Follow')]")
                # ac.move_to_element(posts).click().perform()
                #dms = self.driver.find_element_by_class_name("xWeGp")
                followers_heading = self.driver.find_element_by_class_name("m82CD")
                ac.move_to_element(followers_heading).click().perform()
                print('Moved to avoid comment failure.')
                j+=1
            if(j > 150):
                return True
        self.previousComments.close()
        return True


    def alreadyCommented(self, username):
        for commented_on_user in self.previousCommentsUsernames:
            if(commented_on_user == username):
                return True
        return False

    def alreadyLiked(self):
        #unlike_xpath = "//section/span/button/div/span[*[local-name()='svg']/@aria-label='Unlike']"
        unlike_path = "html > body > div > div > div > article > div > section > span > button > div.QBdPU > span > svg._8-yf5"
        try:
            aria_label = self.driver.find_element_by_css_selector(unlike_path).get_attribute("aria-label")

            print("aria-label: " + aria_label)

            '''liked_elem = self.driver.find_elements_by_xpath(unlike_xpath)
            if len(liked_elem) == 1:
                print("Image already liked... moving on")
                return True
            print("Image has not been previously liked.")
            return False'''
            
            if (aria_label == "Unlike"):
                return True
            return False
        except:
            print("Exception")
            return False


    def followingUnder1500(self):
        sleep(math.floor(random.random() * 3 + 2))
        try:
            return (int(self.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(3) > a > span").text.replace(',', '')) < 1500)
        except:
            print("Get number of followers failed")
            return False

if __name__ == '__main__':
    #4th argument indicates whether or not the account is the main account
    
    
    #ig_bot = InstagramBot(user2,user2_pass,'fuckit.jp',False)
    #ig_bot = InstagramBot(user3,user3_pass,'heartlessclothingco',False)
    #ig_bot = InstagramBot(user3,user3_pass,'vzn_clothing',False)
    #ig_bot = InstagramBot(user2,user2_pass,'hufworldwide',False)
    #ig_bot = InstagramBot(user2,user2_pass,'bmeboston',False)
    #ig_bot = InstagramBot(user2,user2_pass,'movingto.mars',False)
    #ig_bot = InstagramBot(user1,user1_pass,'scummy__apparel',False)
    #ig_bot = InstagramBot(user1,user1_pass,'verborgenstudios',False)
    #ig_bot = InstagramBot(user1,user1_pass,'yourstrulyclothing',False)
    ig_bot = InstagramBot(user1,user1_pass,'zumiez',False)
    #ig_bot = InstagramBot(main1,main1_pass,'novaluestreetwear',False)
    #ig_bot = InstagramBot(main1,main1_pass,'hufworldwide',True)
    #ig_bot = InstagramBot(main1,main1_pass,'zumiez',True)
    #ig_bot = InstagramBot(main1,main1_pass,'annashumatee',True)
    #sleep(math.floor(random.random() * 3 + 2))
    
    if (ig_bot.doCommentRound()):
        ig_bot.quit()
        
    