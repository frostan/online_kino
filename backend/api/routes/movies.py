from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.movies import MovieRead
from crud.engine import get_async_session
from crud.models_crud import crud_movies

movies_router = APIRouter(prefix='/api')


@movies_router.get(
    '/movies',
    response_model=list[MovieRead],
    summary='Получаем список фильмов',
    status_code=status.HTTP_200_OK,
)
async def movies_list(session: AsyncSession = Depends(get_async_session)):
    movies = await crud_movies.get_multi(session=session)
    return movies


@movies_router.get(
    '/movies/{movie_id}',
    response_model=MovieRead,
    summary='Получаем фильм по id',
    status_code=status.HTTP_200_OK,
)
async def movies_retrieve(
    movie_id: int, session: AsyncSession = Depends(get_async_session)
):
    movie = await crud_movies.get(id=movie_id, session=session)
    return movie
