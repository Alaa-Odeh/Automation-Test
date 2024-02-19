from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from infra.base_page import BasePage


class SuggestedPage(BasePage):
    CHOSSEN_VIDEO='//a[@title="Python Tutorial - Python Full Course for Beginners"]'
    FILLTER_BUTTON='//*[@id="filter-button"]/ytd-button-renderer/yt-button-shape/button'
    FILLTER_BY_TODAY='//div[./yt-formatted-string[text()="Under 4 minutes"]]'
    TIMEUPLOAD='/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-search-pyv-renderer[1]/div/ytd-ad-slot-renderer/div/ytd-in-feed-ad-layout-renderer/div/ytd-promoted-video-renderer/div/ytd-thumbnail/a/div[1]/ytd-thumbnail-overlay-time-status-renderer/div/span'

    def __init__(self,driver):
        super().__init__(driver)
        self.find_video=self._driver.find_element(By.XPATH, self.CHOSSEN_VIDEO)
        self.fillter_button = self._driver.find_element(By.XPATH, self.FILLTER_BUTTON)


    def click_suggestion(self):
        self.find_video.click()

    def click_filter_button(self):
        self.fillter_button.click()

    def click_filter_by_video_length(self):
        self.click_filter_button()
        self.fillter_by_today=self._driver.find_element(By.XPATH, self.FILLTER_BY_TODAY)
        self.fillter_by_today.click()

    def find_video_length(self):
        self.video_upload_time=WebDriverWait(self._driver,10).until(EC.visibility_of_element_located((By.XPATH, self.TIMEUPLOAD)))
        self.list_of_time=self.video_upload_time.text.split(':')
        return self.list_of_time[0]

