from sqlalchemy import Column, String, ForeignKey, text
from sqlalchemy.orm import relationship

from src.Dto import Base


class TechnologyDto(Base):
    __tablename__ = 'technology'

    id = Column(String, primary_key=True, server_default=text('uuid_generate_v4()'))
    label = Column(String)
    type = Column(String)
    image = Column(String)
    category_id = Column(String, ForeignKey('category.id'))
    question = relationship("QuestionDto", lazy='subquery')
