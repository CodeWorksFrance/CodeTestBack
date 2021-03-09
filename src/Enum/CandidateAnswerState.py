from enum import Enum


class CandidateAnswerState(Enum):
    PENDING = 'Pending'
    CORRECT = 'Correct'
    INCORRECT = 'Incorrect'
    SKIPPED = 'Skipped'
