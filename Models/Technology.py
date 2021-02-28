import strawberry
import typing

from Models.Question import Question


@strawberry.type
class Technology:
    id: str
    label: str
    type: str
    question: typing.List['Question']
