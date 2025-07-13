from fastapi import APIRouter


comments_router = APIRouter()



@comments_router.get('')
async def comments_list():
    return {'comments':[]}