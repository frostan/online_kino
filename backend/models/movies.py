from sqlalchemy import DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .movies_categories import movies_categories
from .movies_genres import movies_genres


class Movies(Base):
    title: Mapped[str] = mapped_column(String)
    date: Mapped[DateTime] = mapped_column(DateTime)
    description: Mapped[str] = mapped_column(String)
    rating: Mapped[float] = mapped_column(Float)
    video_path: Mapped[str] = mapped_column(String(255), nullable=True)
    comments: Mapped[list['Comments']] = relationship(
        'Comments', back_populates='movie'
    )
    categories: Mapped[list['Categories']] = relationship(
        'Categories', secondary=movies_categories, back_populates='movies'
    )
    genres: Mapped[list['Genres']] = relationship(
        'Genres', secondary=movies_genres, back_populates='movies'
    )

    def __str__(self):
        return self.title
