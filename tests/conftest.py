import asyncio
import json
from datetime import datetime
import pytest
from sqlalchemy import insert
from httpx import AsyncClient, ASGITransport
from src.main import app as fastapi_app

from src.databases.models.authors import Authors
from src.databases.models.books import Books
from src.databases.models.borrows import Borrows
from src.databases.postgres.connect_db import Base, engine, async_session_maker


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"tests/mock_{model}.json", encoding="utf-8") as file:
            return json.load(file)

    authors = open_mock_json("authors")
    books = open_mock_json("books")
    borrows = open_mock_json("borrows")

    for author in authors:
        if author["birthday"]:
            author["birthday"] = datetime.strptime(author["birthday"], "%Y-%m-%d")

    for borrow in borrows:
        if borrow["date_borrow"]:
            borrow["date_borrow"] = datetime.strptime(borrow["date_borrow"], "%Y-%m-%d")
        if borrow["date_return"]:
            borrow["date_return"] = datetime.strptime(borrow["date_return"], "%Y-%m-%d")


    async with async_session_maker() as session:
        add_authors = insert(Authors).values(authors)
        add_books = insert(Books).values(books)
        add_borrows = insert(Borrows).values(borrows)

        await session.execute(add_authors)
        await session.execute(add_books)
        await session.execute(add_borrows)
        await session.commit()



# документация pytest-asyncio
@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def ac_client():
    async with AsyncClient(transport=ASGITransport(app=fastapi_app), base_url="http://test") as ac:
        yield ac


