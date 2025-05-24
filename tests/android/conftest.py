import os
import pytest
from allure_commons._allure import StepContext
from appium.options.android import UiAutomator2Options
from appium import webdriver
from selene import browser, support
from dotenv import load_dotenv

load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')


desired_caps = {
    "platformName": "Android",
    "platformVersion": "15",
    "automationName": "UIAutomator2",
    "appPackage": "ru.ivi.client",
    "appActivity": "ru.ivi.client.activity.MainActivity",
    "autoGrantPermissions": True,
    "udid": 'mnv4zxustsi7z9in',  # номер девайса из adb devices
}

remote_url = os.getenv('remote_url', 'http://127.0.0.1:4723')


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities(desired_caps)
    browser.config.driver = webdriver.Remote(remote_url, options=options)
    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    browser.config._wait_decorator = support._logging.wait_with(context=StepContext)

    yield

    browser.quit()
