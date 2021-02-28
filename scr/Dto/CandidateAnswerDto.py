from sqlalchemy import Column, String, Float, ForeignKey

from scr.Dto import Base


class CandidateAnswerDto(Base):
    __tablename__ = 'candidate_answer'

    id = Column(String, primary_key=True)
    state = Column(String)
    score = Column(Float)
    evaluation_id = Column(String, ForeignKey('evaluation.id'))