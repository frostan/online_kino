from pydantic import BaseModel
from typing import Optional, List


class UserBase(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True


class UserRead(UserBase):
    id: int
    comments: Optional[List['CommentRead']] = []


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


