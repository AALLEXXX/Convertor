from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    EXCHANGERATE_API_KEY: str
    MONGODB_URL: str
    MONGODB_DATABASE: str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()