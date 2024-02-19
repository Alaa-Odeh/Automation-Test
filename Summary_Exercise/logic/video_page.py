import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class VideoPythonProgramming(BasePage):
    SUBSCRIPTION_UNDER_VIDEO=('//button[@aria-label="Subscribe to Programming with Mosh."]')
    SUBSCRIBED_BUTTON_TEXT=('//*[@id="notification-preference-button"]/'
                       'ytd-subscription-notification-toggle-button-'
                       'renderer-next/yt-button-shape/button/div[2]/span')
    SUBSCRIBED_BUTTON='//*[@id="notification-preference-button"]//button'
    UNSUBSCRIBE_CHOICE='//*[@id="items"]/ytd-menu-service-item-renderer[4]'
    UNSUBSCRIBE_FINAL='//button[@aria-label="Unsubscribe"]'
    ADD_COMMENT_BUTTON='//*[@id="placeholder-area"]'
    ADD_COMMENT_INPUT='//*[@id="contenteditable-root"]'
    COMMENT_BUTTON='//*[@id="submit-button"]/yt-button-shape/button/div/span'


    def __init__(self,driver):
        super().__init__(driver)
        self.subscribe_button_under_video=self._driver.find_element(By.XPATH,self.SUBSCRIPTION_UNDER_VIDEO)

        while True:
            try:
                self.add_comment_button=self._driver.find_element(By.XPATH,self.ADD_COMMENT_BUTTON)
                break
            except:
                self._driver.execute_script("window.scrollBy(0, 350);")


    def click_on_element(self,element):
        element.click()

    def press_subscribe_button_under_video(self):
        self.click_on_element(self.subscribe_button_under_video)
        self.subscribed_button_text=self._driver.find_element(By.XPATH, self.SUBSCRIBED_BUTTON_TEXT)
        self.subscribed_button=self._driver.find_element(By.XPATH,self.SUBSCRIBED_BUTTON)

    def unsubscribe_button_under_video(self):
        self.click_on_element(self.subscribed_button)
        self.unsubscribed_button=self._driver.find_element(By.XPATH, self.UNSUBSCRIBE_CHOICE)
        self.click_on_element(self.unsubscribed_button)
        self.unsubscribed_final_button=self._driver.find_element(By.XPATH, self.UNSUBSCRIBE_FINAL)
        self.click_on_element(self.unsubscribed_final_button)




    def add_a_comment_flow(self,comment):
        self.add_comment_button.click()
        self.add_comment_input=self._driver.find_element(By.XPATH, self.ADD_COMMENT_INPUT)
        self.add_comment_input.send_keys(comment)
        self.comment_button=self._driver.find_element(By.XPATH, self.COMMENT_BUTTON)




