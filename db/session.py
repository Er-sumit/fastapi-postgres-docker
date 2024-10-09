# https://www.fastapitutorial.com/blog/database-connection-fastapi/
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Connecting to Database ", settings.DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# if you don't want to install postgres or any database, use sqlite, a file system based database,
# uncomment below lines if you would like to use sqlite and comment above 2 lines of SQLALCHEMY_DATABASE_URL AND engine

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
During tests, we would want a different database and during development/production, our DB would be completely different.
This can be achieved by using dependency injection. For this we would create a dependency called 'get_db' which would guide our database connection.
During unit testing, we would override this 'get_db' dependency and we would get connected to some other test database.
https://www.fastapitutorial.com/blog/dependencies-in-fastapi/
"""


def get_db() -> Generator:  # new
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


"""
 this setup allows you to obtain database sessions using the get_db function. The session is automatically closed when it's no longer needed, ensuring proper handling of database connections. Additionally, the use of a generator function enables efficient resource management, especially in asynchronous environments.
"""
