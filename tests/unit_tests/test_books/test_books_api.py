import pytest
from httpx import AsyncClient


async def test_get_all_books(ac_client: AsyncClient):
    response = await ac_client.get("/books/get_books")
    assert response.status_code == 200


@pytest.mark.parametrize("id, status_code", [
    (1, 200),
    (0, 404),
    (-1, 404),

], )
async def test_get_books_by_id(id, status_code, ac_client: AsyncClient):
    response = await ac_client.get(f"/books/books_id/{id}")
    assert response.status_code == status_code


@pytest.mark.parametrize("title, describe, id_author, date_publication, genre, quantity, status_code", [
    ("book1", "book_test", 3, "1801-01-01", "Роман", 5, 200),
    ("book2", "book_test2", 4, "1800-01-01", "Роман", 7, 200),
    ("", "book_test2", 4, "1800-01-01", "Роман", 7, 422),
], )
async def test_create_books(title, describe, id_author, date_publication, genre, quantity, status_code,
                            ac_client: AsyncClient):
    response = await ac_client.post("/books/add_books", json={
        "cart": [
            {
                "title": title,
                "describe": describe,
                "id_author": id_author,
                "date_publication": date_publication,
                "genre": genre,
                "quantity": quantity
            }
        ]
    })
    assert response.status_code == status_code


@pytest.mark.parametrize("id, title, describe, id_author, date_publication,genre, quantity, status_code", [
    (3, "book15", "book_test", 3, "1801-01-01", "Роман", 5, 200),
    (4, "book", "book_test2", 4, "1800-01-01", "Роман", 7, 200),
], )
async def test_update_book(id, title, describe, id_author, date_publication, genre, quantity, status_code,
                           ac_client: AsyncClient):
    response = await ac_client.put(f"/books/update_book/{id}", json={
        "title": title,
        "describe": describe,
        "id_author": id_author,
        "date_publication": date_publication,
        "genre": genre,
        "quantity": quantity
    })
    assert response.status_code == status_code
