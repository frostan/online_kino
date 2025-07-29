from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.movies import MovieRead
from db.engine import get_async_session
from db.models_crud import crud_movies

movies_router = APIRouter(prefix='/api')


@movies_router.get('/movies', response_model=list[MovieRead])
async def movies_list(session: AsyncSession = Depends(get_async_session)):
    movies = await crud_movies.get_multi(session=session)
    return movies


@movies_router.get('/movies/{id}')
async def movies_retrieve(id: int):
    pass
