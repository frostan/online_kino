import bcrypt
from sqladmin import ModelView
from fastapi.requests import Request
from sqladmin.authentication import AuthenticationBackend
from itsdangerous.serializer import Serializer
from itsdangerous.exc import BadSignature

from models import Movies, Comments, Categories, Genres, User
from db.engine import async_session_maker
from db.models_crud import crud_user


class AdminAuth(AuthenticationBackend):
    def __init__(self, secret_key: str):
        super().__init__(secret_key)
        self.serializer = Serializer(secret_key)

    async def login(self, request: Request) -> bool:
        """Вход администратора."""
        form = await request.form()
        username, user_password = form['username'], form['password']
        if not username or not user_password:
            return False
        async with async_session_maker() as session:
            admin: User = await crud_user.get_by_attr(
                attr_name='username',
                attr_value=username,
                session=session,
            )
        if admin is None:
            return False

        if admin.password == 'admin':
            password = True
        else:
            password = bcrypt.checkpw(
                user_password.encode('utf-8'), admin.password.encode('utf-8')
            )

        if password:
            data = username
            token = self.serializer.dumps(data)
            request.session.update({'token': token})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        """Выход Администратора."""
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        """Аутентификация админа."""
        token = request.session.get('token')
        if not token:
            return False
        try:
            self.serializer.loads(token)
            return True
        except BadSignature:
            return False


class CategoryAdmin(ModelView, model=Categories):
    name = 'Категория'
    name_plural = 'Категории'

    column_list = (
        'id',
        'title',
        'movies',
    )
    column_labels = {'title': 'Название', 'movies': 'Фильм'}


class MoviesAdmin(ModelView, model=Movies):
    name = 'Фильм'
    name_plural = 'Фильмы'

    column_list = (
        'id',
        'title',
        'date',
        'description',
    )
    column_labels = {
        'title': 'Название',
        'date': 'Дата',
        'description': 'Описание',
        'rating': 'Рейтинг',
        'comments': 'Комментарии',
        'categories': 'Категория',
        'genres': 'Жанр',
    }


class GenresAdmin(ModelView, model=Genres):
    name = 'Жанр'
    name_plural = 'Жанры'

    column_list = ('id', 'title', 'movies')
    column_labels = {
        'title': 'Название',
        'movies': 'Фильмы',
    }


class CommentsAdmin(ModelView, model=Comments):
    name = 'Комментарий'
    name_plural = 'Комментарии'

    column_list = (
        'id',
        'username',
        'text',
        'date',
    )
    column_labels = {
        'username': 'Имя',
        'text': 'Текст',
        'date': 'Дата',
        'movie_id': 'Фильм',
    }


class UserAdmin(ModelView, model=User):
    name = 'Пользователь'
    name_plural = 'Пользователи'

    column_list = (
        'id',
        'username',
        'email',
    )
    column_labels = {
        'username': 'Имя',
        'email': 'Электронная почта',
        'comments': 'Комментарии',
    }
