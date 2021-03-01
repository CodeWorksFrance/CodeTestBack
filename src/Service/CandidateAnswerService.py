from db_config import DBConfig
from src.Dto.CandidateAnswerDto import CandidateAnswerDto


class CandidateAnswerService:
    @staticmethod
    def get_candidate_answers() -> [CandidateAnswerDto]:
        session = DBConfig().init_session()
        return session.query(CandidateAnswerDto)
