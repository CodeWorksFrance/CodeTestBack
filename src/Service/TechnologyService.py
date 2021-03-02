from db_config import DBConfig
from src.Dto.TechnologyDto import TechnologyDto


class TechnologyService:
    @staticmethod
    def get_technologies() -> [TechnologyDto]:
        session = DBConfig().get_session()
        query_result = session.query(TechnologyDto)
        session.close()
        return query_result
