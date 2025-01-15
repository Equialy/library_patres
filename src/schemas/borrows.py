from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class BorrowSchema(BaseModel):
    id: int = Field(..., ge=1)
    id_book: int = Field(..., ge=1)
    name_reader: str = Field(..., min_length=1, max_length=100)
    date_borrow: date = Field(..., le=date.today())
    date_return: Optional[date]

    class Config:
        from_attributes = True


class BorrowSchemaAdd(BaseModel):
    id_book: int = Field(..., ge=1)
    date_borrow: date = Field(..., le=date.today())

    class Config:
        from_attributes = True


class BorrowsSchemaUpdate(BaseModel):
    date_return: Optional[date]


class BorrowsSchemaDelete(BaseModel):
    id: int = Field(..., ge=1)


class BorrowsSchemaDateReturn(BaseModel):
    id_book: int = Field(..., ge=1)
    date_borrow: date


class BorrowsSchemaReturn(BaseModel):
    id_book: int = Field(..., ge=1)
    date_return: date = Field(..., le=date.today())

    class Config:
        from_attributes = True


class BorrowsSchemaId(BaseModel):
    id: int = Field(..., ge=1)

    class Config:
        from_attributes = True
