import typing

from src.Dto.CategoryDto import CategoryDto
from src.Helper.TechnologyHelper import TechnologyHelper
from src.Models.Category import Category
from src.Service.CategoryService import CategoryService


class CategoryHelper:
    def retrieve_category(self) -> typing.List[Category]:
        return self.map_categories(CategoryService().get())

    @staticmethod
    def map_categories(categories: [CategoryDto]):
        return [Category(c.id, c.label, TechnologyHelper.map_technologies(c.technology)) for c in categories]
