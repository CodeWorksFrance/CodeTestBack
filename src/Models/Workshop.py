import typing

import strawberry

from src.Models.Evaluation import Evaluation


@strawberry.type
class Workshop:
    id: str
    state: str
    score: typing.Optional[float]
    evaluation: typing.List['Evaluation']
