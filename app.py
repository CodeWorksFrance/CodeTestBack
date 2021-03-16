import atexit
import typing

import strawberry

from db_config import DBConfig
from src.Helper.CategoryHelper import CategoryHelper
from src.Helper.EvaluationQuestionHelper import EvaluationQuestionHelper
from src.Helper.QuestionHelper import QuestionHelper
from src.Helper.TechnologyHelper import TechnologyHelper
from src.Helper.WorkshopHelper import WorkshopHelper
from src.Models.EvaluationQuestion import EvaluationQuestion
from src.Models.Category import Category
from src.Models.Question import Question
from src.Models.Technology import Technology
from src.Models.Workshop import Workshop


@strawberry.type
class Query:
    # Category #
    @strawberry.field
    def categories(self) -> typing.List[Category]:
        return CategoryHelper().retrieve()

    @strawberry.field
    def category(self, index: str) -> typing.Optional[Category]:
        return CategoryHelper().retrieve_by_index(index)

    # Technology #
    @strawberry.field
    def technologies(self) -> typing.List[Technology]:
        return TechnologyHelper().retrieve()

    @strawberry.field
    def technology(self, index: str) -> typing.Optional[Technology]:
        return TechnologyHelper().retrieve_by_index(index)

    # Question #
    @strawberry.field
    def questions(self) -> typing.List[Question]:
        return QuestionHelper().retrieve()

    @strawberry.field
    def question(self, index: str) -> typing.Optional[Question]:
        return QuestionHelper().retrieve_by_index(index)

    # Workshop #
    @strawberry.field
    def workshops(self) -> typing.List[Workshop]:
        return WorkshopHelper().retrieve()

    @strawberry.field
    def workshop(self, index: str) -> typing.Optional[Workshop]:
        return WorkshopHelper().retrieve_by_index(index)

    # Next Question #
    @strawberry.field
    def next_question(self, workshop_id: str) -> typing.Optional[EvaluationQuestion]:
        return WorkshopHelper().retrieve_next_question(workshop_id)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def workshop(self, technologies: typing.List[str]) -> Workshop:
        return WorkshopHelper().create_workshop(technologies)

    @strawberry.mutation
    def save_answer(self, evaluation_question_id: str, state: str) -> EvaluationQuestion:
        EvaluationQuestionHelper().save_answer(evaluation_question_id, state)
        return EvaluationQuestionHelper().retrieve_by_index(evaluation_question_id)


schema = strawberry.Schema(query=Query, mutation=Mutation)


@atexit.register
def goodbye():
    DBConfig.close_all_sessions()
