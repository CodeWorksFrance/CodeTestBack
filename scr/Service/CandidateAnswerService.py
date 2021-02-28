from scr.Dto.CandidateAnswerDto import CandidateAnswerDto
from postgres import Postgres


class CandidateAnswerService:
    @staticmethod
    def get_candidate_answers() -> [CandidateAnswerDto]:
        session = Postgres.init_session()
        return session.query(CandidateAnswerDto)
