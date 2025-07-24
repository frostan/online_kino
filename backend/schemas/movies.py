from pydantic import BaseModel
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .comments import CommentRead
    from .categories import CategoryRead
    from .genres import GenreRead

class MovieBase(BaseModel):
    title: str
    date: Optional[str]
    description: str
    rating: float

    class Config:
        from_attributes = True

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

MovieRead.model_rebuild()