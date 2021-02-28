from Dto.QuestionDto import QuestionDto
from postgres import Postgres


class QuestionService:
    @staticmethod
    def get_questions(index: str) -> [QuestionDto]:
        session = Postgres.init_session()
        if index is None:
            return session.query(QuestionDto)

        return session.query(QuestionDto).filter_by(id=index)
