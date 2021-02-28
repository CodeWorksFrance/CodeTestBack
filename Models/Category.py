import strawberry
import typing

from Models.Technology import Technology


@strawberry.type
class Category:
    id: str
    label: str
    technology: typing.List['Technology']
