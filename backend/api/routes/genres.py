from fastapi import APIRouter


genres_router = APIRouter(prefix='/api')


@genres_router.get('/movies')
async def genres_list():
    return {'genres': []}
