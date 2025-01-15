from fastapi import APIRouter, Depends, HTTPException, status

from src.api.depends import get_user_service, get_current_user
from src.services.users_service.JWTauth import HashService
from src.services.users_service.users import UsersSchemaAdd

router = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
)


@router.post("/register")
async def register_user(user_data: UsersSchemaAdd, user_service: get_user_service):
    user_exist = await user_service.user_if_exist(username=user_data.username)
    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    hashed_password = HashService().get_password_hash(user_data.hashed_password)
    result = await user_service.user_registration(username=user_data.username,
                                                  hashed_password=hashed_password,
                                                  role=user_data.role)

    return {"result": result}


@router.get("/all_users", summary="Просмотр всех пользователей")
async def get_users_for_admin(users_service: get_user_service, current_user=Depends(get_current_user)):
    """

    Возвращается список всех пользователь только если у пользователя стоит роль admin. \n
    Для пользователь с ролью user возвращается 403 Forbidden
    """
    users_get = await users_service.get_all_users(current_user)
    return {"all_users": users_get}


@router.post("/update_user")
async def update_user(update_data: UsersSchemaAdd, user_service: get_user_service,
                      current_user=Depends(get_current_user)):
    user_exist = await user_service.user_if_exist(username=update_data.username)
    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    hashed_password = HashService().get_password_hash(update_data.hashed_password)
    update_user_data = await user_service.update_user_data(current_user,
                                                           username=update_data.username,
                                                           hashed_password=hashed_password,
                                                           role=update_data.role)
    return {'result': update_user_data}


@router.get("/me")
async def me(current_user=Depends(get_current_user)):
    return {'result': current_user}
