from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.engine import get_async_session
from schemas.comments import CommentRead
from db.models_crud import crud_comments

comments_router = APIRouter(prefix='/api')


@comments_router.get('/comments', response_model=list[CommentRead])
async def comments_list(session: AsyncSession = Depends(get_async_session)):
    comments = await crud_comments.get_multi(session=session)
    return comments


@comments_router.get('/comments/{id}')
async def comments_retrive(id: int):
    pass


@comments_router.post('/comments/{id}')
async def comments_post(id: int):
    pass
