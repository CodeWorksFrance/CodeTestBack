import strawberry
import typing

from scr.Models.CandidateAnswer import CandidateAnswer
from scr.Models.Technology import Technology


@strawberry.type
class Evaluation:
    id: str
    state: str
    score: float
    candidate_answer: typing.List['CandidateAnswer']
    technology: Technology
