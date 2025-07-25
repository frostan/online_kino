from sqladmin import ModelView

from models import Movies, Comments, Categories, Genres, User


class CategoryAdmin(ModelView,model=Categories):

    name = 'Категория'
    name_plural = 'Категории'

    column_list = '__all__'
    column_labels = {}

class MoviesAdmin(ModelView, model=Movies):

    name = 'Фильм'
    name_plural = 'Фильмы'

    column_list = '__all__'
    column_labels = {}

class GenresAdmin(ModelView,model=Genres):

    name = 'Жанр'
    name_plural = 'Жанры'

    column_list = '__all__'
    column_labels = {}


class CommentsAdmin(ModelView,model=Comments):

    name = 'Комментарий'
    name_plural = 'Комментарии'

    column_list = '__all__'
    column_labels = {}

class UserAdmin(ModelView, model=User):

    name = 'Пользователь'
    name_plural = 'Пользователи'

    column_list = '__all__'
    column_labels = {}