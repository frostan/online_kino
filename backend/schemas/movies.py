from pydantic import BaseModel
from typing import Optional


class MovieBase(BaseModel):
    title: str
    date: Optional[str]
    description: str
    rating: float

    model_config = {
        'from_attributes': True,
    }


class MovieRead(MovieBase):
    id: int
    comments: Optional[list['CommentRead']] = None
    categories: Optional[list['CategoryRead']] = None
    genres: Optional[list['GenreRead']] = None

    model_config = {
        'from_attributes': True,
        'arbitrary_types_allowed': True,
    }


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieBase):
    pass
