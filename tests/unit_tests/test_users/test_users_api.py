import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("username,hashed_password,role, status_code", [
    ("test", "123password", "user", 200),
    ("test1", "123password", "admin", 200),
    ("", "123password", "admin", 422),
], )
async def test_register_user(username, hashed_password, role, status_code, ac_client: AsyncClient):
    response = await ac_client.post(f"/users/register", json={
        "username": username,
        "hashed_password": hashed_password,
        "role": role
    })
    assert response.status_code == status_code


@pytest.mark.parametrize("username,hashed_password,role, status_code", [
    ("test1", "123password", "user", 401),
    ("test11", "123password", "admin", 401),
], )
async def test_update_user(username, hashed_password, role, status_code, ac_client: AsyncClient):
    """ Если пользователь не уатентифицирован 401 ошибка
        409 Конфликт. Пользователь уже существует"""
    response = await ac_client.post(f"/users/update_user", json={
        "username": username,
        "hashed_password": hashed_password,
        "role": role
    })
    assert response.status_code == status_code
