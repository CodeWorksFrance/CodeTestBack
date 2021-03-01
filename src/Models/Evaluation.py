import typing

import strawberry

from src.Models.CandidateAnswer import CandidateAnswer
from src.Models.Technology import Technology


@strawberry.type
class Evaluation:
    id: str
    state: str
    score: float
    candidate_answer: typing.List['CandidateAnswer']
    technology: Technology
