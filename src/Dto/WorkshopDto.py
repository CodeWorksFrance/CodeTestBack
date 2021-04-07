from sqlalchemy import Column, Float, text, Enum, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.Dto import Base
from src.Enum.WorkshopState import WorkshopState


class WorkshopDto(Base):
    __table__ = Table(
        "workshop",
        Base.metadata,
        Column("id", UUID(as_uuid=True), primary_key=True, server_default=text('uuid_generate_v4()')),
        Column("state", Enum('In progress', 'Finished'), default=WorkshopState.IN_PROGRESS.value),
        Column("score", Float, nullable=True)
    )

    evaluation = relationship("EvaluationDto", lazy="subquery", order_by="EvaluationDto.score")
