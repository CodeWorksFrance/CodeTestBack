import typing

from src.Dto.EvaluationDto import EvaluationDto
from src.Dto.WorkshopDto import WorkshopDto
from src.Helper.EvaluationHelper import EvaluationHelper
from src.Models.CandidateAnswer import CandidateAnswer
from src.Models.Workshop import Workshop
from src.Service.EvaluationService import EvaluationService
from src.Service.WorkshopService import WorkshopService


class WorkshopHelper:
    def retrieve_workshop(self, index: str) -> typing.List[Workshop]:
        return self.map_workshops(WorkshopService().get(index))

    def create_workshop(self, technologies: [str]) -> Workshop:
        workshop_id = WorkshopService().create_workshop(technologies)
        return self.retrieve_workshop(workshop_id)[0]

    @staticmethod
    def retrieve_next_question(workshop_id: str) -> [CandidateAnswer]:
        if WorkshopService().is_closed_workshop(workshop_id):
            return []

        if EvaluationService().get_current_workshop_evaluation(
                workshop_id) is None and not EvaluationService().has_potential_next_workshop_evaluation(workshop_id):
            WorkshopService().close_workshop(workshop_id)
            return []

        EvaluationService().set_current_workshop_evaluation(workshop_id)
        current_evaluation: EvaluationDto = EvaluationService().get_current_workshop_evaluation(workshop_id)

        return EvaluationHelper().retrieve_next_question(current_evaluation.id, current_evaluation.technology_id)

    @staticmethod
    def map_workshop(workshop: WorkshopDto):
        return Workshop(workshop.id, workshop.state, workshop.score,
                        EvaluationHelper.map_evaluations(workshop.evaluation))

    @staticmethod
    def map_workshops(workshops: [WorkshopDto]):
        return [Workshop(w.id, w.state, w.score, EvaluationHelper.map_evaluations(w.evaluation)) for w in workshops]
