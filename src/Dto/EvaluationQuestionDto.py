from sqlalchemy import Column, String, Float, ForeignKey, text
from sqlalchemy.orm import relationship

from src.Dto import Base
from src.Enum.EvaluationQuestionState import EvaluationQuestionState


class EvaluationQuestionDto(Base):
    __tablename__ = 'evaluation_question'

    id = Column(String, primary_key=True, server_default=text('uuid_generate_v4()'))
    state = Column(String, default=EvaluationQuestionState.PENDING.value)
    score = Column(Float, nullable=True)
    evaluation_id = Column(String, ForeignKey('evaluation.id'))
    question_id = Column(String, ForeignKey('question.id'))
    question = relationship("QuestionDto", lazy='subquery')
    creation_date = Column(String, server_default=text('now()'))
