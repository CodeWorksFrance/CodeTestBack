from db_config import DBConfig
from src.Dto.CategoryDto import CategoryDto


class CategoryService:
    @staticmethod
    def get_categories() -> [CategoryDto]:
        session = DBConfig().get_session()
        query_result = session.query(CategoryDto)
        session.close()
        return query_result
