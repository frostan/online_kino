from sqlalchemy import Table, Integer, ForeignKey, Column
from .base import Base

movies_genres = Table(
    'movies_genres',
    Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id'), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genres.id'), primary_key=True),
)
