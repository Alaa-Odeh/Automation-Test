import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from infra.browser_wrapper import BrowserWrapper
from logic.home_page import HomePage
from logic.list_of_suggestion_page import SuggestedPage
from logic.login_page import LoginPage
from logic.video_page import VideoPythonProgramming


class list_of_suggestions_page_test(unittest.TestCase):

    # Since most cases need a already logged in account,
    # the setup does contain the login flow
    # for this test we need a suggestion list as a result of a search input
    #thus the search flow is setup in advanced
    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_diver("https://accounts.google.com/InteractiveLogin/signinchooser?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&ec=65620&hl=en&passive=true&service=youtube&uilel=3&ifkv=ATuJsjxsk9AXkrb-s8g0LVQRmzleFNpCW8kJ8t7PLCWF6QUB9c4HKtHjSLQF96Y6_2E9d3LTFjtA&theme=glif&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        self.login_page = LoginPage(self.driver)
        self.login_page.enter_email_password("ofriend31@gmail.com", 'TesterOlaYoutube')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="logo-icon"]')))
        self.home_page = HomePage(self.driver)
        self.home_page.search_flow("python programming")
        self.suggested_video = SuggestedPage(self.driver)

    def tearDown(self):
        self.driver.quit()



    # here we verify the filter video Under 4 minutes is actually applied
    #and a only list of video under 4 minutes are shown

    def test_video_length_fillter_button(self):
        self.suggested_video.click_filter_by_video_length()

        minute= self.suggested_video.find_video_length()
        self.assertLessEqual(int(minute),4,"The filter video under 4 minutes is not working")
