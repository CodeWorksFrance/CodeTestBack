import typing

from scr.Dto.WorkshopDto import WorkshopDto
from scr.Helper.EvaluationHelper import EvaluationHelper
from scr.Models.Workshop import Workshop
from scr.Service.WorkshopService import WorkshopService


class WorkshopHelper:
    def retrieve_workshop(self, index: str) -> typing.List[Workshop]:
        return self.map_workshops(WorkshopService.get_workshops(index))

    @staticmethod
    def map_workshops(workshops: [WorkshopDto]):
        return [Workshop(w.id, w.state, w.score, EvaluationHelper.map_evaluations(w.evaluation)) for w in workshops]
