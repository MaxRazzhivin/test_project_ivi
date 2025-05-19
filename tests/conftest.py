import pytest
from allure_commons._allure import StepContext
from selene import browser, support
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach
import os
from dotenv import load_dotenv

load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        help='Версия браузера в которой будут запущены тесты',
        default='128.0'
    )


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):

    browser.config.base_url = os.getenv('base_url', 'https://ivi.tv')

    #Настройка опций для режима инкогнито
    # options = webdriver.ChromeOptions()
    # options.add_argument('--incognito')

    # Устанавливаем разрешение экрана
    browser.config.window_width = os.getenv('window_width', '1920')
    browser.config.window_height = os.getenv('window_height', '1080')

    browser.config._wait_decorator = support._logging.wait_with(context=StepContext)
    browser.config.timeout = float(os.getenv("timeout", '3.0'))


    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    browser_version = request.config.getoption('--browser_version')
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f'https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub',
        options=options)

    browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
