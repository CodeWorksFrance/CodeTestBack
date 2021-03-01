from db_config import DBConfig
from src.Dto.TechnologyDto import TechnologyDto


class TechnologyService:
    @staticmethod
    def get_technologies() -> [TechnologyDto]:
        session = DBConfig().init_session()
        return session.query(TechnologyDto)
