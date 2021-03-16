import typing

import strawberry

from src.Models.EvaluationQuestion import EvaluationQuestion
from src.Models.Technology import Technology


@strawberry.type
class Evaluation:
    id: str
    state: str
    score: typing.Optional[float]
    evaluation_question: typing.List[EvaluationQuestion]
    technology: Technology
