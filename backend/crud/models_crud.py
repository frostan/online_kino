from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from crud.base_crud import CRUDBase
from models import Categories, Comments, User, Genres, Movies


class CRUDCategories(CRUDBase):
    async def get_by_title(self, session: AsyncSession, title: str):
        result = await session.execute(
            select(self.model).where(self.model.title == title)
        )
        return result.scalars().first()


class CRUDComments(CRUDBase):
    pass


class CRUDGenres(CRUDBase):
    pass


class CRUDMovies(CRUDBase):
    pass


class CRUDUser(CRUDBase):
    pass


crud_categories = CRUDCategories(Categories)
crud_comments = CRUDComments(Comments)
crud_genres = CRUDGenres(Genres)
crud_movies = CRUDMovies(Movies)
crud_user = CRUDUser(User)
