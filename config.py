import os

from appium.options.android import UiAutomator2Options
from pydantic_settings import BaseSettings

import utils


class Config(BaseSettings):
    base_url: str = 'https://ivi.tv'
    hold_driver_at_exit: bool = False
    window_width: int = 1900
    window_height: int = 1200
    timeout: float = 5.0

config = Config()

remote_url = os.getenv('remote_url', 'http://127.0.0.1:4723')
deviceName = os.getenv('deviceName')
appWaitActivity = os.getenv('appWaitActivity', 'org.wikipedia.*')
app = os.getenv('app', './app-alpha-universal-release.apk')
runs_on_bstack = app.startswith('bs://')
if runs_on_bstack:
    remote_url = 'http://hub.browserstack.com/wd/hub'

def driver_options():
    options = UiAutomator2Options()

    if deviceName:
        options.set_capability('deviceName', deviceName)

    if appWaitActivity:
        options.set_capability('appWaitActivity', appWaitActivity)

    options.set_capability('app', (
        app if (app.startswith('/') or runs_on_bstack)
        else utils.file.abs_path_from_project(app)
    ))


    return options
