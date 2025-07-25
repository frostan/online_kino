from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING, Optional, List,TYPE_CHECKING

# if TYPE_CHECKING:
#     from .comments import CommentRead

class UserBase(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        from_attributes = True


class UserRead(UserBase):
    id: int
    comments: Optional[List['CommentRead']] = None
    
    model_config = {
        "arbitrary_types_allowed": True,
    }


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass
