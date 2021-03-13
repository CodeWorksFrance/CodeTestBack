from typing import Optional

from src.Dto.EvaluationDto import EvaluationDto
from src.Dto.EvaluationQuestionDto import EvaluationQuestionDto
from src.Dto.QuestionDto import QuestionDto
from src.Helper.EvaluationQuestionHelper import EvaluationQuestionHelper
from src.Helper.Helper import Helper
from src.Helper.TechnologyHelper import TechnologyHelper
from src.Models.Evaluation import Evaluation
from src.Models.EvaluationQuestion import EvaluationQuestion
from src.Service.EvaluationQuestionService import EvaluationQuestionService
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
                          EvaluationQuestionHelper().map_all(evaluation.evaluation_question),
                          TechnologyHelper.map(evaluation.technology))

    # New behaviour #
    @staticmethod
    def retrieve_next_question(evaluation_id: str, technology_id: str) -> Optional[EvaluationQuestion]:
        evaluation_question: EvaluationQuestionDto = EvaluationQuestionService().get_current_evaluation_question(
            evaluation_id)
        if evaluation_question is not None:
            return EvaluationQuestionHelper().map(evaluation_question)

        new_question: QuestionDto = QuestionService().get_question_technology(
            technology_id=technology_id,
            excluded_ids=list(
                map(lambda e: str(e.question_id),
                    EvaluationQuestionService().get_closed_evaluation_questions(evaluation_id)))
        )

        new_evaluation_question: EvaluationQuestionDto = EvaluationQuestionService().set_current_evaluation_question(
            evaluation_id=evaluation_id, question_id=new_question.id)

        return None if new_evaluation_question is None else EvaluationQuestionHelper().map(new_evaluation_question)
