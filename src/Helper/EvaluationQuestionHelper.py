from src.Dto import EvaluationQuestionDto
from src.Helper.Helper import Helper
from src.Models.EvaluationQuestion import EvaluationQuestion
from src.Service.EvaluationQuestionService import EvaluationQuestionService


class EvaluationQuestionHelper(Helper):
    # Inheritance #
    _type_dto = EvaluationQuestionDto
    _type_model = EvaluationQuestion
    _type_service = EvaluationQuestionService

    @staticmethod
    def map(evaluation_question: EvaluationQuestionDto) -> EvaluationQuestion:
        return EvaluationQuestion(evaluation_question.id, evaluation_question.state, evaluation_question.score,
                                  evaluation_question.creation_date, evaluation_question.question)

    # New behaviour #
