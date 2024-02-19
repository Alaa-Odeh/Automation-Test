from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = '//*[@id="identifierId"]'
    NEXT_BUTTON='//*[@id="identifierNext"]/div/button'
    PASSWORD_INPUT = '//*[@id="password"]/div[1]/div/div[1]/input'
    NEXT_BUTTON_PASSWORD = '//*[@id="passwordNext"]/div/button'


    def __init__(self, driver):
        super().__init__(driver)
        self.email_input = self._driver.find_element(By.XPATH,self.EMAIL_INPUT)
        self.next_button = self._driver.find_element(By.XPATH,self.NEXT_BUTTON)

    def enter_email_password(self,email,password):
        self.email_input.send_keys(email)
        self.next_button.click()
        self.password_input = self._driver.find_element(By.XPATH,self.PASSWORD_INPUT)
        self.next_button_password=self._driver.find_element(By.XPATH,self.NEXT_BUTTON_PASSWORD)
        self.password_input.send_keys(password)
        self.next_button_password.click()



