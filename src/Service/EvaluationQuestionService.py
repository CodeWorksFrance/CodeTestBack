from src.Dto.EvaluationQuestionDto import EvaluationQuestionDto
from src.Enum.EvaluationQuestionState import EvaluationQuestionState
from src.Service.Service import Service


class EvaluationQuestionService(Service):
    _type = EvaluationQuestionDto

    def get_current_evaluation_question(self, evaluation_id: str) -> EvaluationQuestionDto:
        return self.get().filter(EvaluationQuestionDto.evaluation_id == evaluation_id).filter(
            EvaluationQuestionDto.state == EvaluationQuestionState.PENDING.value).first()

    def get_closed_evaluation_questions(self, evaluation_id: str) -> [EvaluationQuestionDto]:
        return self.get().filter(EvaluationQuestionDto.evaluation_id == evaluation_id).filter(
            EvaluationQuestionDto.state != EvaluationQuestionState.PENDING.value)

    def set_current_evaluation_question(self, evaluation_id: str, question_id: str) -> EvaluationQuestionDto:
        return self.create(EvaluationQuestionDto(evaluation_id=evaluation_id, question_id=question_id))
