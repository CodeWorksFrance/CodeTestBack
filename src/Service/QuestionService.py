from sqlalchemy import desc

from src.Dto.QuestionDto import QuestionDto
from src.Service.Service import Service


class QuestionService(Service):
    _type = QuestionDto

    def get_question_technology(self, technology_id: str, difficulty: str, excluded_ids: [str] = None) -> QuestionDto:
        if excluded_ids is None:
            excluded_ids = []

        return self.get().filter(QuestionDto.technology_id == technology_id).filter(
            QuestionDto.id.notin_(excluded_ids)).order_by(desc(QuestionDto.difficulty == difficulty)).first()
