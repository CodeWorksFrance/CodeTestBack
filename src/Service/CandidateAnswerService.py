from db_config import DBConfig
from src.Dto.CandidateAnswerDto import CandidateAnswerDto


class CandidateAnswerService:
    @staticmethod
    def get_candidate_answers() -> [CandidateAnswerDto]:
        session = DBConfig().get_session()
        query_result = session.query(CandidateAnswerDto)
        session.close()
        return query_result
