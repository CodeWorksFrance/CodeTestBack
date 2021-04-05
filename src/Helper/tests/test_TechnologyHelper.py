from unittest import TestCase

from src.Dto.QuestionDto import QuestionDto
from src.Dto.TechnologyDto import TechnologyDto
from src.Helper.TechnologyHelper import TechnologyHelper


class TestTechnologyHelper(TestCase):
    def test_map_should_copy_id(self):
        # GIVEN
        helper = TechnologyHelper()
        questionDto = QuestionDto(id='3456', label='q1', answer='answer', difficulty=5, technology_id='2345')
        technologyDto = TechnologyDto(id='2345', label='java', type='', image='', category_id='1234',
                                      question=[questionDto])

        # WHEN
        technology = helper.map(technologyDto)

        # THEN
        self.assertEqual('2345', technology.id)

    def test_map_should_copy_label(self):
        # GIVEN
        helper = TechnologyHelper()
        questionDto = QuestionDto(id='3456', label='q1', answer='answer', difficulty=5, technology_id='2345')
        technologyDto = TechnologyDto(id='2345', label='java', type='', image='', category_id='1234',
                                      question=[questionDto])

        # WHEN
        technology = helper.map(technologyDto)

        # THEN
        self.assertEqual('java', technology.label)

    def test_map_should_copy_type(self):
        # GIVEN
        helper = TechnologyHelper()
        questionDto = QuestionDto(id='3456', label='q1', answer='answer', difficulty=5, technology_id='2345')
        technologyDto = TechnologyDto(id='2345', label='java', type='type', image='', category_id='1234',
                                      question=[questionDto])

        # WHEN
        technology = helper.map(technologyDto)

        # THEN
        self.assertEqual('type', technology.type)

    def test_map_should_copy_image(self):
        # GIVEN
        helper = TechnologyHelper()
        questionDto = QuestionDto(id='3456', label='q1', answer='answer', difficulty=5, technology_id='2345')
        technologyDto = TechnologyDto(id='2345', label='java', type='type', image='0987654321', category_id='1234',
                                      question=[questionDto])

        # WHEN
        technology = helper.map(technologyDto)

        # THEN
        self.assertEqual('0987654321', technology.image)

    def test_map_should_copy_mapped_question(self):
        # GIVEN
        helper = TechnologyHelper()
        questionDto = QuestionDto(id='3456', label='q1', answer='answer', difficulty=5, technology_id='2345')
        technologyDto = TechnologyDto(id='2345', label='java', type='type', image='0987654321', category_id='1234',
                                      question=[questionDto])

        # WHEN
        technology = helper.map(technologyDto)

        # THEN
        self.assertEqual(1, len(technology.question))

    def test_map_should_copy_mapped_questions(self):
        # GIVEN
        helper = TechnologyHelper()
        questionDto = QuestionDto(id='3456', label='q1', answer='answer', difficulty=5, technology_id='2345')
        questionDto2 = QuestionDto(id='34567', label='q2', answer='answer2', difficulty=5, technology_id='2345')
        technologyDto = TechnologyDto(id='2345', label='java', type='type', image='0987654321', category_id='1234',
                                      question=[questionDto, questionDto2])

        # WHEN
        technology = helper.map(technologyDto)

        # THEN
        self.assertEqual(2, len(technology.question))