from fastapi import APIRouter

from src.api.depends import get_books_service
from src.schemas.books import BooksSchemaAdd, BookSchema,  BooksCartAdd

router = APIRouter(
    prefix="/books",
    tags=["Книги"],
)


@router.post("/add_books", summary="Добавление новой книги")
async def create_books(book: BooksCartAdd, books_service: get_books_service) -> dict[str, BooksSchemaAdd]:
    """
    :param book: Добавление одной или нескольких книг сразу
    """
    book_result = await books_service.add_book(book)
    return {"book_result": book_result}


@router.get("/get_books", summary="Получить все книги")
async def get_all_books(books_service: get_books_service,
                        genre: str = None,
                        page: int = 0,
                        page_size: int = 10) -> dict[str, list[BookSchema]]:
    """
    :param genre: Фильтр по жанру. Например 'Роман'. Регистр важен. \n
    :param page: Страница. Выведутся книги только у которых нет значения null в поле id_author \n
    :param page_size: Количесвто  записей на странице
    """

    book_result = await books_service.get_book_pagination(page, page_size, genre)
    return {"all_books": book_result}


@router.get("/books_id/{id}", summary="Получить книгу по id")
async def get_books_by_id(id: int, books_service: get_books_service) -> dict[str, BookSchema]:
    result = await books_service.get_book_by_id(id)
    return {"book": result}


@router.put("/update_book/{id}", summary="Обновить данные книги")
async def update_books(id: int, data: BooksSchemaAdd, books_service: get_books_service):
    return await books_service.update_book(id, data)


@router.delete("/delete_book/{id}", summary="Удаление книги")
async def delete_book(id: int, books_service: get_books_service) -> dict[str, BookSchema]:
    """
    : id книги: \n
    Удаляется запись с книгой из таблицы books и запись выдачи из таблицы borrows
    """
    result = await books_service.delete_books_by_id(id)
    return {"delete_book": result}
