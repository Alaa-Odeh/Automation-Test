import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest

from selenium.webdriver.support.wait import WebDriverWait

from infra.browser_wrapper import BrowserWrapper
from logic.channel_page import ChannelPage
from logic.home_page import HomePage
from logic.list_of_suggestion_page import SuggestedPage
from logic.login_page import LoginPage
from logic.video_page import VideoPythonProgramming


class youtube_page_test(unittest.TestCase):

    # Since most cases need a already logged in account,
    # the setup does contain the login flow
    #although in both test cases i could have setup the
    # page to go directly to the vedio, i choose to make the whole flow
    #login ->homepage-> Enter search input -> choose a video from the
    # suggestion list-> test the video page
    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_diver(
            "https://accounts.google.com/InteractiveLogin/signinchooser?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&ec=65620&hl=en&passive=true&service=youtube&uilel=3&ifkv=ATuJsjxsk9AXkrb-s8g0LVQRmzleFNpCW8kJ8t7PLCWF6QUB9c4HKtHjSLQF96Y6_2E9d3LTFjtA&theme=glif&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        self.login_page = LoginPage(self.driver)
        self.login_page.enter_email_password("ofriend31@gmail.com", 'TesterOlaYoutube')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="logo-icon"]')))
        self.home_page = HomePage(self.driver)
        self.home_page.search_flow("python programming")
        self.suggested_video = SuggestedPage(self.driver)
        self.suggested_video.click_suggestion()
        self.video_page= VideoPythonProgramming(self.driver)


    def tearDown(self):
        self.driver.quit()

    #this test the functionality of the subscription button
    def test_subscription_button(self):
        self.video_page.press_subscribe_button_under_video()
        self.assertIn( "Subscribed",self.video_page.subscribed_button_text.text,"Element Not Found")

        #this function is to reset the subscription button
        self.video_page.unsubscribe_button_under_video()

    #test the option to enter a comment is enabled once a text is entered
    def test_add_comment_for_video(self):
        self.video_page.add_a_comment_flow("Good Job")
        self.assertTrue(self.video_page.comment_button.is_enabled(),"Button is not Enabled")
