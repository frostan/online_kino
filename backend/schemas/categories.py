from pydantic import BaseModel
from typing import List, Optional


class CategoryBase(BaseModel):
    title: str

    class Config:
        orm_mode = True


class CategoryRead(CategoryBase):
    id: int
    movies: Optional[List['MovieRead']] = []

    class Config:
        orm_mode = True


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass