from pydantic import BaseModel
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .movies import MovieRead


class CategoryBase(BaseModel):
    title: str

    class Config:
        from_attributes = True

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
