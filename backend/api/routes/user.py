from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.engine import get_async_session
from schemas.user import UserRead
from db.models_crud import crud_user

user_router = APIRouter(prefix='/api')


@user_router.get('/users', response_model=list[UserRead])
async def user_list(session: AsyncSession = Depends(get_async_session)):
    users = await crud_user.get_multi(session=session)
    return users


@user_router.get('/users/{id}')
async def user_retrieve(id: int):
    pass
