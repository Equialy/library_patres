from src.api.routers.authors import router as router_authors
from src.api.routers.books import router as router_books
from src.api.routers.borrows import router as router_borrows
from src.api.routers.users import router as router_users
from src.api.routers.auth import router as router_auth

all_routers = [
    router_authors,
    router_books,
    router_borrows,
    router_users,
    router_auth
]