from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from src.repositories.users import UsersRepository

oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/token")


class UsersService:

    def __init__(self, user_repo: UsersRepository):
        self.user_repo: UsersRepository = user_repo

    async def get_all_users(self, current_user):
        if current_user.role == 'admin':
            return await self.user_repo.find_all()
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    async def user_if_exist(self, **user_data):
        result = await self.user_repo.get_one_or_none(**user_data)
        return result

    async def update_user_data(self, current_user, **update_data):
        result = await self.user_repo.update(current_user, **update_data)
        return result

    async def user_registration(self, **user_data):
        result = await self.user_repo.add(**user_data)
        return result
