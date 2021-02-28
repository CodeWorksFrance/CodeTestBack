from postgres import Postgres
from scr.Dto.TechnologyDto import TechnologyDto


class TechnologyService:
    @staticmethod
    def get_technologies() -> [TechnologyDto]:
        session = Postgres.init_session()
        return session.query(TechnologyDto)
