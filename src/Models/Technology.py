import typing

import strawberry

from src.Models.Question import Question


@strawberry.type
class Technology:
    id: str
    label: str
    type: str
    image: str
    question: typing.List[Question]
