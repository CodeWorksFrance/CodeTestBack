import strawberry

from scr.Models.Question import Question


@strawberry.type
class CandidateAnswer:
    id: str
    state: str
    score: float
    question: Question
