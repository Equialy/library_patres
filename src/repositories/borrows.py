from fastapi import HTTPException, status
from sqlalchemy import update, insert, delete, select, func

from src.databases.models.books import Books
from src.databases.models.borrows import Borrows
from src.repositories.base import SQLAlchemyRepository
from src.schemas.borrows import BorrowsSchemaReturn, BorrowSchemaAdd, BorrowSchema


class BorrowsRepository(SQLAlchemyRepository):
    model = Borrows

    async def _is_correct_count_books(self, username: str) -> bool:
        """
        Проверяет, сколько книг уже выдано пользователю.
        Возвращает True, если выдано менее 5 книг, иначе False.
        """
        stmt = (
            select(func.count(self.model.id))
            .where(self.model.name_reader == username)
            .where(self.model.date_return.is_(None))  # Только незакрытые записи
        )
        result = await self.session.execute(stmt)
        count = result.scalar_one()  # Получить количество выданных книг
        return count < 5

    async def add(self, data: BorrowSchemaAdd, current_user) -> BorrowSchema:
        borrow_data = data.model_dump()
        borrow_data["name_reader"] = current_user.username
        if not await self._is_correct_count_books(borrow_data["name_reader"]):
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)

        query_add_borrow = insert(self.model).values(borrow_data).returning(self.model)
        query_update_book = update(Books).where(Books.id == data.id_book).values(quantity=Books.quantity - 1)
        result_add = await self.session.execute(query_add_borrow)
        await self.session.execute(query_update_book)

        return result_add.scalar_one().to_read_model()


    async def delete(self, data_id: int) -> BorrowSchema:
        stmt = delete(self.model).where(self.model.id == data_id).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalar_one().to_read_model()


    async def return_borrows(self,  date_return: BorrowsSchemaReturn, username) -> BorrowSchema:
        stmt_check = (
            select(self.model)
            .where(self.model.name_reader == username)
            .where(self.model.id_book == date_return.id_book)
            .where(self.model.date_return.is_(None))
        )
        result = await self.session.execute(stmt_check)
        borrow_records = result.scalars().all()
        if not borrow_records:
            raise ValueError("Книга не найдена или уже возвращена.")

        query_update_borrow = update(self.model).where(self.model.id == borrow_records[0].id).where(self.model.date_return.is_(None)).values(date_return=date_return.date_return).returning(self.model)
        query_update_book = update(Books).where(Books.id == date_return.id_book).values(quantity=Books.quantity + 1)
        result_borrow = await self.session.execute(query_update_borrow)
        await self.session.execute(query_update_book)
        return result_borrow.scalar_one().to_read_model()
