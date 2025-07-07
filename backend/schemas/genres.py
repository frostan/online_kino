from pydantic import BaseModel
from typing import Optional, List


class GenreBase(BaseModel):
    title: str

    class Config:
        orm_mode = True


class GenreRead(GenreBase):
    id: int
    movies: Optional[List['MovieRead']] = []


class GenreUpdate(GenreBase):
    pass


class GenreCreate(GenreBase):
    pass