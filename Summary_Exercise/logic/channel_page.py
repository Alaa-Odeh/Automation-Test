from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class ChannelPage(BasePage):
    SUBSCRIPTION_BUTTON_IN_THE_CHANNEL='//div[contains(text(),"Subscribed")]'


    def __init__(self,driver):
        super().__init__(driver)
        self.subscribe_button=self._driver.find_element(By.XPATH,self.SUBSCRIPTION_BUTTON_IN_THE_CHANNEL)

