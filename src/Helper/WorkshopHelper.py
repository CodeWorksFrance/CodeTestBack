import typing

from src.Dto.WorkshopDto import WorkshopDto
from src.Helper.EvaluationHelper import EvaluationHelper
from src.Models.Workshop import Workshop
from src.Service.WorkshopService import WorkshopService


class WorkshopHelper:
    def retrieve_workshop(self, index: str) -> typing.List[Workshop]:
        return self.map_workshops(WorkshopService.get_workshops(index))

    @staticmethod
    def map_workshop(workshop: WorkshopDto):
        return Workshop(workshop.id, workshop.state, workshop.score,
                        EvaluationHelper.map_evaluations(workshop.evaluation))

    @staticmethod
    def map_workshops(workshops: [WorkshopDto]):
        return [Workshop(w.id, w.state, w.score, EvaluationHelper.map_evaluations(w.evaluation)) for w in workshops]

    def create_workshop(self, technologies: [str]) -> Workshop:
        workshop_id = WorkshopService.create_workshop(technologies)
        return self.retrieve_workshop(workshop_id)[0]
