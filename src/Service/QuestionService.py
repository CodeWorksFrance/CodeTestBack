from db_config import DBConfig
from src.Dto.QuestionDto import QuestionDto


class QuestionService:
    @staticmethod
    def get_questions(index: str) -> [QuestionDto]:
        session = DBConfig().init_session()
        if index is None:
            return session.query(QuestionDto)

        return session.query(QuestionDto).filter_by(id=index)
