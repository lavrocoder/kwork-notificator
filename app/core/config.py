from pathlib import Path

from pydantic_settings import SettingsConfigDict, BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / 'data'
DATA_DIR.mkdir(parents=True, exist_ok=True)

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", env_file_encoding="utf-8")

    TELEGRAM_TOKEN: str = None
    USER_ID: int = None

    DB_TYPE: str = "sqlite"  # sqlite or postgresql

    # docker run -d --name kwork_db -e POSTGRES_USER=db_user -e POSTGRES_PASSWORD=db_password -e POSTGRES_DB=db_name -p 5432:5432 postgres:16-alpine
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "db_user"
    POSTGRES_PASSWORD: str = "db_password"
    POSTGRES_DB: str = "db_name"

    @property
    def DATABASE_URL(self) -> str:
        if self.DB_TYPE == "sqlite":
            return "sqlite:///./data/app.db"
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


settings = Settings()

PARS_URLS = [
    "https://kwork.ru/projects?c=80",
    "https://kwork.ru/projects?c=255",
    "https://kwork.ru/projects?c=41",
]
