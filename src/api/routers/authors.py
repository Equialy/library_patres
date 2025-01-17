from fastapi import APIRouter
import logging
from src.api.depends import get_author_service
from src.schemas.authors import AuthorsSchemaAdd,  AuthorsSchema, AuthorsSchemaUpdate

router = APIRouter(
    tags=["Авторы"],
    prefix="/authors",
)


logger = logging.getLogger('authors_logger')

@router.post("/add_author", summary="Добавление нового автора")
async def create_authors(item: AuthorsSchemaAdd, author_service: get_author_service) -> dict[str, AuthorsSchema]:
    logger.info("INFO LOG")
    item_result = await author_service.add_item(item)
    return {"authors_add": item_result}


@router.get("/all_authors", summary="Получить всех авторов")
async def get_all_authors(author_service: get_author_service) -> dict[str, list[AuthorsSchema]]:
    logger.info("Возвращаем всех авторов ")
    result = await author_service.find_all_items()
    return {"all_authors": result}


@router.get("/author_id/{id}", summary="Получить автора по id")
async def get_authors_by_id(id: int, author_service: get_author_service) -> dict[str, AuthorsSchema]:
    result = await author_service.get_item_by_id(id)
    return {"author": result}


@router.put("/update_author/{id}", summary="Обновить данные книги")
async def update_authors(id: int, data: AuthorsSchemaUpdate, author_service: get_author_service):
    return await author_service.update_authors(id, data)


@router.delete("/delete_author/{id}", summary="Удаление автора")
async def delete_authors(id: int, author_service: get_author_service) -> dict[str, AuthorsSchema]:
    """
    :param id: ID Автора
    :return: Данные автора \n
    При удалении автора из таблицы autors удаляется запись с автором. \n
    В таблице books в поле id_autor ставится значение null
    """
    result = await author_service.delete_item(id)
    logger.debug("Удаление авторов ", result)
    return {"author_del": result}
