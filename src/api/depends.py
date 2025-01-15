from datetime import datetime

from jose import jwt
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, status
from typing import Annotated

from src.databases.postgres.connect_db import get_async_session
from src.repositories.authors import AuthorsRepository
from src.repositories.books import BooksRepository
from src.repositories.borrows import BorrowsRepository
from src.repositories.users import UsersRepository
from src.services.authors import AuthorService
from src.services.book_service import BookService
from src.services.borrows import BorrowsService
from src.services.users import UsersService, oauth2_schema
from src.settings.base import config_jwt


def author_service(session: AsyncSession = Depends(get_async_session)):
    return AuthorService(AuthorsRepository(session))


get_author_service = Annotated[AuthorService, Depends(author_service)]


def books_service(session: AsyncSession = Depends(get_async_session)):
    return BookService(BooksRepository(session))


get_books_service = Annotated[BookService, Depends(books_service)]


def borrows_service(session: AsyncSession = Depends(get_async_session)):
    return BorrowsService(BorrowsRepository(session))


get_borrows_service = Annotated[BorrowsService, Depends(borrows_service)]


def user_service(session: AsyncSession = Depends(get_async_session)):
    return UsersService(UsersRepository(session))


get_user_service = Annotated[UsersService, Depends(user_service)]


async def get_current_user(user_service: Annotated[UsersService, Depends(user_service)],
                           token: str = Depends(oauth2_schema)):
    try:
        payload = jwt.decode(token, config_jwt.secret_key, config_jwt.algorithm)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    username: str = payload.get("username")

    if not username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user = await user_service.user_if_exist(username=username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user
