import concurrent
from concurrent import futures

from selenium import webdriver
import json

class BrowserWrapper:
    f=open('C:\\Users\\Alaa Oda\\PycharmProjects\\Automation\\project365score\\infra\\config.json','r',encoding='utf')
    CONFIG=json.load(f)
    HUB_URL=CONFIG["hub_url"]

    def __init__(self):
        self._driver = None
        print("Test Start")


    def get_driver(self,test_cases):
        for test_case in test_cases:

            if self.CONFIG["grid"]:
                self.build_cap()

                for caps in self.caps_list:
                        self._driver = webdriver.Remote(command_executor=self.HUB_URL, options=caps)
                        self._driver.get(self.CONFIG["url"])
                        self._driver.set_window_size(1024, 796)
                        self._driver.maximize_window()
                        if self.CONFIG["grid type"] == "serial":
                            test_case()

                        elif self.CONFIG["grid type"] == "parallel":
                            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.caps_list)) as executor:
                                    executor.map(test_case, self.caps_list)

            else:
                if self.CONFIG["browser"]=="Chrome":
                    self._driver= webdriver.Chrome()
                elif self.CONFIG["browser"]=="FireFox":
                    self._driver= webdriver.Firefox()
                elif self.CONFIG["browser"]=="Edge":
                    self._driver= webdriver.Edge()
                self._driver.get(self.CONFIG["url"])
                self._driver.set_window_size(1024, 796)
                self._driver.maximize_window()
                test_case()





    def build_cap(self):
        self.chrome_cap = webdriver.ChromeOptions()
        self.chrome_cap.capabilities['platformName'] = 'Windows 11'

        self.firfox_cap=webdriver.FirefoxOptions()
        self.firfox_cap.capabilities['platformName'] = 'Windows 11'

        self.edge_cap = webdriver.EdgeOptions()
        self.edge_cap.capabilities['platformName'] = 'Windows 11'
        self.caps_list = [self.chrome_cap, self.edge_cap,self.firfox_cap]







