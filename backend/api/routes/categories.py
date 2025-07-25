from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.models_crud import crud_categories
from db.engine import async_session_maker
from schemas.categories import CategoryRead
from typing import List

categories_router = APIRouter()


@categories_router.get('', response_model=List[CategoryRead])
async def get_all_categories(session: AsyncSession = Depends(async_session_maker)):
    result = await crud_categories.get_all(session=session)
    categories = result.fetchall()
    if not categories:
        return []
    return [CategoryRead(**dict(row)) for row in categories]