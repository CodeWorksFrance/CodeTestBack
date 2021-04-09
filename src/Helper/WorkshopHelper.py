from typing import Optional

from src.Dto.EvaluationDto import EvaluationDto
from src.Dto.WorkshopDto import WorkshopDto
from src.Helper.EvaluationHelper import EvaluationHelper
from src.Helper.Helper import Helper
from src.Helper.ScoreHelper import ScoreHelper
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

    def retrieve_next_question(self, workshop_id: str) -> Optional[EvaluationQuestion]:
        # Check if the workshop is closed
        if WorkshopService().is_closed_workshop(workshop_id):
            return None

        # Get the current evaluation
        current_evaluation: EvaluationDto = self.get_current_evaluation(workshop_id)

        # Close the workshop if needed
        if current_evaluation is None:
            current_workshop: WorkshopDto = self.retrieve_by_index(workshop_id)
            score: float = ScoreHelper.get_average_score(list(map(lambda e: e.score, current_workshop.evaluation)))
            WorkshopService().close_workshop(workshop_id, score)
            return None

        next_question: EvaluationQuestion = EvaluationHelper().retrieve_next_question(current_evaluation.id,
                                                                                      current_evaluation.technology_id)

        if next_question is None:
            EvaluationHelper.close_evaluation(current_evaluation)
            return self.retrieve_next_question(workshop_id)

        return next_question

    def get_current_evaluation(self, workshop_id: str) -> Optional[EvaluationDto]:
        current_evaluation: EvaluationDto = EvaluationService().get_current_workshop_evaluation(workshop_id)

        if current_evaluation is None and not EvaluationService().has_potential_next_workshop_evaluation(workshop_id):
            return None

        if current_evaluation is not None:
            if EvaluationHelper().evaluation_must_be_closed(current_evaluation):
                EvaluationHelper.close_evaluation(current_evaluation)
                return self.get_current_evaluation(workshop_id)
            else:
                return current_evaluation

        EvaluationService().set_current_workshop_evaluation(workshop_id)
        return EvaluationService().get_current_workshop_evaluation(workshop_id)
