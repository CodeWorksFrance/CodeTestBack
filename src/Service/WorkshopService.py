from db_config import DBConfig
from src.Dto.WorkshopDto import WorkshopDto


class WorkshopService:
    @staticmethod
    def get_workshops(index: str) -> [WorkshopDto]:
        session = DBConfig().get_session()
        if index is None:
            query_result = session.query(WorkshopDto)
            session.close()
            return query_result

        query_result = session.query(WorkshopDto).filter_by(id=index)
        session.close()
        return query_result
