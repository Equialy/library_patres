from src.repositories.authors import AuthorsRepository
from src.schemas.authors import AuthorsSchema, AuthorsSchemaAdd, AuthorsSchemaUpdate


class AuthorService:
    def __init__(self, item_repo: AuthorsRepository):
        self.item_repo: AuthorsRepository = item_repo

    async def add_item(self, item: AuthorsSchemaAdd) -> AuthorsSchema:
        item_dict = item.model_dump()
        item_result = await self.item_repo.add(**item_dict)
        return item_result

    async def get_item_by_id(self, id: int) -> AuthorsSchema:
        item_result = await self.item_repo.get_by_id(id)
        return item_result

    async def update_authors(self, id: int, authors: AuthorsSchemaUpdate):
        return await self.item_repo.update(id, authors)

    async def find_all_items(self):
        item_result = await self.item_repo.find_all()
        return item_result

    async def delete_item(self, id: int) -> AuthorsSchema:
        item_result = await self.item_repo.delete(id)
        return item_result
