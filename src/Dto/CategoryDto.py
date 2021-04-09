from sqlalchemy import Column, String, text, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.Dto import Base


class CategoryDto(Base):
    __table__ = Table(
        "category",
        Base.metadata,
        Column("id", UUID(as_uuid=True), primary_key=True, server_default=text('uuid_generate_v4()')),
        Column("label", String)
    )

    technology = relationship("TechnologyDto", lazy="subquery", order_by="TechnologyDto.label")
