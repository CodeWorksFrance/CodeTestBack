import typing

from src.Dto.EvaluationDto import EvaluationDto
from src.Helper.CandidateAnswerHelper import CandidateAnswerHelper
from src.Helper.TechnologyHelper import TechnologyHelper
from src.Models.Evaluation import Evaluation
from src.Service.EvaluationService import EvaluationService


class EvaluationHelper:
    def retrieve_evaluation(self) -> typing.List[Evaluation]:
        return self.map_evaluations(EvaluationService.get_evaluations())

    @staticmethod
    def map_evaluations(evaluations: [EvaluationDto]):
        return [Evaluation(e.id, e.state, e.score, CandidateAnswerHelper.map_candidate_answers(e.candidate_answer),
                           TechnologyHelper.map_technology(e.technology)) for e in evaluations]
