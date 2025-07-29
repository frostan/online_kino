from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.engine import get_async_session
from schemas.genres import GenreRead
from db.models_crud import crud_genres

genres_router = APIRouter(prefix='/api')


@genres_router.get('/genres', response_model=list[GenreRead])
async def genres_list(session: AsyncSession = Depends(get_async_session)):
    genres = await crud_genres.get_all(session=session)
    return genres
