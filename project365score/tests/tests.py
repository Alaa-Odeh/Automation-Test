import unittest
import concurrent
from concurrent import futures
import unittest
from selenium import webdriver
from infra.browser_wrapper import BrowserWrapper
from logic.home_page_eng import HomePage
from selenium.webdriver.firefox.options import Options

class home_page_tests(unittest.TestCase):

    def setUp(self):
        self.test_cases = [self.search_league,self.test_add_league_to_favorits,self.test_add_game_to_favorits]
        self.browser=BrowserWrapper()

    def test_run(self):
        self.browser.get_driver(self.test_cases)
        self._driver=self.browser._driver
        self.homepage_page = HomePage(self._driver)

    def tearDown(self):
        self.browser._driver.quit()

    def test_add_game_to_favorits(self):
        self.homepage_page.add_league_upcoming_game()
        self.assertEqual(self.homepage_page.add_to_favorite.get_attribute("src"),"https://res.365scores.com/static/media/star-unactive.91152aeafa73736f37faeb042e98f304.svg","Not Tha Same League Name")

    def test_add_league_to_favorits(self):
        self.homepage_page.add_to_favorits_and_check_updated_list()
        self.assertEqual(self.homepage_page.add_to_favorite.get_attribute("src"),"https://res.365scores.com/static/media/star-active.8195e94059ff5b51062e218ae3e7c9aa.svg","Not Tha Same League Name")

    def search_league(self):
        self.homepage_page.search_group_name("ריאל מדריד")
        self.assertIn("ריאל מדריד",self.homepage_page.page_header.text,"Not The Correct Page")





