from src.Dto import TechnologyDto
from src.Helper.Helper import Helper
from src.Helper.QuestionHelper import QuestionHelper
from src.Models.Technology import Technology
from src.Service.TechnologyService import TechnologyService


class TechnologyHelper(Helper):
    # Inheritance #
    _type_dto = TechnologyDto
    _type_model = Technology
    _type_service = TechnologyService

    @staticmethod
    def map(technology: TechnologyDto) -> Technology:
        return Technology(technology.id, technology.label, technology.type, technology.image,
                          QuestionHelper().map_all(technology.questions))

    # New behaviour #
