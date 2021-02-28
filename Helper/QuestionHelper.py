import typing

from Dto.QuestionDto import QuestionDto
from Models.Question import Question
from Service.QuestionService import QuestionService


class QuestionHelper:
    def retrieve_question(self, index: str) -> typing.List[Question]:
        return self.map_questions(QuestionService.get_questions(index))

    @staticmethod
    def map_questions(questions: [QuestionDto]):
        return [Question(q.id, q.label, q.answer, q.difficulty) for q in questions]
