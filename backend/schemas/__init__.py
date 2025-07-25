from .categories import CategoryRead
from .movies import MovieRead
from .comments import CommentRead
from .genres import GenreRead
from .user import UserRead

CategoryRead.model_rebuild()
MovieRead.model_rebuild()
CommentRead.model_rebuild()
GenreRead.model_rebuild()
UserRead.model_rebuild()
