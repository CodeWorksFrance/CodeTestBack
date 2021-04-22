from src.Dto.EvaluationDto import EvaluationDto
from src.Dto.WorkshopDto import WorkshopDto
from src.Enum.WorkshopState import WorkshopState
from src.Service.Service import Service


class WorkshopService(Service):
    _type = WorkshopDto

    def create_workshop(self, technologies: [str]) -> WorkshopDto:
        new_workshop = WorkshopDto()
        for technology_id in technologies:
            new_workshop.evaluations.append(EvaluationDto(workshop_id=new_workshop.id, technology_id=technology_id))

        return self.create(new_workshop)

    def is_closed_workshop(self, index: str) -> bool:
        query_result = self.get().filter(WorkshopDto.id == index).first()
        return query_result is None or query_result.state == WorkshopState.FINISHED.value

    def close_workshop(self, index: str, score: float):
        self.update(index=index, instruction={WorkshopDto.state: WorkshopState.FINISHED, WorkshopDto.score: score})
