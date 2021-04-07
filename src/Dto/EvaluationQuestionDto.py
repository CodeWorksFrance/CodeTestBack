from sqlalchemy import Column, String, Float, ForeignKey, text, Enum, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.Dto import Base
from src.Enum.EvaluationQuestionState import EvaluationQuestionState


class EvaluationQuestionDto(Base):
    __table__ = Table(
        "evaluation_question",
        Base.metadata,
        Column("id", UUID(as_uuid=True), primary_key=True, server_default=text('uuid_generate_v4()')),
        Column("state", Enum('Pending', 'Correct', 'Incorrect', 'Skipped'),
               default=EvaluationQuestionState.PENDING.value),
        Column("score", Float, nullable=True),
        Column("evaluation_id", UUID(as_uuid=True), ForeignKey('evaluation.id')),
        Column("question_id", UUID(as_uuid=True), ForeignKey('question.id')),
        Column("creation_date", String, server_default=text('now()'))
    )

    question = relationship("QuestionDto", lazy="subquery")
