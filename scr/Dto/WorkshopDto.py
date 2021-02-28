from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship

from scr.Dto import Base


class WorkshopDto(Base):
    __tablename__ = 'workshop'

    id = Column(String, primary_key=True)
    state = Column(String)
    score = Column(Float)
    evaluation = relationship("EvaluationDto")