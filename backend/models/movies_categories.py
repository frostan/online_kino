from sqlalchemy import Table, Integer, ForeignKey, Column
from .base import Base


movies_categories = Table(
    'movies_categories',
    Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id'), primary_key=True),
    Column('category_id', Integer, ForeignKey('categories.id'), primary_key=True),
)
