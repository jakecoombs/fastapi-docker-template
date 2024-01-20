from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
