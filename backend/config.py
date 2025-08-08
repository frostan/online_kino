from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


class Settings(BaseSettings):
    DB_URL: str
    SECRET_KEY: str

    BASE_DIR: Path = Path(__file__).parent.resolve()
    MEDIA_DIR: Path = BASE_DIR / 'media'

    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', extra='ignore'
    )


settings = Settings()
