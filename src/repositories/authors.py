from sqlalchemy import select, update

from src.databases.models.authors import Authors
from src.repositories.base import SQLAlchemyRepository
from fastapi import HTTPException, status

from src.schemas.authors import AuthorsSchemaUpdate



class AuthorsRepository(SQLAlchemyRepository):
    model = Authors

    async def update(self, author_id: int, data: AuthorsSchemaUpdate):
        query_select = select(self.model).filter_by(id=author_id)
        execute_query = await self.session.execute(query_select)
        result = execute_query.scalar_one_or_none()

        if result == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        query_author = select(Authors).filter_by(id=author_id)
        execute_author = await self.session.execute(query_author)
        result_author = execute_author.scalar_one_or_none()

        if result_author == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        query = update(self.model).where(self.model.id == author_id).values(data.model_dump()).execution_options(
            synchronize_session="fetch")
        result = await self.session.execute(query)
        await self.session.commit()

        if result.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return result.scalar_one_or_none()