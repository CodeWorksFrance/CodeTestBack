import strawberry


@strawberry.type
class CandidateAnswer:
    id: str
    state: str
    score: float
