import typing

import strawberry

from scr.Helper.CategoryHelper import CategoryHelper
from scr.Helper.QuestionHelper import QuestionHelper
from scr.Helper.TechnologyHelper import TechnologyHelper
from scr.Helper.WorkshopHelper import WorkshopHelper
from scr.Models.Category import Category
from scr.Models.Question import Question
from scr.Models.Technology import Technology
from scr.Models.Workshop import Workshop


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
    def category(self, label: str) -> Category:
        return Category.save_category(label)


schema = strawberry.Schema(query=Query, mutation=Mutation)
