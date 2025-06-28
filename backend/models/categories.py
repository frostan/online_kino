from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .movies_categories import movies_categories



class Categories(Base):
    title: Mapped[str] = mapped_column(String)
    movies: Mapped[list['Movies']] = relationship(
        'Movies', secondary=movies_categories, back_populates='categories'
    )

    def __str__(self):
        return self.title
