from db_config import DBConfig
from scr.Dto.CategoryDto import CategoryDto


class CategoryService:
    @staticmethod
    def get_categories() -> [CategoryDto]:
        session = DBConfig().init_session()
        return session.query(CategoryDto)
