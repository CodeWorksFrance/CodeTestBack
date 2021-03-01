from db_config import DBConfig
from src.Dto.WorkshopDto import WorkshopDto


class WorkshopService:
    @staticmethod
    def get_workshops(index: str) -> [WorkshopDto]:
        session = DBConfig().init_session()
        if index is None:
            return session.query(WorkshopDto)

        return session.query(WorkshopDto).filter_by(id=index)
