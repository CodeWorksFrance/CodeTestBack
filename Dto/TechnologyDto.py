from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from Dto import Base


class TechnologyDto(Base):
    __tablename__ = 'technology'

    id = Column(String, primary_key=True)
    label = Column(String)
    type = Column(String)
    category_id = Column(String, ForeignKey('category.id'))
    question = relationship("QuestionDto")
