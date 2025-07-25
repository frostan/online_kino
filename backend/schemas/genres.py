from pydantic import BaseModel
from typing import Optional, List


class GenreBase(BaseModel):
    title: str

    model_config = {
        "arbitrary_types_allowed": True,
    }


class GenreRead(GenreBase):
    id: int
    movies: Optional[List['MovieRead']] = None

    model_config = {
        "arbitrary_types_allowed": True,
    }


class GenreUpdate(GenreBase):
    pass


class GenreCreate(GenreBase):
    pass
