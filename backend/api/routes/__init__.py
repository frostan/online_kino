from .comments import comments_router
from .categories import categories_router
from .genres import genres_router
from .user import user_router
from .movies import movies_router


__all__ = (
    'genres_router',
    'user_router',
    'categories_router',
    'movies_router',
    'comments_router',
)
