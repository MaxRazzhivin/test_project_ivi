import os
from datetime import time


import pytest

from appium import webdriver
from appium.options.ios import XCUITestOptions

desired_caps = dict (

    deviceName = 'iPhone',
    platformName = "iOS",
    platformVersion = '18.4.2',
    automationName = "XCUITest",
    udid = '', #позже уточнить айдишник здесь
    appPackage = "ru.ivi.client",
    appActivity = "ru.ivi.client.activity.MainActivity"
)

remote_url = os.getenv('remote_url', 'http://127.0.0.1:4723/')

@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = XCUITestOptions().load_capabilities(desired_caps)
    driver = webdriver.Remote(remote_url, options=options)


    time.sleep(5)
    driver.quit()