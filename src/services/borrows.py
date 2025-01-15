from fastapi import HTTPException, status

from src.repositories.borrows import BorrowsRepository
from src.schemas.borrows import BorrowSchemaAdd, BorrowSchema


class BorrowsService:
    def __init__(self, borrow_repo: BorrowsRepository):
        self.borrow_repo: BorrowsRepository = borrow_repo

    def _validate_borrow_id(self, borrow_id: int):
        if borrow_id <= 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    async def add_borrow(self, borrow_data: BorrowSchemaAdd, current_user) -> BorrowSchema:
        borrow_result = await self.borrow_repo.add(borrow_data, current_user)
        return borrow_result

    async def find_all_borrows(self) -> list[BorrowSchema]:
        result = await self.borrow_repo.find_all()
        return result

    async def return_borrows_by_id(self, date_return, current_user) -> BorrowSchema:
        username = current_user.username
        if date_return.date_return is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        try:
            result = await self.borrow_repo.return_borrows(date_return, username)
        except ValueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        return result

    async def delete_borrows_by_id(self, id_borrow: int) -> BorrowSchema:
        self._validate_borrow_id(id_borrow)
        result = await self.borrow_repo.delete(id_borrow)
        return result
