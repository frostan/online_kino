from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from crud.models_crud import crud_categories
from crud.engine import get_async_session
from schemas.categories import CategoryRead

categories_router = APIRouter(prefix='/api')


@categories_router.get(
    '/category',
    response_model=list[CategoryRead],
    summary='Получаем список всех категорий',
    responses={
        status.HTTP_200_OK: {'description': 'Список категорий', 'model': CategoryRead},
        status.HTTP_404_NOT_FOUND: {'description': 'Категории не найдены'},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            'description': 'Внутренняя ошибка сервера'
        },
    },
)
async def get_all_categories(session: AsyncSession = Depends(get_async_session)):
    categories = await crud_categories.get_all(session=session)
    return categories
