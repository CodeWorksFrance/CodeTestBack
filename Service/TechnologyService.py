from Dto.TechnologyDto import TechnologyDto
from postgres import Postgres


class TechnologyService:
    @staticmethod
    def get_technologies() -> [TechnologyDto]:
        session = Postgres.init_session()
        return session.query(TechnologyDto)
