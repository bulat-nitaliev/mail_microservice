from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    EMAIL_HOST_USER: str
    EMAIL_HOST: str
    EMAIL_PORT: str
    EMAIL_HOST_PASSWORD: str
    BROKER_URL: str
