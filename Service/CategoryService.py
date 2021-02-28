from Dto.CategoryDto import CategoryDto
from postgres import Postgres


class CategoryService:
    @staticmethod
    def get_categories() -> [CategoryDto]:
        session = Postgres.init_session()
        return session.query(CategoryDto)
