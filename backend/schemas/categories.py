from pydantic import BaseModel
from typing import Optional


class CategoryBase(BaseModel):
    title: str

    model_config = {
        'arbitrary_types_allowed': True,
    }


class CategoryRead(CategoryBase):
    id: int
    movies: Optional[list['MovieRead']] = None

    model_config = {
        'from_attributes': True,
        'arbitrary_types_allowed': True,
    }


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass
