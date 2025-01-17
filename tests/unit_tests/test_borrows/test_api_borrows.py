import pytest
from httpx import AsyncClient


async def test_get_all_borrows(ac_client: AsyncClient):
    response = await ac_client.get("/borrows/all_borrows")
    assert response.status_code == 200


@pytest.mark.parametrize("id_book, date_borrow, status_code", [
    (1, "2024-01-15",  401),
    ( 1, "2024-01-15",  401),
], )
async def test_create_borrows(id_book, date_borrow,  status_code, ac_client: AsyncClient):
    """ 401 Если не авторизирован """
    response = await ac_client.post(f"/borrows/add_borrows", json={
        "id_book": id_book,
        "date_borrow": date_borrow
    })
    assert response.status_code == status_code
