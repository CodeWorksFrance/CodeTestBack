import typing

from src.Dto import CandidateAnswerDto
from src.Models.CandidateAnswer import CandidateAnswer
from src.Service.CandidateAnswerService import CandidateAnswerService


class CandidateAnswerHelper:
    def retrieve_candidate_answers(self) -> typing.List[CandidateAnswer]:
        return self.map_candidate_answers(CandidateAnswerService().get())

    @staticmethod
    def map_candidate_answers(candidate_answers: [CandidateAnswerDto]):
        return [CandidateAnswer(c.id, c.state, c.score, c.question) for c in candidate_answers]
