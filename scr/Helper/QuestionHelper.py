import typing

from scr.Dto import QuestionDto
from scr.Models.Question import Question
from scr.Service.QuestionService import QuestionService


class QuestionHelper:
    def retrieve_question(self, index: str) -> typing.List[Question]:
        return self.map_questions(QuestionService.get_questions(index))

    @staticmethod
    def map_questions(questions: [QuestionDto]):
        return [Question(q.id, q.label, q.answer, q.difficulty) for q in questions]

    @staticmethod
    def map_question(question: QuestionDto):
        return Question(question.id, question.label, question.answer, question.difficulty)
