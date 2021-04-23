from src.Enum.Difficulty import Difficulty


class ScoreHelper:
    @staticmethod
    def get_score(value: str) -> float:
        switcher: dict = {
            Difficulty.D1.value: 1.0,
            Difficulty.D2.value: 2.0,
            Difficulty.D3.value: 3.0,
            Difficulty.D4.value: 4.0,
            Difficulty.D5.value: 5.0
        }
        return switcher.get(value, 0.0)

    @staticmethod
    def get_average_score(values: [float]) -> float:
        if len(values) == 0:
            return 0

        top_scores: [float] = values
        if len(values) > 3:
            values.sort()
            top_scores = values[-3:]

        return sum(top_scores) / len(top_scores)
