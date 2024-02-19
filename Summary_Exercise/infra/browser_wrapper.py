from selenium import webdriver


class BrowserWrapper:
    def __init__(self):
        self.driver = None
        print("Test Start")

    def get_diver(self,url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        return self.driver
