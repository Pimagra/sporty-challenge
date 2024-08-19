from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TwitchResultsPage(BasePage):
    FIRST_STREAMER = (By.CSS_SELECTOR, "section div:last-of-type a h2")
    PEOPLE_SEARCHING_FOR_LABEL = (By.XPATH, "//h2[contains(text(), 'People searching for')]")
    CHANNELS_LABEL = (By.XPATH, "//h2[text() = 'CHANNELS']")
    VIEW_ALL_CHANNELS_BUTTON = (By.XPATH, "//h2[text() = 'CHANNELS']/..//p[text() = 'View All']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until_element_is_displayed(self.FIRST_STREAMER)
        self.wait_until_element_is_displayed(self.PEOPLE_SEARCHING_FOR_LABEL)

    def click_on_first_streamer(self):
        self.click(self.FIRST_STREAMER)

    def focus_results(self):
        self.click(self.CHANNELS_LABEL)

    def click_on_view_all_channels(self):
        self.click(self.VIEW_ALL_CHANNELS_BUTTON)

