import typing

import strawberry


@strawberry.type
class Question:
    id: str
    label: str
    answer: str
    difficulty: str
    alternative_answers: typing.Optional[typing.List[str]]
