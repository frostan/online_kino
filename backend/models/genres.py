from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .movies_genres import movies_genres


class Genres(Base):
    title: Mapped[str] = mapped_column(String)
    movies: Mapped[list['Movies']] = relationship(
        'Movies', secondary=movies_genres, back_populates='genres'
    )
