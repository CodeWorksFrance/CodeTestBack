import typing

import strawberry

from src.Helper.CategoryHelper import CategoryHelper
from src.Helper.QuestionHelper import QuestionHelper
from src.Helper.TechnologyHelper import TechnologyHelper
from src.Helper.WorkshopHelper import WorkshopHelper
from src.Models.Category import Category
from src.Models.Question import Question
from src.Models.Technology import Technology
from src.Models.Workshop import Workshop


@strawberry.type
class Query:
    @strawberry.field
    def category(self) -> typing.List['Category']:
        return CategoryHelper().retrieve_category()

    @strawberry.field
    def technology(self) -> typing.List['Technology']:
        return TechnologyHelper().retrieve_technology()

    @strawberry.field
    def question(self, index: str = None) -> typing.List['Question']:
        return QuestionHelper().retrieve_question(index=index)

    @strawberry.field
    def workshop(self, index: str = None) -> typing.List['Workshop']:
        return WorkshopHelper().retrieve_workshop(index=index)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def workshop(self, technologies: typing.List[str]) -> Workshop:
        return WorkshopHelper().create_workshop(technologies)


schema = strawberry.Schema(query=Query, mutation=Mutation)
