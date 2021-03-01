from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from src.Dto import Base


class CategoryDto(Base):
    __tablename__ = 'category'

    id = Column(String, primary_key=True)
    label = Column(String)
    technology = relationship("TechnologyDto")
