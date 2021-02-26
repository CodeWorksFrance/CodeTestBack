import strawberry
import typing

from Models.category import Category
from Models.technology import Technology


@strawberry.type
class Query:
    @strawberry.field
    def category(self) -> typing.List['Category']:
        return Category.get_categories()

    @strawberry.field
    def technology(self, index: str = None) -> typing.List['Technology']:
        return Technology.get_technologies(index=index)


schema = strawberry.Schema(query=Query)
