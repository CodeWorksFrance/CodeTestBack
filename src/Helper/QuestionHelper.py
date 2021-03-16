from src.Dto import QuestionDto
from src.Helper.Helper import Helper
from src.Models.Question import Question
from src.Service.QuestionService import QuestionService


class QuestionHelper(Helper):
    # Inheritance #
    _type_dto = QuestionDto
    _type_model = Question
    _type_service = QuestionService

    @staticmethod
    def map(question: QuestionDto) -> Question:
        return Question(question.id, question.label, question.answer, question.difficulty)

    # New behaviour #
