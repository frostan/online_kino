from fastapi import APIRouter


genres_router = APIRouter()



@genres_router.get('')
async def genres_list():
    return {'genres':[]}