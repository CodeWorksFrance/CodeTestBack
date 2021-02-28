import strawberry
import typing

from scr.Models.CandidateAnswer import CandidateAnswer


@strawberry.type
class Evaluation:
    id: str
    state: str
    score: float
    candidate_answer: typing.List['CandidateAnswer']
