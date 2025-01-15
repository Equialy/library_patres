from sqlalchemy.orm import Mapped, mapped_column

from src.databases.postgres.connect_db import Base
from src.services.users_service.users import UsersSchema


class Users(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False)

    def to_read_model(self) -> UsersSchema:
        return UsersSchema(
            id=self.id,
            username=self.username,
            hashed_password=self.hashed_password,
            role=self.role
        )
