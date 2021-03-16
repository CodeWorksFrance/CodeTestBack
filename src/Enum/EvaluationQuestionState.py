from enum import Enum


class EvaluationQuestionState(Enum):
    PENDING = 'Pending'
    CORRECT = 'Correct'
    INCORRECT = 'Incorrect'
    SKIPPED = 'Skipped'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_
