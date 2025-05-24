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
