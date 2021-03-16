import typing

import strawberry

from src.Models.Technology import Technology


@strawberry.type
class Category:
    id: str
    label: str
    technology: typing.List[Technology]
