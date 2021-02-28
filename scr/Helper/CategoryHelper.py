import typing

from scr.Helper.TechnologyHelper import TechnologyHelper
from scr.Models.Category import Category
from scr.Service.CategoryService import CategoryService


class CategoryHelper:
    @staticmethod
    def retrieve_category() -> typing.List[Category]:
        return [Category(c.id, c.label, TechnologyHelper.map_technologies(c.technology))
                for c in CategoryService.get_categories()]
