import time

from selenium.common import TimeoutException
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class HomePage(BasePage):
    DONT_MISS_POPUP="// button[contains(text(), 'בטח')]"
    ACCEPT_BUTTON='//*[@id="didomi-notice-agree-button"]'
    CLOSE_POPUP_BUTTON='//*[@id="modal-root"]/div[1]/div[2]/button'
    ADD_TO_FAVORITE = '//div[@class="all-scores-widget-competition_all_scores_widget_competition_info_star_container__rFuYG"]//img'
    FAVORITE_LEAGUE_GAME="//a[@class='game-card_game_card_link__L3moj game-card_game_card__RpinR game-card_clickable__-fXXf game-card_support_hover__ES-mS']"
    SEARCH_INPUT='//input[@class="main-header-module-desktop-search-input"]'
    GAME_ADD_TO_FAVORITE='//img[@class="star-icon-spin-close clickable"]'
    SUGGESTION='//div[@class="search-widget-item-text-container"]'
    NEW_PAGE_HEADER='//h1[@class="mega-header-module-entity-name"]'

    def __init__(self, driver):
        super().__init__(driver)
    def initial_element(self):

        self.accept_terms = WebDriverWait(self._driver, 10).until(

            EC.visibility_of_element_located((By.XPATH, self.ACCEPT_BUTTON))).click()


        while True:
            try:
                self.close_popup= WebDriverWait(self._driver, 10).until(

                    EC.visibility_of_element_located((By.XPATH, self.CLOSE_POPUP_BUTTON))).click()
                break
            except:
                print("No such widge section")
        self.add_to_favorite=self._driver.find_element(By.XPATH,self.ADD_TO_FAVORITE)
        self.search_input=self._driver.find_element(By.XPATH,self.SEARCH_INPUT)
        self.add_league_game=self._driver.find_element(By.XPATH,self.FAVORITE_LEAGUE_GAME)



    def find_popular_games_and_click_on_it(self):
        self.initial_element()
        self.add_to_favorite.click()

        if isinstance(self._driver, webdriver.Edge):
            pass
        else:
            while True:
                try:
                    self.dont_miss_popup= WebDriverWait(self._driver, 10).until(

                        EC.visibility_of_element_located((By.XPATH, self.DONT_MISS_POPUP))).click()
                    break
                except:
                    print("No such widge section")




    def add_to_favorits_and_check_updated_list(self):
        self.find_popular_games_and_click_on_it()

    def add_league_upcoming_game(self):
        self.initial_element()
        actions = ActionChains(self._driver)
        actions.move_to_element(self.add_league_game).perform()
        self.add_game_to_favorite=self._driver.find_element(By.XPATH, self.GAME_ADD_TO_FAVORITE)

    def search_group_name(self, group_name):
        self.initial_element()
        self.search_input.send_keys(group_name)
        self.first_suggestion=WebDriverWait(self._driver, 12).until(

                        EC.visibility_of_element_located((By.XPATH, self.SUGGESTION))).click()
        self.page_header=WebDriverWait(self._driver, 12).until(

                        EC.visibility_of_element_located((By.XPATH, self.NEW_PAGE_HEADER)))




