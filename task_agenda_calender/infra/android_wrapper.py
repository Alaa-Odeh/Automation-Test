import json
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options


class AndroidWrapper:

    def __init__(self):
        f = open('../tests/config.json', 'r', encoding='utf-8')
        self.capabilities = json.load(f)
        self.appium_server_url = 'http://localhost:4723'
        self.capabilities_options = UiAutomator2Options().load_capabilities(self.capabilities)
        self._driver = webdriver.Remote(
            command_executor=self.appium_server_url,
            options=self.capabilities_options
        )
        f.close()
