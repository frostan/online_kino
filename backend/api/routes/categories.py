from fastapi import APIRouter


categories_router = APIRouter()


@categories_router.get('')
async def categories_list():
    return {'categories':[]}