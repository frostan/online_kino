from pydantic import BaseModel
from typing import Optional


class CommentBase(BaseModel):
    text: str
    date: Optional[str]
    movie_id: int
    username: str

    model_config = {
        "arbitrary_types_allowed": True,
    }


class CommentRead(CommentBase):
    id: int
    movie: Optional['MovieRead'] = None
    user: Optional['UserRead'] = None

    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
    }


class CommentCreate(CommentBase):
    pass


class CommentsUpdate(CommentBase):
    pass
