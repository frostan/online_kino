from fastapi import FastAPI
from sqladmin import Admin
from contextlib import asynccontextmanager
from db.engine import engine
from fastapi.staticfiles import StaticFiles

from admin_panel.admin import CommentsAdmin, CategoryAdmin, UserAdmin, MoviesAdmin, GenresAdmin
from api.routes import categories_router, user_router, comments_router, movies_router, genres_router


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

app.mount('/media', StaticFiles(directory='media'), name='media')
admin = Admin(
    app,
    engine,
    title='Online-kino',
    logo_url='/media/freepik__retouch__9805.png',
)

admin.add_view(CommentsAdmin)
admin.add_view(CategoryAdmin)
admin.add_view(MoviesAdmin)
admin.add_view(GenresAdmin)
admin.add_view(UserAdmin)

app.include_router(comments_router, prefix='/comments')
app.include_router(user_router, prefix='/users')
app.include_router(categories_router, prefix='/category')
app.include_router(movies_router, prefix='/movies')
app.include_router(genres_router, prefix='/genres')