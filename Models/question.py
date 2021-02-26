import strawberry

from postgres import Postgres


@strawberry.type
class Question:
    id: str
    label: str
    answer: str
    difficulty: str

    @staticmethod
    def get_questions(technology_id: str = None):
        postgres = Postgres()
        if technology_id is not None:
            query_result = postgres.execute(f"SELECT * FROM question WHERE technology_id = '{technology_id}'")
        else:
            query_result = postgres.execute(f"SELECT * FROM question")

        result = []
        if query_result is not None:
            for row in query_result:
                result.append(Question(row[0], row[1], row[2], row[4]))

        return result
