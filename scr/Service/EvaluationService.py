from scr.Dto.EvaluationDto import EvaluationDto
from postgres import Postgres


class EvaluationService:
    @staticmethod
    def get_evaluations() -> [EvaluationDto]:
        session = Postgres.init_session()
        return session.query(EvaluationDto)
