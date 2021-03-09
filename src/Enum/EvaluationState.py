from enum import Enum


class EvaluationState(Enum):
    PENDING = 'Pending'
    IN_PROGRESS = 'In progress'
    FINISHED = 'Finished'
