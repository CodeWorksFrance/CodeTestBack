import strawberry
import typing

from Helper.CategoryHelper import CategoryHelper
from Helper.QuestionHelper import QuestionHelper
from Helper.TechnologyHelper import TechnologyHelper
from Helper.WorkshopHelper import WorkshopHelper
from Models.Category import Category
from Models.Technology import Technology
from Models.Question import Question
from Models.Workshop import Workshop


@strawberry.type
class Query:
    @strawberry.field
    def category(self) -> typing.List['Category']:
        return CategoryHelper.retrieve_category()

    @strawberry.field
    def technology(self) -> typing.List['Technology']:
        return TechnologyHelper().retrieve_technology()

    @strawberry.field
    def question(self, index: str = None) -> typing.List['Question']:
        return QuestionHelper().retrieve_question(index=index)

    @strawberry.field
    def workshop(self, index: str = None) -> typing.List['Workshop']:
        return WorkshopHelper.retrieve_workshop(index=index)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def category(self, label: str) -> Category:
        return Category.save_category(label)


schema = strawberry.Schema(query=Query, mutation=Mutation)
