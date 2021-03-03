import typing

from src.Dto import TechnologyDto
from src.Helper.QuestionHelper import QuestionHelper
from src.Models.Technology import Technology
from src.Service.TechnologyService import TechnologyService


class TechnologyHelper:
    def retrieve_technology(self) -> typing.List[Technology]:
        return self.map_technologies(TechnologyService.get_technologies())

    @staticmethod
    def map_technologies(technologies: [TechnologyDto]):
        return [Technology(t.id, t.label, t.type, t.image, QuestionHelper.map_questions(t.question))
                for t in technologies]

    @staticmethod
    def map_technology(technology: TechnologyDto):
        return Technology(technology.id, technology.label, technology.type, technology.image,
                          QuestionHelper.map_questions(technology.question))
