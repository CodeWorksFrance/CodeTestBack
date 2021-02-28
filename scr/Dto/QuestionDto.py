from sqlalchemy import Column, String, ForeignKey

from scr.Dto import Base


class QuestionDto(Base):
    __tablename__ = 'question'

    id = Column(String, primary_key=True)
    label = Column(String)
    answer = Column(String)
    difficulty = Column(String)
    technology_id = Column(String, ForeignKey('technology.id'))
