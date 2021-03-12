import atexit
import typing

import strawberry

from db_config import DBConfig
from src.Helper.CategoryHelper import CategoryHelper
from src.Helper.QuestionHelper import QuestionHelper
from src.Helper.TechnologyHelper import TechnologyHelper
from src.Helper.WorkshopHelper import WorkshopHelper
from src.Models.CandidateAnswer import CandidateAnswer
from src.Models.Category import Category
from src.Models.Question import Question
from src.Models.Technology import Technology
from src.Models.Workshop import Workshop


@strawberry.type
class Query:
    @strawberry.field
    def category(self) -> typing.List['Category']:
        return CategoryHelper().retrieve()

    @strawberry.field
    def technology(self) -> typing.List['Technology']:
        return TechnologyHelper().retrieve()

    @strawberry.field
    def question(self, index: str = None) -> typing.List['Question']:
        return QuestionHelper().retrieve(index=index)

    @strawberry.field
    def workshop(self, index: str = None) -> typing.List['Workshop']:
        return WorkshopHelper().retrieve(index=index)

    @strawberry.field
    def next_question(self, workshop_id: str) -> typing.List['CandidateAnswer']:
        return WorkshopHelper().retrieve_next_question(workshop_id)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def workshop(self, technologies: typing.List[str]) -> Workshop:
        return WorkshopHelper().create_workshop(technologies)


schema = strawberry.Schema(query=Query, mutation=Mutation)


@atexit.register
def goodbye():
    DBConfig.close_all_sessions()
