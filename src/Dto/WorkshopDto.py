from sqlalchemy import Column, String, Float, text
from sqlalchemy.orm import relationship

from src.Dto import Base
from src.Enum.WorkshopState import WorkshopState


class WorkshopDto(Base):
    __tablename__ = 'workshop'

    id = Column(String, primary_key=True, server_default=text('uuid_generate_v4()'))
    state = Column(String, default=WorkshopState.IN_PROGRESS.value)
    score = Column(Float, nullable=True)
    evaluation = relationship("EvaluationDto", lazy='subquery')
