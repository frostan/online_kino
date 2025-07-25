from pydantic import BaseModel
from typing import List, Optional


class MovieBase(BaseModel):
    title: str
    date: Optional[str]
    description: str
    rating: float

    model_config = {
        "from_attributes": True,
    }

class MovieRead(MovieBase):
    id: int
    comments: Optional[List["CommentRead"]] = None
    categories: Optional[List["CategoryRead"]] = None
    genres: Optional[List["GenreRead"]] = None

    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
    }


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieBase):
    pass
