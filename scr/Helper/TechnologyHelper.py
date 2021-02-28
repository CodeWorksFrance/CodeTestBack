import typing

from scr.Dto import TechnologyDto
from scr.Helper.QuestionHelper import QuestionHelper
from scr.Models.Technology import Technology
from scr.Service.TechnologyService import TechnologyService


class TechnologyHelper:
    def retrieve_technology(self) -> typing.List[Technology]:
        return self.map_technologies(TechnologyService.get_technologies())

    @staticmethod
    def map_technologies(technologies: [TechnologyDto]):
        return [Technology(t.id, t.label, t.type, QuestionHelper.map_questions(t.question)) for t in technologies]

    @staticmethod
    def map_technology(technologies: TechnologyDto):
        return Technology(technologies.id, technologies.label, technologies.type,
                          QuestionHelper.map_questions(technologies.question))
