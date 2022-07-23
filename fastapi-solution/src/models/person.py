# -*- coding: utf-8 -*-
from typing import List
from uuid import UUID

from models.base import BaseMixin


class BasePerson(BaseMixin):
    """
    Данные о персоне на странице фильма  пп.1 п.3 ТЗ
    """

    name: str


class Person(BasePerson):
    """
    Страница персонажа п.4 ТЗ
    Поиск по персонам пп.2 п.2 ТЗ
    """

    role: str
    film_id: List[UUID]
