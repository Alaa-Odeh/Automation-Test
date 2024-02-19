import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from infra.base_page import BasePage


class HomePage(BasePage):
    SERACH_INPUT='//input[@id="search"]'
    PODCASTS_BUTTON='//a//*[contains(text(),"Podcasts")]'
    PODCASTS_PAGE_TITLE=('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse'
                         '/div[3]/ytd-tabbed-page-header/div/div/yt-page-header-'
                         'renderer/yt-page-header-view-model/div/div[1]/div/yt-'
                         'dynamic-text-view-model')

    PROFILE_BUTTON='//button[@id="avatar-btn"]'
    SIDE_BAR='//*[@id="contentWrapper"]'
    LOCATION_BUTTON_ON_THE_MENU='//div//yt-formatted-string[contains(text(),"Location")]'
    AFTER='//div[./yt-formatted-string[contains(text(),"Location")]]//yt-formatted-string[@id="subtitle"]'
    def __init__(self,driver):
        super().__init__(driver)
        self.search_input=self._driver.find_element(By.XPATH,self.SERACH_INPUT)
        self.podcasts_button=self._driver.find_element(By.XPATH,self.PODCASTS_BUTTON)
        self.profile_button=self._driver.find_element(By.XPATH,self.PROFILE_BUTTON)

    def search_flow(self,searchinput):
        self.search_input.send_keys(searchinput)
        self.search_input.send_keys(Keys.ENTER)


    def podcasts_button_click(self):
        self.podcasts_button.click()
        self.podcasts_page_title=self._driver.find_element(By.XPATH,self.PODCASTS_PAGE_TITLE)

    def open_profile_menu_click(self,State,location=None):
        if State=="before":
            self.profile_button.click()
            self.location_on_the_side_menu=self._driver.find_element(By.XPATH,self.LOCATION_BUTTON_ON_THE_MENU)
        elif State=="after":
            self.profile_button=self._driver.find_element(By.XPATH,self.PROFILE_BUTTON).click()
            self.location_after_change=self._driver.find_element(By.XPATH,'//*[contains(text(),"{}")]'.format(location))
    def click_on_location_menu(self,choosen_location):
        self.location_on_the_side_menu.click()
        time.sleep(3)
        self. choose_location= self._driver.find_element(By.XPATH,'//yt-formatted-string[contains(text(),"{}")]'.format(choosen_location))
        time.sleep(3)
        self.choose_location.click()

