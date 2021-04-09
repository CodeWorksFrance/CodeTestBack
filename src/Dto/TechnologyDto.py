from sqlalchemy import Column, String, ForeignKey, text, Enum, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.Dto import Base


class TechnologyDto(Base):
    __table__ = Table(
        "technology",
        Base.metadata,
        Column("id", UUID(as_uuid=True), primary_key=True, server_default=text('uuid_generate_v4()')),
        Column("label", String),
        Column("type", Enum('Simple questions', 'State questions', 'Multiple choice questions', 'Image questions')),
        Column("image", String),
        Column("category_id", UUID(as_uuid=True), ForeignKey('category.id'))
    )

    questions = relationship("QuestionDto", lazy="subquery", order_by="QuestionDto.difficulty")
