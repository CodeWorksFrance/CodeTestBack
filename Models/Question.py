import strawberry


@strawberry.type
class Question:
    id: str
    label: str
    answer: str
    difficulty: str
