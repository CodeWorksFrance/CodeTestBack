import typing

from src.Dto.CandidateAnswerDto import CandidateAnswerDto
from src.Dto.EvaluationDto import EvaluationDto
from src.Dto.QuestionDto import QuestionDto
from src.Helper.CandidateAnswerHelper import CandidateAnswerHelper
from src.Helper.TechnologyHelper import TechnologyHelper
from src.Models.CandidateAnswer import CandidateAnswer
from src.Models.Evaluation import Evaluation
from src.Service.CandidateAnswerService import CandidateAnswerService
from src.Service.EvaluationService import EvaluationService
from src.Service.QuestionService import QuestionService


class EvaluationHelper:
    def retrieve_evaluation(self) -> typing.List[Evaluation]:
        return self.map_evaluations(EvaluationService().get())

    @staticmethod
    def retrieve_next_question(evaluation_id: str, technology_id: str) -> [CandidateAnswer]:
        current_candidate_answer: CandidateAnswerDto = CandidateAnswerService().get_current_evaluation_candidate_answer(
            evaluation_id)
        if current_candidate_answer is not None:
            return CandidateAnswerHelper.map_candidate_answers([current_candidate_answer])

        new_question: QuestionDto = QuestionService().get_question_technology(
            technology_id=technology_id,
            excluded_ids=list(
                map(lambda e: str(e.question_id),
                    CandidateAnswerService().get_closed_evaluation_candidate_answer(evaluation_id)))
        )

        new_candidate_answer: CandidateAnswerDto = CandidateAnswerService().set_current_evaluation_candidate_answer(
            evaluation_id=evaluation_id, question_id=new_question.id)

        return [] if new_candidate_answer is None else CandidateAnswerHelper.map_candidate_answers(
            [new_candidate_answer])

    @staticmethod
    def map_evaluations(evaluations: [EvaluationDto]):
        return [Evaluation(e.id, e.state, e.score, CandidateAnswerHelper.map_candidate_answers(e.candidate_answer),
                           TechnologyHelper.map_technology(e.technology)) for e in evaluations]
