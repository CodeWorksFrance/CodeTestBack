import uuid

from db_config import DBConfig
from src.Dto.EvaluationDto import EvaluationDto
from src.Dto.WorkshopDto import WorkshopDto


class WorkshopService:
    @staticmethod
    def get_workshops(index: str) -> [WorkshopDto]:
        session = DBConfig().get_session()
        if index is None:
            query_result = session.query(WorkshopDto)
            session.close()
            return query_result

        query_result = session.query(WorkshopDto).filter_by(id=index)
        session.close()
        return query_result

    @staticmethod
    def create_workshop(technologies: [str]) -> str:
        new_workshop = WorkshopDto(id=str(uuid.uuid4()), state="In progress", evaluation=[])
        for technology_id in technologies:
            new_workshop.evaluation.append(
                EvaluationDto(id=str(uuid.uuid4()), state="Pending", workshop_id=new_workshop.id, technology_id=technology_id))

        session = DBConfig().get_session()
        session.add(new_workshop)
        session.commit()
        new_workshop_id = str(new_workshop.id)
        session.close()

        return new_workshop_id
