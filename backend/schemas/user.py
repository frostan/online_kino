from pydantic import BaseModel
from typing import Optional, List


class UserBase(BaseModel):
    username: str
    email: str
    password: str

    model_config = {
        "from_attributes": True,
    }


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
