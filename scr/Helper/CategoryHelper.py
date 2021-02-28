import typing

from scr.Dto.CategoryDto import CategoryDto
from scr.Helper.TechnologyHelper import TechnologyHelper
from scr.Models.Category import Category
from scr.Service.CategoryService import CategoryService


class CategoryHelper:
    def retrieve_category(self) -> typing.List[Category]:
        return self.map_categories(CategoryService.get_categories())

    @staticmethod
    def map_categories(categories: [CategoryDto]):
        return [Category(c.id, c.label, TechnologyHelper.map_technologies(c.technology)) for c in categories]
