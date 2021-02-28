import typing

import strawberry

from scr.Models.Question import Question


@strawberry.type
class Technology:
    id: str
    label: str
    type: str
    question: typing.List['Question']
