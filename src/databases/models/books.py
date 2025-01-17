from datetime import date

from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.databases.postgres.connect_db import Base
from src.schemas.books import  BookSchema




class Books(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False, index=True)
    describe: Mapped[str] = mapped_column(nullable=False)
    date_publication: Mapped[date] = mapped_column( nullable=False)
    genre: Mapped[str] = mapped_column(nullable=False, index=True)
    id_author: Mapped[int] = mapped_column(ForeignKey("authors.id", ondelete="CASCADE"), nullable=True, index=True)
    quantity: Mapped[int] = mapped_column(nullable=False)
    borrows: Mapped[list["Borrows"]] = relationship("Borrows", back_populates="book", cascade="all, delete-orphan")
    __table_args__ = (
        CheckConstraint("quantity >= 0", name="quantity_non_negative"),
    )

    def to_read_model(self) -> BookSchema:
        return BookSchema(
            id=self.id,
            title=self.title,
            describe=self.describe,
            date_publication=self.date_publication,
            genre=self.genre,
            id_author=self.id_author,
            quantity=self.quantity
        )
