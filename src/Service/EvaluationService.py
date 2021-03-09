from db_config import DBConfig
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

    @staticmethod
    def set_current_workshop_evaluation(workshop_id: str):
        session = DBConfig().get_session()
        query_result: EvaluationDto = session.query(EvaluationDto).filter(
            EvaluationDto.workshop_id == workshop_id).filter(
            EvaluationDto.state == EvaluationState.PENDING).first()

        if query_result is not None:
            query_result.state = EvaluationState.IN_PROGRESS

        session.commit()
        session.close()
