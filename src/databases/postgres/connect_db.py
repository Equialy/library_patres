import os

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.settings.base import config_postgres

if os.getenv("TESTING") == "1":
    DB_URL = config_postgres.test_db_postgres_url
    DB_PARAMS = {"poolclass": NullPool}
else:
    DB_URL = config_postgres.postgres_url
    DB_PARAMS = {}

engine = create_async_engine(DB_URL, echo=True)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_async_session():
    async with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()
