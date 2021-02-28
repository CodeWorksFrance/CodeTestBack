from postgres import Postgres
from scr.Dto.WorkshopDto import WorkshopDto


class WorkshopService:
    @staticmethod
    def get_workshops(index: str) -> [WorkshopDto]:
        session = Postgres.init_session()
        if index is None:
            return session.query(WorkshopDto)

        return session.query(WorkshopDto).filter_by(id=index)
