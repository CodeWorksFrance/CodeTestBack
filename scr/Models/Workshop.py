import strawberry
import typing

from scr.Models.Evaluation import Evaluation


@strawberry.type
class Workshop:
    id: str
    state: str
    score: float
    evaluation: typing.List['Evaluation']
