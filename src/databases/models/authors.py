from datetime import date

from sqlalchemy.orm import Mapped, mapped_column

from src.databases.postgres.connect_db import Base
from src.schemas.authors import AuthorsSchema


class Authors(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, index=True)
    second_name: Mapped[str] = mapped_column(nullable=False, index=True)
    birthday: Mapped[date] = mapped_column( nullable=False)
    biography: Mapped[str] = mapped_column(nullable=True)

    def to_read_model(self) -> AuthorsSchema:
        return AuthorsSchema(
            id=self.id,
            name=self.name,
            second_name=self.second_name,
            birthday=self.birthday,
            biography=self.biography
        )