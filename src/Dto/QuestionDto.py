from sqlalchemy import Column, String, ForeignKey, text

from src.Dto import Base


class QuestionDto(Base):
    __tablename__ = 'question'

    id = Column(String, primary_key=True, server_default=text('uuid_generate_v4()'))
    label = Column(String)
    answer = Column(String)
    difficulty = Column(String)
    technology_id = Column(String, ForeignKey('technology.id'))

    __mapper_args__ = {
        "order_by": difficulty
    }
