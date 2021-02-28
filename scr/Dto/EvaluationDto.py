from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from scr.Dto import Base


class EvaluationDto(Base):
    __tablename__ = 'evaluation'

    id = Column(String, primary_key=True)
    state = Column(String)
    score = Column(Float)
    workshop_id = Column(String, ForeignKey('workshop.id'))
    candidate_answer = relationship("CandidateAnswerDto")
    technology_id = Column(String, ForeignKey('technology.id'))
    technology = relationship("TechnologyDto")
