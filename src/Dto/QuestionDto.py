from sqlalchemy import Column, String, ForeignKey, text, Enum, Table
from sqlalchemy.dialects.postgresql import UUID

from src.Dto import Base


class QuestionDto(Base):
    __table__ = Table(
        "question",
        Base.metadata,
        Column("id", UUID(as_uuid=True), primary_key=True, server_default=text('uuid_generate_v4()')),
        Column("label", String),
        Column("answer", String),
        Column("difficulty", Enum('1', '2', '3', '4', '5')),
        Column("technology_id", UUID(as_uuid=True), ForeignKey('technology.id')),
        Column("alternative_answers", String)
    )
