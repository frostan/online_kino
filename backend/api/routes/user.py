from fastapi import APIRouter


user_router = APIRouter()


@user_router.get('')
async def user_list():
    return {'users': []}
