import strawberry
import typing

from src.Models.Question import Question


@strawberry.type
class CandidateAnswer:
    id: str
    state: str
    score: typing.Optional[float]
    question: Question
