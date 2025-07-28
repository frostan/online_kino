from fastapi import APIRouter


movies_router = APIRouter(prefix='/api')


@movies_router.get('/movies')
async def movies_list():
    return {'movies': ['1', '1', '2', '3']}


@movies_router.get('/movies/{id}')
async def movies_retrieve(id: int):
    pass
