#config.py 
# Reference: https://www.fastapitutorial.com/blog/fastapi-hello-world/

import os

class Settings:
    PROJECT_NAME:str = "MBdgt"
    PROJECT_VERSION: str = "1.0.0"
    POSTGRES_PORT=5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_DB: str = os.environ.get("DATABASE_PWD", "app")
    POSTGRES_PASSWORD: str = os.environ.get("DATABASE_PWD", "supersecretpassword")
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:{POSTGRES_PORT}/{POSTGRES_DB}"


'''docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres'''
settings = Settings()