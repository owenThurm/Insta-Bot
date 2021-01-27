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
#import pyautogui
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

        self.driver = webdriver.Chrome('/Users/othurm/Desktop/Insta-Bot/chromedriver')

        #chrome_options = webdriver.ChromeOptions()
        #chrome_options.headless = True
        #chrome_options.add_argument("--headless") # Runs Chrome in headless mode.
        #chrome_options.add_argument('--no-sandbox') # Bypass OS security model
        #chrome_options.add_argument('--disable-gpu')  # applicable to windows os only
        #chrome_options.add_argument('start-maximized') #
        #chrome_options.add_argument('disable-infobars')
        #chrome_options.add_argument("--disable-extensions")
        #chrome_options.add_argument('--proxy-server=%s' % PROXY)

        #chrome_options.add_argument("--window-size=1920x1080")
        #user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        #chrome_options.add_argument(f'user-agent={user_agent}')
        #self.driver = webdriver.Chrome(options=chrome_options)#,seleniumwire_options=options)
        sleep(random.random() * 2)

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

        except Exception as e:
            print("Login failed....", e)
        screenshot here
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
            print("Failed to wait for followers>>>", e)
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

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.FPmhX"))
            )
            sleep(random.random() / 2 + 0.1)
        except Exception as e:
            print("Failed to wait for followers>>>")
            print(e)
        #sleep(1)
        self.driver.find_elements_by_css_selector("a.FPmhX")[followerNum].click()


    def comment(self, commentText):
        try:
            # Click the latest post
            print("Selecting latest post...")
            self.driver.find_element_by_css_selector("#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1) > a > div.eLAPa").click()
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

                self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button").click()
                print("Media liked.")
                sleep(math.floor(random.random() * 2 + 1))
                #print("here2")
                self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span._15y0l > button").click()
                sleep(math.floor(random.random() * 3 + 2))
                commentBox = self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
                commentBox.send_keys(commentText)
                print("Media commented.")
                sleep(math.floor(random.random() * 2 + 2))
                number_of_comments_before = self.getNumberOfComments()
                # Hit the post button
                self.driver.find_element_by_xpath("//button[contains(text(),'Post')]").click()
                sleep(random.random() * 2 + 4)
                if not self.checkCommentDidPost(number_of_comments_before):
                screenshot here
                    print("!!!!!!!!!!!!!!!######### UNABLE TO POST COMMENT #########!!!!!!!!!!!!!!!")

                print("Commented: " + commentText)
                sleep(random.random() + .5)
                return True

            except Exception as e:
                print('Commenting on post failed', e)
                sleep(random.random() + 0.3)
                return False
        except Exception as e:
            print('Selecting latest post failed', e)
            return False

    def scrapeFollowers(self):

        '''
            Returns a list of followers after scrolling through the modal.
        '''

        SCROLL_PAUSE = 0.8  # Pause to allow loading of content
        self.driver.execute_script("followersbox = document.getElementsByClassName('isgrP')[0];")
        last_height = self.driver.execute_script("return followersbox.scrollHeight;")

        # Finally, scrape the followers
        selector = "a.FPmhX"

        # We need to scroll the followers modal to ensure that all followers are loaded
        while True:
            self.driver.execute_script("followersbox.scrollTo(0, followersbox.scrollHeight);")

            # Wait for page to load
            time.sleep(SCROLL_PAUSE)

            # Calculate new scrollHeight and compare with the previous
            new_height = self.driver.execute_script("return followersbox.scrollHeight;")
            if new_height == last_height or len(self.driver.find_elements_by_css_selector(selector)) >= 50:
                break
            last_height = new_height
            print(self.driver.find_elements_by_css_selector(selector))

        # Finally, scrape the followers
        followers_elems = self.driver.find_elements_by_css_selector(selector)
        print(followers_elems)

        followers = [e.text for e in followers_elems]  # List of followers

        print("______________________________________")
        print("SCRAPED FOLLOWERS")

        return followers

    # To be used to get the number of comments on a post
    def getNumberOfComments(self):
        return len(self.driver.find_elements_by_class_name("Mr508"))


    # To be used to check if a comment was successfully posted
    def checkCommentDidPost(self, num_comments_before):
        return self.getNumberOfComments() > num_comments_before

    # To be used to go to a instagram follower account page
    def goToFollower(self,follower):
        sleep(random.random() + 0.5)
        self.driver.get(f"https://www.instagram.com/{follower}/")
        sleep(random.random() + 0.5)


    def doCommentRound(self):

        sleep(random.random() + 1)
        # Get follower names
        followers = self.scrapeFollowers()
        #print(followers)

        comments_done = 0
        # For every folllower name, go to follower url and comment until comments_done reaches target amount.
        for follower in followers:

            if follower in self.previousCommentsUsernames:
                continue

            self.goToFollower(follower)

            comment = randomCommentText()
            if (self.is_main):
                comment = randomCommentTextMain()

            if (self.comment(comment)):
                comments_done += 1
                print("Comment: ", comments_done)
                print("Cummented on: ", follower)

            if comments_done == 30:
                break

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
        except Exception as e:
            print("Exception", e)
            return False


    def followingUnder1500(self):
        sleep(math.floor(random.random() * 3 + 2))
        try:
            return (int(self.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(3) > a > span").text.replace(',', '')) < 1500)
        except Exception as e:
            print("Get number of followers failed", e)
            return False

    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    #4th argument indicates whether or not the account is the main account

    user1 = ""
    user1_pass = ""

    user3 =  "username"
    user3_pass = "password"

    main1 = "genuineaesthetic"
    main1_pass = "MagicJohnson32!"

    #ig_bot = InstagramBot(user1, user1_pass, 'zumiez', False)
    #ig_bot = InstagramBot(user2,user2_pass,'fuckit.jp',False)
    #ig_bot = InstagramBot(user3,user3_pass,'heartlessclothingco',False)
    #ig_bot = InstagramBot(user3,user3_pass,'vzn_clothing',False)
    #ig_bot = InstagramBot(user2,user2_pass,'hufworldwide',False)
    #ig_bot = InstagramBot(user2,user2_pass,'bmeboston',False)
    #ig_bot = InstagramBot(user2,user2_pass,'movingto.mars',False)
    #ig_bot = InstagramBot(user1,user1_pass,'scummy__apparel',False)
    #ig_bot = InstagramBot(user1,user1_pass,'verborgenstudios',False)
    #ig_bot = InstagramBot(user1,user1_pass,'yourstrulyclothing',False)
    #ig_bot = InstagramBot(user1,user1_pass,'zumiez',False)
    #ig_bot = InstagramBot(main1,main1_pass,'novaluestreetwear',False)
    #ig_bot = InstagramBot(main1,main1_pass,'hufworldwide',True)
    #ig_bot = InstagramBot(main1,main1_pass,'zumiez',True)
    #ig_bot = InstagramBot(main1,main1_pass,'annashumatee',True)
    #sleep(math.floor(random.random() * 3 + 2))

    if (ig_bot.doCommentRound()):
        print("done")
        #ig_bot.quit()