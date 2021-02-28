import strawberry
import typing

from scr.Models.Technology import Technology


@strawberry.type
class Category:
    id: str
    label: str
    technology: typing.List['Technology']
