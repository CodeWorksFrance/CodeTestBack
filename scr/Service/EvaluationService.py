from db_config import DBConfig
from scr.Dto.EvaluationDto import EvaluationDto


class EvaluationService:
    @staticmethod
    def get_evaluations() -> [EvaluationDto]:
        session = DBConfig().init_session()
        return session.query(EvaluationDto)
