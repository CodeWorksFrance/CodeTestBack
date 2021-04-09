from sqlalchemy import Column, Float, ForeignKey, text, Enum, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.Dto import Base
from src.Enum.EvaluationState import EvaluationState


class EvaluationDto(Base):
    __table__ = Table(
        "evaluation",
        Base.metadata,
        Column("id", UUID(as_uuid=True), primary_key=True, server_default=text('uuid_generate_v4()')),
        Column("state", Enum('Pending', 'In progress', 'Finished'), default=EvaluationState.PENDING.value),
        Column("score", Float, nullable=True),
        Column("workshop_id", UUID(as_uuid=True), ForeignKey('workshop.id')),
        Column("technology_id", UUID(as_uuid=True), ForeignKey('technology.id'))
    )

    evaluation_questions = relationship("EvaluationQuestionDto", lazy="subquery",
                                        order_by="EvaluationQuestionDto.creation_date")
    technology = relationship("TechnologyDto", lazy="subquery")
