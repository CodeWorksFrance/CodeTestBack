from postgres import Postgres
from scr.Dto.EvaluationDto import EvaluationDto


class EvaluationService:
    @staticmethod
    def get_evaluations() -> [EvaluationDto]:
        session = Postgres.init_session()
        return session.query(EvaluationDto)
