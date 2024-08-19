from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TwitchStreamerPage(BasePage):
    VIDEO_PLAYER = (By.CSS_SELECTOR, "div[data-a-target='video-player']")
    FOLLOW_BUTTON = (By.CSS_SELECTOR, "button[data-a-target='follow-button']")
    STREAMER_NAME = (By.XPATH, "//a[contains(@href, 'directory/')]/../../..//p")
    STREAMER_LOGO = (By.CSS_SELECTOR, "img[class*=tw-image-avatar]")
    CHAT_WELCOME_MESSAGE = (By.CSS_SELECTOR, "div[data-a-target='chat-welcome-message']")
    CHAT_AREA = (By.CSS_SELECTOR, "div[data-test-selector='chat-scrollable-area__message-container']")
    LIVE_MESSAGE = (By.XPATH, "//p[text() = 'LIVE']")

    def __init__(self, driver):
        super().__init__(driver)
        # Wait for DOM to be loaded completely
        self.wait_for_dom_complete()
        # Wait for some elements to be displayed
        self.wait_until_element_is_displayed(self.VIDEO_PLAYER)
        self.wait_until_element_is_displayed(self.FOLLOW_BUTTON)
        self.wait_until_element_is_displayed(self.CHAT_WELCOME_MESSAGE)
        self.wait_until_element_is_displayed(self.CHAT_AREA)
        self.wait_until_element_is_displayed(self.LIVE_MESSAGE)

