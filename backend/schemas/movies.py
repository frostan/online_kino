from datetime import datetime

from pydantic import BaseModel
from typing import Optional


class MovieBase(BaseModel):
    title: str
    date: Optional[datetime]
    description: str
    rating: float

    model_config = {
        'from_attributes': True,
    }


class MovieRead(MovieBase):
    id: int

    model_config = {
        'from_attributes': True,
        'arbitrary_types_allowed': True,
    }


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieBase):
    pass
