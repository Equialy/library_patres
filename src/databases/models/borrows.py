from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from src.databases.postgres.connect_db import Base
from src.schemas.borrows import BorrowSchema


class Borrows(Base):
    __tablename__ = "borrows"

    id: Mapped[int] =  mapped_column(primary_key=True)
    id_book: Mapped[int] = mapped_column(ForeignKey("books.id", ondelete="CASCADE" ), nullable=False)
    name_reader: Mapped[str] = mapped_column(nullable=False, index=True)
    date_borrow: Mapped[date] = mapped_column( nullable=True)
    date_return: Mapped[date] = mapped_column( nullable=True)
    book: Mapped["Books"] = relationship("Books", back_populates="borrows")

    def to_read_model(self) -> BorrowSchema:
        return BorrowSchema(
            id=self.id,
            id_book=self.id_book,
            name_reader=self.name_reader,
            date_borrow=self.date_borrow,
            date_return=self.date_return
        )