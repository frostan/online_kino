from pydantic import BaseModel
from typing import Optional, List


class CommentBase(BaseModel):
    text: str
    date: Optional[str]
    movie_id: int
    username: str

    class Config:
        orm_mode = True


class CommentRead(CommentBase):
    id: int
    movie: Optional['MovieRead']
    user: Optional['UserRead']


class CommentCreate(CommentBase):
    pass


class CommentsUpdate(CommentBase):
    pass