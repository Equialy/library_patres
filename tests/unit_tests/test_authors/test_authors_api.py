import pytest
from httpx import AsyncClient


async def test_get_all_authors(ac_client: AsyncClient):
    response = await ac_client.get("/authors/all_authors")
    assert response.status_code == 200


@pytest.mark.parametrize("id, status_code", [
    (1, 200),
    (0, 404),
    (-1, 404),

], )
async def test_get_authors_by_id(id, status_code, ac_client: AsyncClient):
    response = await ac_client.get(f"/authors/author_id/{id}")
    assert response.status_code == status_code


@pytest.mark.parametrize("name, second_name, birthday, biography, status_code", [
    ("test1", "test_second_name1", "1800-01-01", "писатель", 200),
    ("test2", "test_second_name2", "1800-01-01", "писатель", 200),
    ("test3", "test_second_name3", "1800-01-01", "писатель", 200),
], )
async def test_create_authors(name, second_name, birthday, biography, status_code, ac_client: AsyncClient):
    response = await ac_client.post("/authors/add_author", json={
        "name": name,
        "second_name": second_name,
        "birthday": birthday,
        "biography": biography
    })
    assert response.status_code == 200


@pytest.mark.parametrize("id, name, second_name, birthday, biography, status_code", [
    (6, "testtest1", "test_second_name1", "1800-01-01", "писатель", 200),
    (7, "testtest2", "test_second_name2", "1800-01-01", "писатель", 200),
    (8, "testtest3", "test_second_name3", "1800-01-01", "писатель", 200),
    (0, "testtest3", "test_second_name3", "1800-01-01", "pisatel", 404),
], )
async def test_update_authors(id, name, second_name, birthday, biography, status_code, ac_client: AsyncClient):
    response = await ac_client.put(f"/authors/update_author/{id}", json={
        "name": name,
        "second_name": second_name,
        "birthday": birthday,
        "biography": biography
    })
    assert response.status_code == status_code


