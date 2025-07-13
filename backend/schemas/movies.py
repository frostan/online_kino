from pydantic import BaseModel
from typing import Optional, List


class MovieBase(BaseModel):
    title: str
    date: Optional[str]
    description: str
    rating: float

    class Config:
        orm_mode = True


class MovieRead(MovieBase):
    id: int
    comments: Optional[List['CommentRead']] = []
    categories: Optional[List['CategoryRead']] = []
    genres: Optional[List['GenreRead']] = []


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieBase):
    pass