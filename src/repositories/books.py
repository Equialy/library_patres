from sqlalchemy import select, update
from fastapi import HTTPException, status
from sqlalchemy.orm import joinedload

from src.databases.models.authors import Authors
from src.databases.models.books import Books
from src.repositories.base import SQLAlchemyRepository
from src.schemas.books import BooksSchemaUpdate


class BooksRepository(SQLAlchemyRepository):
    model = Books




    async def get_book_paginate(self, page: int, page_size: int, genre: str = None):
        stmt = select(self.model)
        if genre:
            stmt = stmt.filter(self.model.genre == genre)
        stmt = stmt.offset(page * page_size).limit(page_size)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def update(self, record_id: int, data: BooksSchemaUpdate):
        query_select = select(self.model).filter_by(id=record_id)
        execute_query = await self.session.execute(query_select)
        result = execute_query.scalar_one_or_none()

        if result == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        query_author = select(Authors).filter_by(id=data.id_author)
        execute_author = await self.session.execute(query_author)
        result_author = execute_author.scalar_one_or_none()

        if result_author == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        query = update(self.model).where(self.model.id == record_id).values(data.model_dump()).execution_options(
            synchronize_session="fetch")
        result = await self.session.execute(query)
        await self.session.commit()

        if result.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return result.scalar_one_or_none()

