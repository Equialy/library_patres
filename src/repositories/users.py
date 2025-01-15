from sqlalchemy import select, update

from src.databases.models.users import Users
from src.repositories.base import SQLAlchemyRepository
from src.services.users_service.users import UsersSchemaAdd


class UsersRepository(SQLAlchemyRepository):

    model = Users

    async def get_one_or_none(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_user(self, email: str):
        stmt = select(self.model).where(self.model.email == email)
        query = await self.session.execute(stmt)
        return query.scalar_one_or_none()

    async def update(self, current_user, **update_data):
        stmt = update(self.model).where(self.model.id == current_user.id).values(update_data).returning(self.model)
        query = await self.session.execute(stmt)
        return query.scalar_one_or_none()