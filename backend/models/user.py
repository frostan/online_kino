from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class User(Base):
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String, unique=True)

    comments: Mapped[list['Comments']] = relationship('Comments', back_populates='user')

    def __str__(self):
        return self.username