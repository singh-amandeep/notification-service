from pydantic import BaseSettings

class Settings(BaseSettings):
    SMTP_HOST: str
    SMTP_PORT: str
    SMTP_USER: str
    SMTP_PASSWORD: str
    FROM_EMAIL: str

    class Config:
        env_file = ".env"

settings = Settings()
