from pydantic import BaseModel, Field, ConfigDict
from datetime import date



class AuthorsSchema(BaseModel):
    id: int = Field(..., ge=1)
    name: str = Field(..., min_length=1, max_length=100)
    second_name: str = Field(..., min_length=1, max_length=100)
    birthday: date = Field(..., le=date.today())
    biography: str = Field(..., min_length=1, max_length=1024)

    model_config = ConfigDict(from_attributes=True)


class AuthorsSchemaAdd(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    second_name: str = Field(..., min_length=1, max_length=100)
    birthday: date = Field(..., le=date.today())
    biography: str = Field(..., min_length=1)

    model_config = ConfigDict(from_attributes=True)


class AuthorsSchemaUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    second_name: str = Field(..., min_length=1, max_length=100)
    birthday: date = Field(..., le=date.today())
    biography: str = Field(..., min_length=1)

    model_config = ConfigDict(from_attributes=True)


class AuthorsSchemaDelete(BaseModel):
    id: int
