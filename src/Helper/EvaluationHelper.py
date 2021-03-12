from typing import Optional

from src.Dto.CandidateAnswerDto import CandidateAnswerDto
from src.Dto.EvaluationDto import EvaluationDto
from src.Dto.QuestionDto import QuestionDto
from src.Helper.CandidateAnswerHelper import CandidateAnswerHelper
from src.Helper.Helper import Helper
from src.Helper.TechnologyHelper import TechnologyHelper
from src.Models.CandidateAnswer import CandidateAnswer
from src.Models.Evaluation import Evaluation
from src.Service.CandidateAnswerService import CandidateAnswerService
from src.Service.EvaluationService import EvaluationService
from src.Service.QuestionService import QuestionService


class EvaluationHelper(Helper):
    # Inheritance #
    _type_dto = EvaluationDto
    _type_model = Evaluation
    _type_service = EvaluationService

    @staticmethod
    def map(evaluation: EvaluationDto) -> Evaluation:
        return Evaluation(evaluation.id, evaluation.state, evaluation.score,
                          CandidateAnswerHelper().map_all(evaluation.candidate_answer),
                          TechnologyHelper.map(evaluation.technology))

    # New behaviour #
    @staticmethod
    def retrieve_next_question(evaluation_id: str, technology_id: str) -> Optional[CandidateAnswer]:
        current_candidate_answer: CandidateAnswerDto = CandidateAnswerService().get_current_evaluation_candidate_answer(
            evaluation_id)
        if current_candidate_answer is not None:
            return CandidateAnswerHelper().map(current_candidate_answer)

        new_question: QuestionDto = QuestionService().get_question_technology(
            technology_id=technology_id,
            excluded_ids=list(
                map(lambda e: str(e.question_id),
                    CandidateAnswerService().get_closed_evaluation_candidate_answers(evaluation_id)))
        )

        new_candidate_answer: CandidateAnswerDto = CandidateAnswerService().set_current_evaluation_candidate_answer(
            evaluation_id=evaluation_id, question_id=new_question.id)

        return None if new_candidate_answer is None else CandidateAnswerHelper().map(new_candidate_answer)
