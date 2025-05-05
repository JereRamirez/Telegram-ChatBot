from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API settings
    api_port: int = Field(default=8000, env="API_PORT")

    # Database settings
    db_host: str = Field(default="localhost", env="DB_HOST")
    db_port: int = Field(default=5432, env="DB_PORT")
    db_user: str = Field(default="postgres", env="DB_USER")
    db_password: str = Field(default="postgres", env="DB_PASSWORD")
    db_name: str = Field(default="expenses_db", env="DB_NAME")

    # LLM settings
    gemini_api_key: str = Field(default="", env="GEMINI_API_KEY")

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


settings = Settings()