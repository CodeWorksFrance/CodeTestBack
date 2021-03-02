from db_config import DBConfig
from src.Dto.EvaluationDto import EvaluationDto


class EvaluationService:
    @staticmethod
    def get_evaluations() -> [EvaluationDto]:
        session = DBConfig().get_session()
        query_result = session.query(EvaluationDto)
        session.close()
        return query_result
