from fastapi import HTTPException, status
from sqlalchemy import select, delete
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.repository import AbstractRepository


class SQLAlchemyRepository(AbstractRepository):

    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, **data: dict):
        item_model = self.model(**data)
        self.session.add(item_model)
        await self.session.flush()
        return item_model.to_read_model()

    async def get_by_id(self, id: int):
        stmt = select(self.model).where(self.model.id == id)
        result = await self.session.execute(stmt)
        try:
            return result.scalar_one()
        except NoResultFound:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    async def find_all(self) -> list:
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return [row[0].to_read_model() for row in result.all()]

    async def delete(self, item_id):
        stmt = delete(self.model).where(self.model.id == item_id).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalar_one()