import typing

from scr.Dto import CandidateAnswerDto
from scr.Models.CandidateAnswer import CandidateAnswer
from scr.Service.CandidateAnswerService import CandidateAnswerService


class CandidateAnswerHelper:
    def retrieve_candidate_answers(self) -> typing.List[CandidateAnswer]:
        return self.map_candidate_answers(CandidateAnswerService.get_candidate_answers())

    @staticmethod
    def map_candidate_answers(candidate_answers: [CandidateAnswerDto]):
        return [CandidateAnswer(c.id, c.state, c.score) for c in candidate_answers]
