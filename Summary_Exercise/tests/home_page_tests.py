import time
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from infra.browser_wrapper import BrowserWrapper
from logic.home_page import HomePage
from logic.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#Since most cases need a already logged in account,
# the setup does contain the login flow

class youtube_home_page_test(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_diver(
            "https://accounts.google.com/InteractiveLogin/signinchooser?"
            "continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle"
            "_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F"
            "%252Fwww.youtube.com%252F&ec=65620&hl=en&passive=true&service=yout"
            "ube&uilel=3&ifkv=ATuJsjxsk9AXkrb-s8g0LVQRmzleFNpCW8kJ8t7PLCWF6QUB9"
            "c4HKtHjSLQF96Y6_2E9d3LTFjtA&theme=glif&flowName=GlifWebSignIn&flow"
            "Entry=ServiceLogin")
        self.login_page = LoginPage(self.driver)
        self.login_page.enter_email_password("ofriend31@gmail.com",
                                             'TesterOlaYoutube')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="logo-icon"]')))
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()


    #this test verfy the functionality of the podcasts button ,
    # if podcasts button was click (from the side menu) the page
    # should redirect to the podcasts page

    def test_podcast_button(self):
        self.home_page.podcasts_button_click()
        self.assertEqual("Podcasts",self.home_page.podcasts_page_title.text,
                         "Incorrect Page for Podcasts")




    #this test makes sure that once the location on the side menu
    # under the profile icon is switched to Bolivia, it actually is changed
    def test_changing_location_button(self):
        self.home_page.open_profile_menu_click("before")
        self.home_page.click_on_location_menu("Bolivia")
        self.home_page.open_profile_menu_click("after","Bolivia")
        self.assertIn("Bolivia",self.home_page.location_after_change.text,"Incorrect Country")

