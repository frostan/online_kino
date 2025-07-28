from fastapi import APIRouter


comments_router = APIRouter(prefix='/api')


@comments_router.get('/comments')
async def comments_list():
    return {'comments': []}


@comments_router.get('/comments/{id}')
async def comments_retrive(id: int):
    pass


@comments_router.post('/comments/{id}')
async def comments_post(id: int):
    pass
