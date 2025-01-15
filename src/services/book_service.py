from src.repositories.books import BooksRepository
from src.schemas.books import BookSchema, BooksSchemaUpdate, BooksCartAdd


class BookService:
    def __init__(self, book_repo: BooksRepository):
        self.book_repo: BooksRepository = book_repo

    async def find_all_books(self) -> list[BookSchema]:
        book_result = await self.book_repo.find_all()
        return book_result

    async def add_book(self, book: BooksCartAdd):
        book_result = {}
        for i in book.cart:
            book_dict = i.model_dump()
            book_result = await self.book_repo.add(**book_dict)
        return book_result

    async def get_book_pagination(self, page: int, page_size: int, filters):
        return await self.book_repo.get_book_paginate(page, page_size, filters)

    async def get_book_by_id(self, id: int) -> BookSchema:
        book_result = await self.book_repo.get_by_id(id)
        return book_result

    async def update_book(self, id_book, book: BooksSchemaUpdate):
        return await self.book_repo.update(id_book, book)

    async def delete_books_by_id(self, book_id: int) -> BookSchema:
        book_result = await self.book_repo.delete(book_id)
        return book_result
