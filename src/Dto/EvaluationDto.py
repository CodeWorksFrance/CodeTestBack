from sqlalchemy import Column, String, Float, ForeignKey, text
from sqlalchemy.orm import relationship

from src.Dto import Base
from src.Enum.EvaluationState import EvaluationState


class EvaluationDto(Base):
    __tablename__ = 'evaluation'

    id = Column(String, primary_key=True, server_default=text('uuid_generate_v4()'))
    state = Column(String, default=EvaluationState.PENDING.value)
    score = Column(Float, nullable=True)
    workshop_id = Column(String, ForeignKey('workshop.id'))
    candidate_answer = relationship("CandidateAnswerDto", lazy='subquery')
    technology_id = Column(String, ForeignKey('technology.id'))
    technology = relationship("TechnologyDto", lazy='subquery')
