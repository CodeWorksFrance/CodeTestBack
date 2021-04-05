from unittest import TestCase
from src.Dto.CategoryDto import CategoryDto
from src.Dto.QuestionDto import QuestionDto
from src.Dto.TechnologyDto import TechnologyDto
from src.Helper.CategoryHelper import CategoryHelper


class TestCategoryHelper(TestCase):
    def test_map_should_copy_id(self):
        # GIVEN
        helper = CategoryHelper()
        questionDto = QuestionDto(id='3456', label='q1', answer='answer', difficulty=5, technology_id='2345')
        technologyDto = TechnologyDto(id='2345', label='java', type='', image='', category_id='1234',
                                      question=[questionDto])
        categoryDto = CategoryDto(id='1234', label='language', technology=[technologyDto])

        # WHEN
        category = helper.map(categoryDto)

        # THEN
        self.assertEqual('1234', category.id)

    def test_map_should_copy_label(self):
        # GIVEN
        helper = CategoryHelper()
        questionDto = QuestionDto(id='3456', label='q1', answer='answer', difficulty=5, technology_id='2345')
        technologyDto = TechnologyDto(id='2345', label='java', type='', image='', category_id='1234',
                                      question=[questionDto])
        categoryDto = CategoryDto(id='1234', label='language', technology=[technologyDto])

        # WHEN
        category = helper.map(categoryDto)

        # THEN
        self.assertEqual('language', category.label)

    def test_map_should_copy_mapped_technology(self):
        # GIVEN
        helper = CategoryHelper()
        questionDto = QuestionDto(id='3456', label='q1', answer='answer', difficulty=5, technology_id='2345')
        technologyDto = TechnologyDto(id='2345', label='java', type='', image='', category_id='1234',
                                      question=[questionDto])
        categoryDto = CategoryDto(id='1234', label='language', technology=[technologyDto])

        # WHEN
        category = helper.map(categoryDto)

        # THEN
        self.assertEqual(1, len(category.technology))

    def test_map_should_copy_mapped_technologies(self):
        # GIVEN
        helper = CategoryHelper()
        questionDto = QuestionDto(id='3456', label='q1', answer='answer', difficulty=5, technology_id='2345')
        technologyDto = TechnologyDto(id='2345', label='java', type='', image='', category_id='1234',
                                      question=[questionDto])
        technologyDto2 = TechnologyDto(id='23456', label='java', type='', image='', category_id='1234',
                                       question=[questionDto])
        categoryDto = CategoryDto(id='1234', label='language', technology=[technologyDto, technologyDto2])

        # WHEN
        category = helper.map(categoryDto)

        # THEN
        self.assertEqual(2, len(category.technology))
