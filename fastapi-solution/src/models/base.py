# -*- coding: utf-8 -*-
from uuid import UUID

import orjson
from pydantic import BaseModel

# Используем pydantic для упрощения работы при перегонке данных из json в объекты


def orjson_dumps(v, *, default):
    # orjson.dumps возвращает bytes, а pydantic требует unicode, поэтому декодируем
    return orjson.dumps(v, default=default).decode()


class BaseMixin(BaseModel):
    """
    Базовый миксин
    """

    id: UUID

    class Config:
        # Заменяем стандартную работу с json на более быструю
        json_loads = orjson.loads
        json_dumps = orjson_dumps
