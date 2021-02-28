from postgres import Postgres
from scr.Dto.QuestionDto import QuestionDto


class QuestionService:
    @staticmethod
    def get_questions(index: str) -> [QuestionDto]:
        session = Postgres.init_session()
        if index is None:
            return session.query(QuestionDto)

        return session.query(QuestionDto).filter_by(id=index)
