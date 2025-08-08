from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from crud.engine import get_async_session
from schemas.comments import CommentRead, CommentCreate
from crud.models_crud import crud_comments

comments_router = APIRouter(prefix='/api')


@comments_router.get(
    '/comments',
    response_model=list[CommentRead],
    summary='Получаем список комментариев',
    responses={
        status.HTTP_200_OK: {
            'description': 'Список Коменнтариев',
            'model': CommentRead,
        },
        status.HTTP_404_NOT_FOUND: {'description': 'Комментарии не найдены'},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            'description': 'Внутренняя ошибка сервера'
        },
    },
)
async def comments_list(session: AsyncSession = Depends(get_async_session)):
    comments = await crud_comments.get_multi(session=session)
    return comments


@comments_router.get(
    '/comments/{comment_id}',
    response_model=CommentRead,
    summary='Получаем комментарий по id',
    responses={
        status.HTTP_200_OK: {'description': 'Успешный запрос', 'model': CommentRead},
        status.HTTP_404_NOT_FOUND: {'description': 'Комментарий не найден'},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            'description': 'Внутренняя ошибка сервера'
        },
    },
)
async def comments_retrieve(
    comment_id: int, session: AsyncSession = Depends(get_async_session)
):
    comment = await crud_comments.get(id=comment_id, session=session)
    return comment


@comments_router.post(
    '/comments/',
    response_model=CommentRead,
    summary='Создание комментария',
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            'description': 'Комментарий создан',
            'model': CommentCreate,
        },
        status.HTTP_400_BAD_REQUEST: {'description': 'Некорректные данные'},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            'description': 'Внутренняя ошибка сервера'
        },
    },
)
async def comments_post(
    data: CommentCreate, session: AsyncSession = Depends(get_async_session)
):
    comment = await crud_comments.create(data=data, session=session)
    return comment
