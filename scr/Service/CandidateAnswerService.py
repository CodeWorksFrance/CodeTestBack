from postgres import Postgres
from scr.Dto.CandidateAnswerDto import CandidateAnswerDto


class CandidateAnswerService:
    @staticmethod
    def get_candidate_answers() -> [CandidateAnswerDto]:
        session = Postgres.init_session()
        return session.query(CandidateAnswerDto)
