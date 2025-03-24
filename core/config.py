# config.py
# Reference: https://www.fastapitutorial.com/blog/fastapi-hello-world/
import logging
import os


class LogConfig:
    logger = logging.getLogger("app_log")


class Settings:
    PROJECT_NAME: str = "MBdgt"
    PROJECT_VERSION: str = "1.0.0"
    POSTGRES_PORT = 5432
    POSTGRES_USER: str = "appuser"
    POSTGRES_DB: str = os.environ.get("DATABASE_PWD", "app")
    POSTGRES_PASSWORD: str = os.environ.get("DATABASE_PWD", "supersecretpassword")
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY: str = os.environ.get("SECRET_KEY", "skufhoweiu098ye879yih")  # new
    ALGORITHM = "HS256"  # new
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # in mins  #new


"""docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres"""
settings = Settings()
log = LogConfig.logger
