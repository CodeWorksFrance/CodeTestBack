from postgres import Postgres
from scr.Dto.CategoryDto import CategoryDto


class CategoryService:
    @staticmethod
    def get_categories() -> [CategoryDto]:
        session = Postgres.init_session()
        return session.query(CategoryDto)
