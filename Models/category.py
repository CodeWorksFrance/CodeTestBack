import strawberry
import typing

from Models.technology import Technology
from postgres import Postgres


@strawberry.type
class Category:
    id: str
    label: str
    technology: typing.List['Technology']

    @staticmethod
    def get_categories():
        postgres = Postgres()
        query_result = postgres.execute("SELECT * FROM category")

        result = []
        if query_result is not None:
            for row in query_result:
                result.append(Category(row[0], row[1], Technology.get_technologies(category_id=row[0])))

        return result
