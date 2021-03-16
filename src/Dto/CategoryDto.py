from sqlalchemy import Column, String, text
from sqlalchemy.orm import relationship

from src.Dto import Base


class CategoryDto(Base):
    __tablename__ = 'category'

    id = Column(String, primary_key=True, server_default=text('uuid_generate_v4()'))
    label = Column(String)
    technology = relationship("TechnologyDto", lazy='subquery')
