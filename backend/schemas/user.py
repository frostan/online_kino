from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: str
    password: str

    model_config = {
        'from_attributes': True,
    }


class UserRead(UserBase):
    id: int
    comments: Optional[list['CommentRead']] = None

    model_config = {
        'arbitrary_types_allowed': True,
    }


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass
