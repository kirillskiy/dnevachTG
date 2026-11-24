import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Config:
    bot_token: str
    base_url: str


def load_config() -> Config:
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("Не задан BOT_TOKEN в файле .env")

    base_url = os.getenv("BASE_URL", "https://www.istu.edu/raspisanie/")
    return Config(bot_token=token, base_url=base_url)