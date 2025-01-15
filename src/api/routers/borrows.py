from fastapi import APIRouter, Depends

from src.api.depends import get_borrows_service, get_current_user
from src.schemas.borrows import BorrowSchema, BorrowSchemaAdd, BorrowsSchemaReturn

router = APIRouter(
    prefix="/borrows",
    tags=["Выдача"],
)


@router.get("/all_borrows", summary="Получить все выданные книги")
async def get_all_borrows(borrows_service: get_borrows_service) -> dict[str, list[BorrowSchema]]:
    result = await borrows_service.find_all_borrows()
    return {"all_borrows": result}


@router.post("/add_borrows", summary="Выдать книгу")
async def create_borrows(borrow: BorrowSchemaAdd, borrows_service: get_borrows_service, current_user = Depends(get_current_user) ) -> dict[str, BorrowSchemaAdd]:
    borrow_result = await borrows_service.add_borrow(borrow, current_user)
    return {"borrow": borrow_result}


@router.delete("/delete_borrows/{id}", summary="Удалить выдачу")
async def delete_borrows(id: int, borrows_service: get_borrows_service) -> dict[str, BorrowSchema]:
    """
    :param id:  ID Выдачи \n
    :return: Удаленные данные
    """
    result = await borrows_service.delete_borrows_by_id(id)
    return {"deleted_borrow": result}


@router.patch("/return_borrow", summary="Вернуть книгу")
async def return_borrows( return_data: BorrowsSchemaReturn, borrows_service: get_borrows_service, current_user = Depends(get_current_user)) -> BorrowSchema:
    """
    :param current_user текущий пользователь \n
    :param return_data: ID книги и дата возврата. \n
    Заполняет поле date_return учитывая аутентифицированного пользователя в таблице borrows. \n
    Если все книги возвращены то возвращается Bad request
    """
    result = await borrows_service.return_borrows_by_id( return_data, current_user)
    return result
