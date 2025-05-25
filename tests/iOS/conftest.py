import os
import pytest
from allure_commons._allure import StepContext
from appium import webdriver
from appium.options.ios import XCUITestOptions
from dotenv import load_dotenv
from selene import browser, support

import config

load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

desired_caps = {
    "platformName": "ios",
    "appium:automationName": "XCUITest",
    "appium:udid": "00008030-0003555A0212202E",
    "appium:bundleId": "ru.ivi",
    "noReset": False
}

remote_url = config.remote_url

@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = XCUITestOptions().load_capabilities(desired_caps)
    browser.config.driver = webdriver.Remote(remote_url, options=options)
    browser.config.timeout = float(os.getenv('timeout', '15.0'))
    browser.config._wait_decorator = support._logging.wait_with(context=StepContext)

    yield

    browser.quit()