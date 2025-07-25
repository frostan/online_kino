from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING, Optional, List

# if TYPE_CHECKING:
#     from .movies import MovieRead

class GenreBase(BaseModel):
    title: str

    class Config:
        from_attributes = True


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
