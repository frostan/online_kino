from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.models_crud import crud_categories
from db.engine import get_async_session
from schemas.categories import CategoryRead, CategoryCreate

categories_router = APIRouter(prefix='/api')


@categories_router.get('/category', response_model=list[CategoryRead])
async def get_all_categories(session: AsyncSession = Depends(get_async_session)):
    categories = await crud_categories.get_all(session=session)
    return categories


@categories_router.post('/category', response_model=CategoryRead)
async def create_category(
    category_data: CategoryCreate, session: AsyncSession = Depends(get_async_session)
):
    existing_category = await crud_categories.get_by_title(
        session, title=category_data.title
    )
    if existing_category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Категория с таким названием уже существует',
        )
    new_category = await crud_categories.create(
        session, obj_in=category_data.model_dump()
    )
    await session.refresh(new_category)
    return new_category
