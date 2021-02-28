import typing

from Dto.TechnologyDto import TechnologyDto
from Helper.QuestionHelper import QuestionHelper
from Models.Technology import Technology
from Service.TechnologyService import TechnologyService


class TechnologyHelper:
    def retrieve_technology(self) -> typing.List[Technology]:
        return self.map_technologies(TechnologyService.get_technologies())

    @staticmethod
    def map_technologies(technologies: [TechnologyDto]):
        return [Technology(t.id, t.label, t.type, QuestionHelper.map_questions(t.question)) for t in technologies]
