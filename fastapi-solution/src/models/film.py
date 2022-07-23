# -*- coding: utf-8 -*-
from typing import List

from models.base import BaseMixin
from models.person import BasePerson


class BaseFilm(BaseMixin):
    """
    Информация на главной странице п.1 ТЗ
    Фильтрации по жанру пп.1 п.1 ТЗ
    Поиск по фильму п.2 ТЗ
    Фильм по персоне пп.2 п.4 ТЗ
    """

    imdb_rating: float = None
    title: str


class Film(BaseFilm):
    """
    Информайия на странице фильма п.3 ТЗ
    """

    description: str = None
    genre: List[str]
    director: str
    writers: List[BasePerson]
    actors: List[BasePerson]
