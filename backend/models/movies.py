from pyrogram.raw.core import String
from sqlalchemy import DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .comment import Comments
from .genres import Genres
from .categories import Categories


class Movies(Base):
    title: Mapped[str] = mapped_column(String)
    date: Mapped[DateTime] = mapped_column(DateTime)
    description: Mapped[str] = mapped_column(String)
    rating: Mapped[float] = mapped_column(Float)
    comments: Mapped[list[Comments]] = relationship(
        'Comments', back_populates='movie'
    )
    categories: Mapped[list[Categories]] = relationship(
        'Category', secondary='movies_category', back_populates='movies'
    )
    genres: Mapped[list[Genres]] = relationship(
        'Genres', secondary='movie_genres', back_populates='movies'
    )
