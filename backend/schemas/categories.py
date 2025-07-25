from __future__ import annotations
from pydantic import BaseModel
from typing import List, Optional, TYPE_CHECKING

# if TYPE_CHECKING:
#     from .movies import MovieRead


class CategoryBase(BaseModel):
    title: str

    model_config = {
        'from_attributes': True
    }  # лучше такой синтаксис использовать, чем class Config

class CategoryRead(CategoryBase):
    id: int
    movies: Optional[List['MovieRead']] = None

    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
    }


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass
