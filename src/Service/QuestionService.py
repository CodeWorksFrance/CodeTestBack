from db_config import DBConfig
from src.Dto.QuestionDto import QuestionDto


class QuestionService:
    @staticmethod
    def get_questions(index: str) -> [QuestionDto]:
        session = DBConfig().get_session()
        if index is None:
            query_result = session.query(QuestionDto)
            session.close()
            return query_result

        query_result = session.query(QuestionDto).filter_by(id=index)
        session.close()
        return query_result
