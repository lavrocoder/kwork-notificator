from pathlib import Path

from pydantic_settings import SettingsConfigDict, BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / 'data'
DATA_DIR.mkdir(parents=True, exist_ok=True)

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", env_file_encoding="utf-8")

    TELEGRAM_TOKEN: str = None
    USER_ID: int = None
    DATABASE_URL: str = "sqlite:///./data/app.db"


settings = Settings()

PARS_URLS = [
    "https://kwork.ru/projects?c=80",
    "https://kwork.ru/projects?c=255",
    "https://kwork.ru/projects?c=41",
]
