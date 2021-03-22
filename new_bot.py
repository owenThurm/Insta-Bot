from seleniumwire import webdriver
import os
import time
from time import sleep
from utility_methods import randomCommentText
from utility_methods import randomCommentTextMain
import random
import math
import sys
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
import emoji

PROXY = "91.229.245.187:21289" #HOST:PORT
PROXY_USERNAME = "bobdill32984"
PROXY_PASSWORD = "1pntv8iqkb"
PERIOD_OF_TIME = 400
class InstagramBot:

    def __init__(self, username, password, brand, is_main):
        self.username = username
        self.password = password
        self.brand = brand
        self.is_main = is_main
        self.previousComments = open("Instagram_Comment_Names", "a")
        self.accounts_already_commented_on = open("Instagram_Comment_Names", "r").read().split(" ")
        self.comment_filter = {"post_min_number_of_comments": 0,
                               "post_max_number_of_comments":10000}
        self.comment_pool = []
        self.comments_done = 0
        self.num_comments = 1
        self.could_not_comment = False
        self.could_not_comment_popup = False
        self.is_liking = 1
        self.liking_blocked = False


        options = webdriver.ChromeOptions()
        #chrome_options.headless = True
        #chrome_options.add_argument("--headless") # Runs Chrome in headless mode.
        #chrome_options.add_argument('--no-sandbox') # Bypass OS security model
        #chrome_options.add_argument('--disable-gpu')  # applicable to windows os only
        #chrome_options.add_argument('start-maximized') #
        #chrome_options.add_argument('disable-infobars')
        #chrome_options.add_argument("--disable-extensions")
        #chrome_options.add_argument('--proxy-server=%s' % PROXY)


        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        options.add_argument(f'user-agent={user_agent}')
        #options.binary_location = os.getcwd() + "/headless-chromium"

        self.driver = webdriver.Chrome(
        executable_path=os.getcwd() + "/chromedriver",
        chrome_options=options,
        seleniumwire_options={
            'request_storage_base_dir': '/tmp',
            # 'proxy': {
            #     'https': f'https://bobdill32984:1pntv8iqkb@{PROXY}'
            #     }
            }
        )


        #self.driver.get("https://nordvpn.com/what-is-my-ip/")
        #print(self.driver.find_element_by_css_selector("body > div.Page.overflow-hidden.d-flex.flex-column > div:nth-child(1) > div > div > div > div > div > div > div.col-xs-12.col-sm-6.mb-7.mb-sm-0 > h3.Title.mb-6.js-ipdata-ip-address").text)


        self.inception_time = time.time()
        print("Inception:",self.inception_time)
        if not self.login():
            sys.exit("Login failed")

    def perform_preprocess(self):

        funcs = [self.get_brand, self.getFollowerList]

        for func in funcs:
            run = func()
            print("Run:",run)
            if not run:
                #sys.exit("Pre comment round processes failed")
                print("Pre comment round processes failed")
                return False
        return True

    def login(self):
        try:
            # self.driver.get("https://whatismyipaddress.com/")
            # self.driver.save_screenshot("screenie1.png")
            self.driver.get('https://www.instagram.com/accounts/login/')

            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//*[text()='Log In']"))
                )
                sleep(random.random() * 2)
            except Exception as e:
                print("Failed to land on login page>>>")
                print(e)
                print(self.driver.get_screenshot_as_base64())
                return False

            username_field = self.driver.find_element_by_name("username")
            username_field.send_keys(self.username)
            sleep(0.1 + random.random())
            password_field = self.driver.find_element_by_name("password")
            password_field.send_keys(self.password)
            # self.driver.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button").click()
            self.driver.find_elements_by_xpath(
                "//*[text()='Log In']")[0].click()
            # Wait until we truly logged in and landed in home page
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//input[@placeholder='Search']"))
                )
                sleep(random.random() * 2)
            except Exception as e:
                print("Failed to land in homepage>>>")
                print(self.driver.get_screenshot_as_base64())
                print(e)
                return False

        except Exception as e:
            print("Login failed....", e)
            print(self.driver.get_screenshot_as_base64())
            return False

        return True

    def search(self, searchText):
        print("IN SEARCH>>>>>")
        sleep(math.floor(random.random() * 3 + 4))
        # click search bar
        self.driver.find_element_by_css_selector(
            "#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > div").click()
        # type searchText
        searchBox = self.driver.find_element_by_css_selector(
            "#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input")
        for char in searchText:
            sleep(random.random()/10)
            searchBox.send_keys(char)
        sleep(math.floor(random.random() * 3 + 3))
        # select first option
        self.driver.find_element_by_css_selector("span.Ap253").click()

    def get_brand(self):
        print(f"Going here: https://www.instagram.com/{self.brand}/")
        self.driver.get(f"https://www.instagram.com/{self.brand}/")
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "-nal3 "))
            )
            sleep(random.random() / 2 + 0.1)
        except Exception as e:
            print("Failed to wait for brand page to load>>>", e)
            return False
            # self.driver.quit()

        return True

    def getFollowerList(self):
        # clicks the list of followers
        self.driver.find_element_by_css_selector(
            "#react-root > section > main > div > header > section > ul > li:nth-child(2) > a").click()

        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "m82CD"))
            )
            sleep(random.random() / 2 + 0.1)
        except Exception as e:
            print("Failed to wait for followers>>>")
            print(e)
            return False

        return True

    def getFollower(self, followerNum):

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.FPmhX"))
            )
            sleep(random.random() / 2 + 0.1)
        except Exception as e:
            print("Failed to wait for followers>>>")
            print(e)
        # sleep(1)
        self.driver.find_elements_by_css_selector(
            "a.FPmhX")[followerNum].click()

    def comment(self, commentText,follower=""):
        try:
            # Click the latest post
            print("Selecting latest post...")

            if not self.postSatisfiesNumCommentsFilter():
                print("Number of comments filter not met.")
                return False

            self.driver.find_element_by_css_selector(
                "#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1) > a > div.eLAPa").click()
            try:
                print("Post selected...")
                try:
                    element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, "body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg"))
                    )
                    sleep(random.random() / 2 + 0.6)
                except Exception as e:
                    print("Failed to wait for person's profile to load>>>")
                    print(e)

                if (self.is_liking):
                    self.driver.find_element_by_css_selector(
                        "body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button").click()
                    print("Media liked.")
                print("Follower:", follower)
                sleep(math.floor(random.random() * 2 + 1))

                good_for_commenting = self.postGoodForCommenting()

                if not good_for_commenting:
                    return False
                else:
                    print("Good for commenting...")

                if self.hasKeyPhrasesToAvoid():
                    print("Has key phrases")
                    return False

                if not self.satisfiesLikeRequirements():
                    print("Doesn't satisfy post like requirements")
                    return False


                self.driver.find_element_by_css_selector(
                    "body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span._15y0l > button").click()
                sleep(math.floor(random.random() * 3 + 2))
                commentBox = self.driver.find_element_by_css_selector(
                    "body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea")

                JS_ADD_TEXT_TO_INPUT = """
                  var elm = arguments[0], txt = arguments[1];
                  elm.value += txt;
                  elm.dispatchEvent(new Event('change'));"""


                text = "🌎 🌊 " + u'\u2764 Vibes!'

                self.driver.execute_script(JS_ADD_TEXT_TO_INPUT, commentBox, commentText)
                commentBox.send_keys(' ')


                #commentBox.send_keys(commentText)
                print("Media commented.")
                sleep(math.floor(random.random() * 2 + 2))
                number_of_comments_before = self.getNumberOfComments()
                # Hit the post button
                self.driver.find_element_by_xpath(
                    "//button[contains(text(),'Post')]").click()

                if self.couldNotPostCommentPopup():
                    print("!!! \"Couldn't post comment\" popup encountered at bottom of screen. !!!")
                    self.could_not_comment_popup = True
                    return False


                sleep(random.random() * 3.0)
                if not self.checkCommentDidPost(number_of_comments_before):
                    sleep(random.random() + 4.0)
                    #print(self.driver.get_screenshot_as_base64())
                    print(f"!!!### Failed to post comment. Comments before and after check failed. ###!!!")
                    print("Follower:",follower)
                    self.could_not_comment = True
                    sleep(random.random() + .5)
                    return False


                print("Commented: " + commentText)
                sleep(random.random() + .5)
                return True

            except Exception as e:
                print(f'Unable to like/comment on {follower}', e)
                #print(self.driver.get_screenshot_as_base64())
                sleep(random.random() + 0.3)
                return False
        except Exception as e:
            print(f'Selecting latest post failed for {follower}', e)
            return False


    def couldNotPostCommentPopup(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//p[contains(text(),\"Couldn't post comment.\")]"))
            )

        except Exception as e:
            print("Yay! Couldn't post comment bottom popup NOT encountered.")
            return False
        print(self.driver.get_screenshot_as_base64())
        return True




    def postGoodForCommenting(self):
        return self.checkPostHasCommentButton() and not self.checkPostHasLimitedComments()

    def checkPostHasLimitedComments(self):
        # Check if comments on post have been limited.
        limited = self.driver.find_elements_by_xpath(
            "//div[contains(text(),'Comments on this post have been limited.')]"
        )
        if len(limited) > 0: # post has comments limited
            print("Post has comments limited")
            return True
        else:
            #print("Post has comments normal")
            return False


    def checkPostHasCommentButton(self):
        # Check if there is no comment button
        comment_button = self.driver.find_elements_by_xpath(
            "//*[@aria-label='Comment']"
        )
        if len(comment_button) > 0:
            #print("There is comment button")
            return True
        else:
            print("There is no comment button")
            return False

    def checkInstaLikePopup(self):

        elems = self.driver.find_elements_by_css_selector(
            "body > div.RnEpo.Yx5HN > div > div > div"
            )
        #print("Elems:",elems)
        return len(elems) > 0


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
            self.driver.execute_script(
                "followersbox.scrollTo(0, followersbox.scrollHeight);")

            # Wait for page to load
            time.sleep(SCROLL_PAUSE)

            # Calculate new scrollHeight and compare with the previous
            new_height = self.driver.execute_script(
                "return followersbox.scrollHeight;")
            if new_height == last_height or len(self.driver.find_elements_by_css_selector(selector)) >= 80:
                break
            last_height = new_height
            #print(self.driver.find_elements_by_css_selector(selector))

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

    # To be used to get the number of comments on a post
    def getNumberOfComments(self):
        return len(self.driver.find_elements_by_class_name("Mr508"))

    # To be used to check if a comment was successfully posted

    def checkCommentDidPost(self, num_comments_before):
        currNum = self.getNumberOfComments()
        print(f"Number of comments before: {num_comments_before}, after: {currNum}")
        return currNum > num_comments_before

    # To be used to go to a instagram follower account page
    def goToFollower(self, follower):
        sleep(random.random() + 0.5)
        self.driver.get(f"https://www.instagram.com/{follower}/")
        sleep(random.random() + 0.5)

    def doCommentRound(self):
        print("Current Brand:",self.brand)

        sleep(random.random() + 1)
        # Get follower names
        followers = self.scrapeFollowers()
        # print(followers)

        comments_done = 0
        # For every follower name, go to follower url and comment until comments_done reaches target amount.
        for follower in followers:

            if follower in self.accounts_already_commented_on:
                print("Previously commented on: ", follower)
                continue

            self.goToFollower(follower)

            if self.is_private_profile() or self.has_no_posts():
                sleep(random.random() + 0.2)
                print("Skipped because private:", follower)
                continue

            if not (self.satisfiesFollowerRequirements() and self.satisfiesFollowingRequirements()):
                print("Follower/following requirements not satisifed for:", follower)
                continue

            if (self.acctDescHasKeyPhrasesToAvoid()):
                continue

            comment = randomCommentText()
            if (self.is_main):
                if len(self.comment_pool) >= 20:
                    comment = random.choice(self.comment_pool)

                else:
                    comment = randomCommentTextMain()


            if (self.comment(comment,follower)):
                self.comments_done += 1
                print("Comment: ", self.comments_done)
                print("Commented on: ", follower)
                self.accounts_already_commented_on.append(follower)
                #self.current_commented_on.append(follower)


            # Check for insta popup after comment attempted
            like_blocked = self.checkInstaLikePopup()

            if like_blocked or self.could_not_comment_popup:
                print("Like Popup:",like_blocked)
                if like_blocked:
                    self.liking_blocked = True
                print("[WARNING] Instagram Popup Encountered")
                sleep(1)
                print(self.driver.get_screenshot_as_base64())
                return False

            if self.could_not_comment: # number before and after not properly changed
                self.accounts_already_commented_on.append(follower)
                #self.current_commented_on.append(follower)
                return False


            if self.comments_done >= self.num_comments:
                break

            curr_time = time.time()
            #print("Curr time:", curr_time)
            #print("Inception + Period:",self.inception_time + PERIOD_OF_TIME)
            if curr_time > self.inception_time + PERIOD_OF_TIME:
                break

        return True

    def has_no_posts(self):
        """
        Checks whether the current account has no posts even if public.
        :return: True if has no posts, False otherwise
        """

        has_no_posts = False
        try:
            elem = self.driver.find_element_by_xpath("//*[contains(text(), 'No Posts Yet')]")
            has_no_posts = True
        except:

            has_no_posts = False


        print("Has No Posts:", has_no_posts)
        return has_no_posts




    def is_private_profile(self):
        """
        Verify whether current account is Private
        :return: True if private, False Otherwise
        """

        is_private = None
        try:
            element = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'This Account is Private')]"))
            )
            print("Element:", element)
            #elem = self.driver.find_element_by_xpath("//*[contains(text(), 'This Account is Private')]")
            is_private = True
        except:

            is_private = False

        print("Is Private: ", is_private)
        return is_private

    def alreadyCommented(self, username):
        for commented_on_user in self.previousCommentsUsernames:
            if(commented_on_user == username):
                return True
        return False

    def alreadyLiked(self):
        #unlike_xpath = "//section/span/button/div/span[*[local-name()='svg']/@aria-label='Unlike']"
        unlike_path = "html > body > div > div > div > article > div > section > span > button > div.QBdPU > span > svg._8-yf5"
        try:
            aria_label = self.driver.find_element_by_css_selector(
                unlike_path).get_attribute("aria-label")

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

    def satisfiesFollowerRequirements(self):
        sleep(math.floor(random.random() * 2 + 1))
        try:
            num_followers = int(
                self.driver.find_elements_by_css_selector(
                    ".g47SY")[1]
                    .get_attribute("title").replace(',', '')
                )
            print("Number of followers:", num_followers)

            account_min_followers = self.comment_filter["account_min_followers"]
            account_max_followers = self.comment_filter["account_max_followers"]

            return num_followers >= account_min_followers and num_followers <= account_max_followers

        except Exception as e:
            print("Get number of followers failed", e)
            return True


    def satisfiesFollowingRequirements(self):

        try:
            sleep(random.random() * 2)
            following = WebDriverWait(self.driver,1).until(EC.presence_of_element_located((By.XPATH, '//li/a[text()=" following"]/span'))).text
            num_following = int(following.replace(",",""))

            print("Num Following:", num_following)
            account_min_following = self.comment_filter['account_min_number_following']
            account_max_following = self.comment_filter['account_max_number_following']


            return num_following >= account_min_following and num_following <= account_max_following

        except Exception as e:
            print("Get number following failed", e)
            return True


    def satisfiesLikeRequirements(self):
        try:
            likes = self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.EDfFK.ygqzn > div > div.Nm9Fw > a > span").text
            likes = int(likes)

            print("Number of likes on post:", likes)
            post_min_likes = self.comment_filter['post_min_number_of_likes']
            post_max_likes = self.comment_filter['post_max_number_of_likes']
            return likes >= post_min_likes and likes <= post_max_likes
        except Exception as e:
            print("Get number of likes on post failed",e)
            return True


    def hasKeyPhrasesToAvoid(self):

        try:

            caption = self.driver.find_element_by_css_selector(
                "body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk > ul > div > li > div > div > div.C4VMK > span"
                ).text

            print("Caption:", caption)


            for phrase in self.comment_filter['post_description_avoided_key_phrases']:
                if phrase in caption:
                    return True
            return False
        except Exception as e:
            print("Failure with getting caption phrases:",e)
            return False

    def acctDescHasKeyPhrasesToAvoid(self):
        try:

            acct_description = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/span').text
            print("Account description:", acct_description)

            for phrase in self.comment_filter['account_description_avoided_key_phrases']:
                if phrase in acct_description:
                    return True
            return False


        except Exception as e:
            #print("Could not read account description:",e)
            return False

    def getNumberOfCommentsOnPost(self):

        try:

            post = self.driver.find_elements_by_class_name("eLAPa")[0]
            hover = ActionChains(self.driver).move_to_element(post)
            hover.perform()
            num_comments = self.driver.find_elements_by_css_selector("ul.Ln-UN > li")
            if len(num_comments) > 1:
                num_comments = num_comments[1].text
            else:
                num_comments = num_comments[0].text

            print("Number of comments on post:", num_comments)
            sleep(random.random() * 2)

            tab = self.driver.find_element_by_css_selector("div.fx7hk")
            ActionChains(self.driver).move_to_element(tab).perform()
            return int(num_comments)


        except Exception as e:
            print("Could not get number of comments on post",e)
            return -1

    def postSatisfiesNumCommentsFilter(self):

        num_comments = self.getNumberOfCommentsOnPost()
        if num_comments == -1:
            return True

        return num_comments >= self.comment_filter['post_min_number_of_comments'] \
                and num_comments <= self.comment_filter['post_max_number_of_comments']


    def quit(self):
        self.driver.quit()


def lambda_handler(event, context):

    print("We got this far>>>>")
    response = {}
    response["statusCode"] = 200
    response["body"] = "We getting there!"
    response["headers"] = {}
    response["isBase64Encoded"] = False

    user1 = 'streetwearlatest'
    user1_pass = 'Julia26'
    main1 = 'genuineaesthetic'
    main1_pass = 'MagicJohnson32!'


    try:
        print(event)

        if ('body' in event):
            print("Getting event body>>>")
            # print(event["body"])
            body = event['body']
            try:
                body = json.loads(event["body"])
            except:
                print("No need for JSON loads")

            print("Body:",body)

            pool = [] if not "custom_comments" in body else body["custom_comments"]
            num_comments = 6 if not "num_comments" in body else body["num_comments"]
            promo_target_accounts_list = body["promo_target_accounts_list"]

            print("Targets:", promo_target_accounts_list)

            if num_comments > 15:
                num_comments = 6

            print("NC: ", num_comments)

            ig_bot = InstagramBot(body["promo_username"], body["promo_password"],
                                 True, body["proxy"], None, None,
                                  body["accounts_already_commented_on"],pool,
                                  num_comments, body["is_liking"], promo_target_accounts_list,
                                  body["comment_filter"])

            print("Got past object creation>>>")

            curr_index, curr_target = 0, ig_bot.promo_target_accounts_list[0]
            while ig_bot.comments_done < ig_bot.num_comments:
                print("Current index:",curr_index)
                ig_bot.perform_preprocess() # get brand and follower list
                try:
                    success = ig_bot.doCommentRound()
                except Exception as e:
                    print("Comment round exception...",e)
                    break
                print("Comments Done:",ig_bot.comments_done)
                if not success:
                    break

                curr_index += 1
                if curr_index == len(ig_bot.promo_target_accounts_list): # return to 0th index
                    curr_index = 0
                    break
                else:
                    curr_target = ig_bot.promo_target_accounts_list[curr_index]
                    print("before brand:", ig_bot.brand)
                    ig_bot.brand = curr_target
                    print("after brand:", ig_bot.brand)

                if time.time() > ig_bot.inception_time + PERIOD_OF_TIME:
                    break



            print()
            print("Curr index after while:",curr_index)
            print("Target list before rotation:",ig_bot.promo_target_accounts_list)
            new_target_list = deque(ig_bot.promo_target_accounts_list)
            new_target_list.rotate(-1 * curr_index)
            new_target_list = list(new_target_list)
            print("Target list after rotation:",new_target_list)
            promo_is_liking = (not ig_bot.liking_blocked) and ig_bot.is_liking
            print("Promo is liking:",promo_is_liking)

            failed_last_comment_round = body["failed_last_comment_round"]
            promo_account_limited = False
            if failed_last_comment_round and ig_bot.could_not_comment_popup:
                promo_account_limited = True

            print("Promo account limited:",promo_account_limited)

            try:
                http = urllib3.PoolManager()
                body_for_post = {
                    "promo_username": body["promo_username"],
                    "commented_on_accounts": ig_bot.current_commented_on,
                    "rotated_target_accounts_list": new_target_list,
                    "promo_is_liking": promo_is_liking,
                    "promo_account_limited": promo_account_limited,
                    "failed_last_comment_round": ig_bot.could_not_comment_popup
                }
                body_for_post = json.dumps(body_for_post).encode('utf-8')
                headers_for_post = {
                    'Content-type': 'application/json', 'Accept': 'application/json'}
                r = http.request('POST', "http://34.226.214.56/api/lambdacallback", body=body_for_post,
                                    headers=headers_for_post)
                print(json.loads(r.data))
                print(r.status)
                if int(r.status) != 200:
                    print("Couldn't POST")
                print(body["promo_username"])
                print(body_for_post)

            except Exception as e:
                print("Couldn't POST")
                print(e)

            ig_bot.quit()
            print(ig_bot.current_commented_on)
            print(ig_bot.accounts_already_commented_on)
    except Exception as e:
        print("No event body")
        print(e)

    return response

# lambda_handler(None,None)

if __name__ == '__main__':
    #4th argument indicates whether or not the account is the main account

    user1 = ""
    user1_pass = ""

    user3 =  "username"
    user3_pass = "password"

    main1 = "genuineaesthetic"
    main1_pass = ""

    #ig_bot = InstagramBot(user1, user1_pass, 'zumiez', False)
    #ig_bot = InstagramBot(user2,user2_pass,'fuckit.jp',False)
    #ig_bot = InstagramBot(user3,user3_pass,'heartlessclothingco',False)
    #ig_bot = InstagramBot(user3,user3_pass,'vzn_clothing',False)
    #ig_bot = InstagramBot(user2,user2_pass,'hufworldwide',False)
    #ig_bot = InstagramBot(user2,user2_pass,'bmeboston',False)
    #ig_bot = InstagramBot(user2,user2_pass,'movingto.mars',False)
    #ig_bot = InstagramBot(user1,user1_pass,'scummy__apparel',False)
    ig_bot = InstagramBot(user1,user1_pass,'verborgenstudios',True)
    ig_bot.perform_preprocess()
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
