from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from crud.engine import get_async_session
from schemas.user import UserRead
from crud.models_crud import crud_user

user_router = APIRouter(prefix='/api')


@user_router.get(
    '/users',
    response_model=list[UserRead],
    summary='Список пользователей',
    status_code=status.HTTP_200_OK,
)
async def user_list(session: AsyncSession = Depends(get_async_session)):
    users = await crud_user.get_multi(session=session)
    return users


@user_router.get(
    '/users/{user_id}', response_model=UserRead, summary='Получаем пользователя по id'
)
async def user_retrieve(
    user_id: int, session: AsyncSession = Depends(get_async_session)
):
    user = await crud_user.get(id=user_id, session=session)
    return user
