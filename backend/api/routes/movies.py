from fastapi import APIRouter


movies_router = APIRouter()


@movies_router.get('')
async def movies_list():
    return {'movies': ['1', '1', '2', '3']}
