from pydantic_settings import BaseSettings


class Config(BaseSettings):
    base_url: str = 'https://ivi.tv'
    hold_driver_at_exit: bool = False
    window_width: int = 1900
    window_height: int = 1200
    timeout: float = 3.0

config = Config()

