from fastapi import APIRouter


user_router = APIRouter(prefix='/api')


@user_router.get('/users')
async def user_list():
    return {'users': []}


@user_router.get('/users/{id}')
async def user_retrieve(id: int):
    pass
