from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from crud.engine import get_async_session
from schemas.genres import GenreRead
from crud.models_crud import crud_genres

genres_router = APIRouter(prefix='/api')


@genres_router.get(
    '/genres',
    response_model=list[GenreRead],
    summary='Получаем список жанров',
    status_code=status.HTTP_200_OK,
)
async def genres_list(session: AsyncSession = Depends(get_async_session)):
    genres = await crud_genres.get_all(session=session)
    return genres
