from anyio.functools import lru_cache
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Prompt(BaseModel):
    insight_path: str
    insight_version: str


class OpenAiModel(BaseModel):
    model_name: str
    api_key: str
    temperature: float


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__"
    )

    app_host: str
    app_port: int

    openai_model: OpenAiModel
    prompt: Prompt


@lru_cache()
def get_settings() -> Settings:
    """
    Getter function for app settings
    :return: runtime app settings
    """
    return Settings()
