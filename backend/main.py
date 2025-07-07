from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.engine import engine
from api.routes import (
    comments_router,
    user_router,
    categories_router,
    movies_router,
    genres_router
)


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Запуск сервера: подключение к базе данных")
    async with engine.connect() as conn:

        yield
    print("Завершение работы: отключение от базы данных")
    await engine.dispose()

app = FastAPI(
    title='Online-kino',
    description='Author - frostan',
    lifespan=lifespan
)


app.include_router(comments_router,prefix='/comments')
app.include_router(user_router,prefix='/users')
app.include_router(categories_router,prefix='/category')
app.include_router(movies_router,prefix='/movies')
app.include_router(genres_router,prefix='/genres')