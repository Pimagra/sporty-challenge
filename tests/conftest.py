from datetime import datetime

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service

from utils.config_parser import ConfigParserIni
from selenium.webdriver.chrome.options import Options


# reads parameters from pytest command line
def pytest_addoption(parser):
  parser.addoption("--browser", action="store", default="mobile", help="browser that the automation will run in")


@pytest.fixture(scope="session")
# instantiates ini file parses object
def prep_properties():
  config_reader = ConfigParserIni("props.ini")
  return config_reader

@pytest.fixture()
# Performs setup and tear down
def create_driver(prep_properties, request):
  global browser, base_url, driver
  browser = request.config.option.browser
  base_url = prep_properties.config_section_dict("AUT")["base_url"]

  if browser == "firefox":
    request.instance.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
  elif browser == "remote":
    capabilities = {
      'browserName': 'firefox',
      'javascriptEnabled': True
    }
    request.instance.driver = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub",
                                               desired_capabilities=capabilities)
  elif browser == "chrome_headless":
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1680, 1050")
    request.instance.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)

  elif browser == 'mobile':
    mobile_emulation = {"deviceName": "Pixel 7"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    request.instance.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
  else:
    request.instance.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

  request.instance.driver.implicitly_wait(60)
  request.instance.driver.maximize_window()
  request.instance.driver.get(base_url)
  yield
  request.instance.driver.quit()

def take_screenshot(driver):
  file_name = f'{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/", "_").replace("::", "__")
  driver.save_screenshot(file_name)