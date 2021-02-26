import strawberry
import typing

from Models.question import Question
from postgres import Postgres


@strawberry.type
class Technology:
    id: str
    label: str
    type: str
    question: typing.List['Question']

    @staticmethod
    def get_technologies(index: str = None, category_id: str = None):
        postgres = Postgres()
        if index is not None:
            query_result = postgres.execute(f"SELECT * FROM technology WHERE id = '{index}'")
        elif category_id is not None:
            query_result = postgres.execute(f"SELECT * FROM technology WHERE category_id = '{category_id}'")
        else:
            query_result = postgres.execute(f"SELECT * FROM technology")

        result = []
        if query_result is not None:
            for row in query_result:
                result.append(Technology(row[0], row[1], row[2], Question.get_questions()))

        return result
