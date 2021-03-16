from src.Dto.EvaluationDto import EvaluationDto
from src.Enum.EvaluationState import EvaluationState
from src.Service.Service import Service


class EvaluationService(Service):
    _type = EvaluationDto

    def get_current_workshop_evaluation(self, workshop_id: str) -> EvaluationDto:
        return self.get().filter(EvaluationDto.workshop_id == workshop_id).filter(
            EvaluationDto.state == EvaluationState.IN_PROGRESS.value).first()

    def has_potential_next_workshop_evaluation(self, workshop_id: str) -> bool:
        return self.get().filter(EvaluationDto.workshop_id == workshop_id).filter(
            EvaluationDto.state == EvaluationState.PENDING.value).first() is not None

    def set_current_workshop_evaluation(self, workshop_id: str):
        query_result: EvaluationDto = self.get().filter(EvaluationDto.workshop_id == workshop_id).filter(
            EvaluationDto.state == EvaluationState.PENDING.value).first()

        if query_result is not None:
            self.update(index=query_result.id, instruction={EvaluationDto.state: EvaluationState.IN_PROGRESS.value})

    def close_evaluation(self, index: str, score: float):
        self.update(index=index,
                    instruction={EvaluationDto.state: EvaluationState.FINISHED, EvaluationDto.score: score})
