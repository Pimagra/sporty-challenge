import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """ Wrapper for selenium operations """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)
        self.wait_for_dom_complete()

    def click(self, web_element):
        retries = 3
        clicked = False

        while retries > 0 and clicked is False:
            try:
                el = self.wait.until(expected_conditions.element_to_be_clickable(web_element))
                self._highlight_element(el, "green")
                el.click()
                clicked = True
            except Exception:
                print("Error clicking on element. Retrying")
                retries -= 1

    def fill_text(self, web_element, txt):
        el = self.wait.until(expected_conditions.element_to_be_clickable(web_element))
        el.clear()
        self._highlight_element(el, "green")
        el.send_keys(txt)

    def scroll_down(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        # Sleep 1 sec just to show that the scroll works correctly, because it runs too fast
        time.sleep(1)

    def get_text(self, web_element):
        el = self.wait.until(expected_conditions.visibility_of_element_located(web_element))
        self._highlight_element(el, "green")
        return el.text

    def _highlight_element(self, web_element, color):
        original_style = web_element.get_attribute("style")
        new_style = "background-color:lightblue;border: 1px solid " + color + original_style
        self.driver.execute_script(
            "var tmpArguments = arguments;setTimeout(function () {tmpArguments[0].setAttribute('style', '"
            + new_style + "');},0);", web_element)
        self.driver.execute_script(
            "var tmpArguments = arguments;setTimeout(function () {tmpArguments[0].setAttribute('style', '"
            + original_style + "');},400);", web_element)

    def wait_until_element_is_displayed(self, web_element):
        found = False
        retries = 30

        while found is False and retries > 0:
            found = self.is_visible(web_element)
            if found is False:
                retries -= 1

    def is_visible(self, locator):
        self.driver.implicitly_wait(2)
        self.wait = WebDriverWait(self.driver, 2)
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(locator))
            return True
        except (NoSuchElementException, TimeoutException):
            return False
        finally:
            self.driver.implicitly_wait(60)
            self.wait = WebDriverWait(self.driver, 20)

    def wait_for_dom_complete(self):
        try:
            WebDriverWait(self.driver, 60).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
        except TimeoutException as err:
            raise TimeoutError("Page not loaded") from err

    def send_keys(self, key):
        actions = ActionChains(self.driver)
        actions.send_keys(key)
        actions.perform()