from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.models_crud import crud_categories
from db.engine import async_session_maker
from schemas.categories import CategoryRead


categories_router = APIRouter(prefix='/api')


@categories_router.get('/category')
async def get_all_categories(session: AsyncSession = Depends(async_session_maker)):
    result = await crud_categories.get_all(session=session)
    categories = result.fetchall()
    print(result)
    print(categories)
    return CategoryRead
