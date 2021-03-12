from src.Dto.CategoryDto import CategoryDto
from src.Helper.Helper import Helper
from src.Helper.TechnologyHelper import TechnologyHelper
from src.Models.Category import Category
from src.Service.CategoryService import CategoryService


class CategoryHelper(Helper):
    # Inheritance #
    _type_dto = CategoryDto
    _type_model = Category
    _type_service = CategoryService

    @staticmethod
    def map(category: CategoryDto) -> Category:
        return Category(category.id, category.label, TechnologyHelper().map_all(category.technology))

    # New behaviour #
