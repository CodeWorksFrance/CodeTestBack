from typing import Optional

from src.Dto.EvaluationDto import EvaluationDto
from src.Dto.WorkshopDto import WorkshopDto
from src.Helper.EvaluationHelper import EvaluationHelper
from src.Helper.Helper import Helper
from src.Models.EvaluationQuestion import EvaluationQuestion
from src.Models.Workshop import Workshop
from src.Service.EvaluationService import EvaluationService
from src.Service.WorkshopService import WorkshopService


class WorkshopHelper(Helper):
    # Inheritance #
    _type_dto = WorkshopDto
    _type_model = Workshop
    _type_service = WorkshopService

    @staticmethod
    def map(workshop: WorkshopDto) -> Workshop:
        return Workshop(workshop.id, workshop.state, workshop.score,
                        EvaluationHelper().map_all(workshop.evaluation))

    # New behaviour #
    def create_workshop(self, technologies: [str]) -> Workshop:
        return self.map(WorkshopService().create_workshop(technologies))

    @staticmethod
    def retrieve_next_question(workshop_id: str) -> Optional[EvaluationQuestion]:
        if WorkshopService().is_closed_workshop(workshop_id):
            return None

        if EvaluationService().get_current_workshop_evaluation(
                workshop_id) is None and not EvaluationService().has_potential_next_workshop_evaluation(workshop_id):
            WorkshopService().close_workshop(workshop_id)
            return None

        EvaluationService().set_current_workshop_evaluation(workshop_id)
        current_evaluation: EvaluationDto = EvaluationService().get_current_workshop_evaluation(workshop_id)

        return EvaluationHelper().retrieve_next_question(current_evaluation.id, current_evaluation.technology_id)
