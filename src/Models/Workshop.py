import typing

import strawberry

from src.Models.Evaluation import Evaluation


@strawberry.type
class Workshop:
    id: str
    state: str
    score: typing.Optional[float]
    evaluations: typing.List[Evaluation]
