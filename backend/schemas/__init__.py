from .categories import CategoryRead
from .movies import MovieRead
from .genres import GenreRead
from .comments import CommentRead
from .user import UserRead

CategoryRead.model_rebuild()
MovieRead.model_rebuild()
GenreRead.model_rebuild()
CommentRead.model_rebuild()
UserRead.model_rebuild()
