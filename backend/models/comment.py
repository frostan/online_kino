from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Comments(Base):
    username: Mapped[str] = mapped_column(ForeignKey('user.username'))
    text: Mapped[str] = mapped_column(String)
    date: Mapped[DateTime] = mapped_column(DateTime)
    movie_id: Mapped[int] = ForeignKey('movies.id')

    movie: Mapped['Movies'] = relationship('Movies', back_populates='comments')
    user: Mapped['User'] = relationship('User', back_populates='comments')
