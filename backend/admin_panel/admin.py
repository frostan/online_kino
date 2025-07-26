from sqladmin import ModelView

from models import Movies, Comments, Categories, Genres, User


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
