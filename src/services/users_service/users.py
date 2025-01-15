from pydantic import BaseModel,  Field


class UsersSchema(BaseModel):
    id: int = Field(..., ge=1)
    username: str = Field(..., max_length=255)
    hashed_password: str = Field(..., min_length=4, max_length=255)
    role: str = Field(..., min_length=4, max_length=255)

    class Config:
        from_attributes = True


class UsersSchemaAdd(BaseModel):
    username: str = Field(..., min_length=1, max_length=255)
    hashed_password: str = Field(..., min_length=4, max_length=255)
    role: str = Field(..., min_length=4, max_length=255)

    class Config:
        from_attributes = True


class UsersSchemaAuth(BaseModel):
    username: str = Field(..., max_length=255)
    hashed_password: str = Field(..., min_length=4, max_length=255)

    class Config:
        from_attributes = True
