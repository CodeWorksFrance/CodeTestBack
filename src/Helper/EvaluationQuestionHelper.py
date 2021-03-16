from src.Dto import EvaluationQuestionDto
from src.Enum.EvaluationQuestionState import EvaluationQuestionState
from src.Helper.Helper import Helper
from src.Helper.ScoreHelper import ScoreHelper
from src.Helper.TechnologyHelper import TechnologyHelper
from src.Models.EvaluationQuestion import EvaluationQuestion
from src.Service.EvaluationQuestionService import EvaluationQuestionService


class EvaluationQuestionHelper(Helper):
    # Inheritance #
    _type_dto = EvaluationQuestionDto
    _type_model = EvaluationQuestion
    _type_service = EvaluationQuestionService

    @staticmethod
    def map(evaluation_question: EvaluationQuestionDto, technology_id: str = None) -> EvaluationQuestion:
        return EvaluationQuestion(evaluation_question.id, evaluation_question.state, evaluation_question.score,
                                  evaluation_question.creation_date, evaluation_question.question,
                                  TechnologyHelper().retrieve_by_index(technology_id))

    # New behaviour #
    @staticmethod
    def save_answer(evaluation_question_id: str, state: str):
        if not EvaluationQuestionState.has_value(state):
            raise ValueError("Invalid state")

        evaluation_question: EvaluationQuestionDto = EvaluationQuestionService().get(evaluation_question_id).first()
        if evaluation_question is None:
            raise ValueError("Invalid EvaluationQuestion id")

        score: float = 0.0 if state != EvaluationQuestionState.CORRECT.value else ScoreHelper.get_score(
            evaluation_question.question.difficulty)

        EvaluationQuestionService().set_evaluation_question_state(evaluation_question_id, state, score)
