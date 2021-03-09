import uuid

from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from src.Dto import Base
from src.Enum.CandidateAnswerState import CandidateAnswerState


class CandidateAnswerDto(Base):
    __tablename__ = 'candidate_answer'

    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    state = Column(String, default=CandidateAnswerState.PENDING.value)
    score = Column(Float, nullable=True)
    evaluation_id = Column(String, ForeignKey('evaluation.id'))
    question_id = Column(String, ForeignKey('question.id'))
    question = relationship("QuestionDto", lazy='subquery')
