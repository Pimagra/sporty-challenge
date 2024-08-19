from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TwitchChannelsResultsPage(BasePage):
    FIRST_CHANNEL = (By.CSS_SELECTOR, "div[role=list] a h2")
    LAST_CHANNEL = (By.CSS_SELECTOR, "div[role=list] div:last-of-type a h2")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until_element_is_displayed(self.FIRST_CHANNEL)

    def click_on_channel(self):
        self.click(self.LAST_CHANNEL)

