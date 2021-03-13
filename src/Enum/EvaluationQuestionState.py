from enum import Enum


class EvaluationQuestionState(Enum):
    PENDING = 'Pending'
    CORRECT = 'Correct'
    INCORRECT = 'Incorrect'
    SKIPPED = 'Skipped'
