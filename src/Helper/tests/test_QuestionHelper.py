from unittest import TestCase

from src.Dto.QuestionDto import QuestionDto
from src.Helper.QuestionHelper import QuestionHelper


class TestQuestionHelper(TestCase):
    def test_map_should_copy_id(self):
        # GIVEN
        helper = QuestionHelper()
        questionDto = QuestionDto(id='3456', label='q1', answer='answer', difficulty=5, technology_id='2345')

        # WHEN
        question = helper.map(questionDto)

        # THEN
        self.assertEqual('3456', question.id)

    def test_map_should_copy_label(self):
        # GIVEN
        helper = QuestionHelper()
        questionDto = QuestionDto(id='3456', label='q1', answer='answer', difficulty=5, technology_id='2345')

        # WHEN
        question = helper.map(questionDto)

        # THEN
        self.assertEqual('q1', question.label)

    def test_map_should_copy_answer(self):
        # GIVEN
        helper = QuestionHelper()
        questionDto = QuestionDto(id='3456', label='q1', answer='answer', difficulty=5, technology_id='2345')

        # WHEN
        question = helper.map(questionDto)

        # THEN
        self.assertEqual('answer', question.answer)

    def test_map_should_copy_difficulty(self):
        # GIVEN
        helper = QuestionHelper()
        questionDto = QuestionDto(id='3456', label='q1', answer='answer', difficulty=5, technology_id='2345')

        # WHEN
        question = helper.map(questionDto)

        # THEN
        self.assertEqual(5, question.difficulty)
