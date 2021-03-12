from src.Dto import CandidateAnswerDto
from src.Helper.Helper import Helper
from src.Models.CandidateAnswer import CandidateAnswer
from src.Service.CandidateAnswerService import CandidateAnswerService


class CandidateAnswerHelper(Helper):
    # Inheritance #
    _type_dto = CandidateAnswerDto
    _type_model = CandidateAnswer
    _type_service = CandidateAnswerService

    @staticmethod
    def map(candidate_answer: CandidateAnswerDto) -> CandidateAnswer:
        return CandidateAnswer(candidate_answer.id, candidate_answer.state, candidate_answer.score,
                               candidate_answer.question)

    # New behaviour #
