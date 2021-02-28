import typing

from scr.Dto.EvaluationDto import EvaluationDto
from scr.Helper.CandidateAnswerHelper import CandidateAnswerHelper
from scr.Models.Evaluation import Evaluation
from scr.Service.EvaluationService import EvaluationService


class EvaluationHelper:
    def retrieve_evaluation(self) -> typing.List[Evaluation]:
        return self.map_evaluations(EvaluationService.get_evaluations())

    @staticmethod
    def map_evaluations(evaluations: [EvaluationDto]):
        return [Evaluation(e.id, e.state, e.score, CandidateAnswerHelper.map_candidate_answers(e.candidate_answer))
                for e in evaluations]
