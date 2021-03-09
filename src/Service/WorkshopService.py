from db_config import DBConfig
from src.Dto.EvaluationDto import EvaluationDto
from src.Dto.WorkshopDto import WorkshopDto
from src.Enum.WorkshopState import WorkshopState
from src.Service.Service import Service


class WorkshopService(Service):
    _type = WorkshopDto

    def create_workshop(self, technologies: [str]) -> str:
        new_workshop = WorkshopDto()
        for technology_id in technologies:
            new_workshop.evaluation.append(EvaluationDto(workshop_id=new_workshop.id, technology_id=technology_id))

        return self.create(new_workshop).id

    def is_closed_workshop(self, index: str):
        query_result = self.get().filter(WorkshopDto.id == index).first()
        return query_result is None or query_result.state == WorkshopState.FINISHED

    def close_workshop(self, index: str):
        self.update(index=index, instruction={WorkshopDto.state: WorkshopState.FINISHED})
