import strawberry
import typing

from src.Models.Question import Question
from src.Models.Technology import Technology


@strawberry.type
class EvaluationQuestion:
    id: str
    state: str
    score: typing.Optional[float]
    creation_date: str
    question: Question
    technology: typing.Optional[Technology]
