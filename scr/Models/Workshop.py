import strawberry


@strawberry.type
class Workshop:
    id: str
    state: str
    score: float
