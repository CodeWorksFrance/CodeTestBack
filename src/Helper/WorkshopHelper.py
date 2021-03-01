import typing

from src.Dto.WorkshopDto import WorkshopDto
from src.Helper.EvaluationHelper import EvaluationHelper
from src.Models.Workshop import Workshop
from src.Service.WorkshopService import WorkshopService


class WorkshopHelper:
    def retrieve_workshop(self, index: str) -> typing.List[Workshop]:
        return self.map_workshops(WorkshopService.get_workshops(index))

    @staticmethod
    def map_workshops(workshops: [WorkshopDto]):
        return [Workshop(w.id, w.state, w.score, EvaluationHelper.map_evaluations(w.evaluation)) for w in workshops]
