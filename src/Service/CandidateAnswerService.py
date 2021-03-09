from src.Dto.CandidateAnswerDto import CandidateAnswerDto
from src.Enum.CandidateAnswerState import CandidateAnswerState
from src.Service.Service import Service


class CandidateAnswerService(Service):
    _type = CandidateAnswerDto

    def get_current_evaluation_candidate_answer(self, evaluation_id: str) -> CandidateAnswerDto:
        return self.get().filter(CandidateAnswerDto.evaluation_id == evaluation_id).filter(
            CandidateAnswerDto.state == CandidateAnswerState.PENDING.value).first()

    def get_closed_evaluation_candidate_answer(self, evaluation_id: str) -> [CandidateAnswerDto]:
        return self.get().filter(CandidateAnswerDto.evaluation_id == evaluation_id).filter(
            CandidateAnswerDto.state != CandidateAnswerState.PENDING.value)

    def set_current_evaluation_candidate_answer(self, evaluation_id: str, question_id: str) -> CandidateAnswerDto:
        return self.create(CandidateAnswerDto(evaluation_id=evaluation_id, question_id=question_id))
