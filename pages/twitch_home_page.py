from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TwitchHomePage(BasePage):
    SEARCH_TEXTBOX = (By.CSS_SELECTOR, "input[type='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "a[aria-label='Search']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until_element_is_displayed(self.SEARCH_BUTTON)

    def search(self, value):
        self.click(self.SEARCH_BUTTON)
        self.click(self.SEARCH_TEXTBOX)
        self.fill_text(self.SEARCH_TEXTBOX, value)
        self.send_keys(Keys.ENTER)

