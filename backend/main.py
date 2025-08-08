from fastapi import FastAPI
from fastapi.requests import Request
from sqladmin import Admin
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles

from config import settings
from crud.engine import engine

from admin_panel.admin import (
    CommentsAdmin,
    CategoryAdmin,
    UserAdmin,
    MoviesAdmin,
    GenresAdmin,
    AdminAuth,
)
from api.routes import (
    categories_router,
    user_router,
    comments_router,
    movies_router,
    genres_router,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Запуск сервера: подключение к базе данных')
    async with engine.connect() as _:
        yield
    print('Завершение работы: отключение от базы данных')
    await engine.dispose()


app = FastAPI(
    title='Online-kino',
    description='Автор - frostan',
    lifespan=lifespan,
    docs_url='/api/docs',
    redoc_url='/api/redoc',
)


@app.middleware('http')
async def force_utf8_charset(request: Request, call_next):
    response = await call_next(request)
    if 'application/json' in response.headers.get('content-type', ''):
        response.headers['content-type'] = 'application/json; charset=utf-8'
    return response


app.mount('/media', StaticFiles(directory=settings.MEDIA_DIR), name='media')
admin = Admin(
    app,
    engine,
    authentication_backend=AdminAuth(secret_key=settings.SECRET_KEY),
    title='Online-kino',
    logo_url='/media/freepik__retouch__9805.png',
)

admin.add_view(CommentsAdmin)
admin.add_view(CategoryAdmin)
admin.add_view(MoviesAdmin)
admin.add_view(GenresAdmin)
admin.add_view(UserAdmin)

app.include_router(comments_router)
app.include_router(user_router)
app.include_router(categories_router)
app.include_router(movies_router)
app.include_router(genres_router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='127.0.0.1', port=8000)
