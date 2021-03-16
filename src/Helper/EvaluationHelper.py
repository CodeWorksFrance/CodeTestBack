from typing import Optional

from src.Dto.EvaluationDto import EvaluationDto
from src.Dto.EvaluationQuestionDto import EvaluationQuestionDto
from src.Dto.QuestionDto import QuestionDto
from src.Dto.TechnologyDto import TechnologyDto
from src.Enum.Difficulty import Difficulty
from src.Enum.EvaluationQuestionState import EvaluationQuestionState
from src.Enum.TechnologyType import TechnologyType
from src.Helper.EvaluationQuestionHelper import EvaluationQuestionHelper
from src.Helper.Helper import Helper
from src.Helper.TechnologyHelper import TechnologyHelper
from src.Models.Evaluation import Evaluation
from src.Models.EvaluationQuestion import EvaluationQuestion
from src.Service.EvaluationQuestionService import EvaluationQuestionService
from src.Service.EvaluationService import EvaluationService
from src.Service.QuestionService import QuestionService


class EvaluationHelper(Helper):
    # Inheritance #
    _type_dto = EvaluationDto
    _type_model = Evaluation
    _type_service = EvaluationService

    @staticmethod
    def map(evaluation: EvaluationDto) -> Evaluation:
        return Evaluation(evaluation.id, evaluation.state, evaluation.score,
                          EvaluationQuestionHelper().map_all(evaluation.evaluation_question),
                          TechnologyHelper.map(evaluation.technology))

    # New behaviour #
    __max_error_simple_question: int = 3
    __max_difficulty_good_answer_simple_question: int = 3

    def retrieve_next_question(self, evaluation_id: str, technology_id: str) -> Optional[EvaluationQuestion]:
        # Check if a question is already pending
        evaluation_question: EvaluationQuestionDto = EvaluationQuestionService().get_current_evaluation_question(
            evaluation_id)
        if evaluation_question is not None:
            return EvaluationQuestionHelper().map(evaluation_question)

        # If there is no pending question select a new one excluding the already asked
        new_question: QuestionDto = QuestionService().get_question_technology(
            technology_id=technology_id,
            difficulty=self.calculate_next_difficulty(evaluation_id=evaluation_id, technology_id=technology_id),
            excluded_ids=list(
                map(lambda e: str(e.question_id),
                    EvaluationQuestionService().get_closed_evaluation_questions(evaluation_id)))
        )

        # Create a new evaluation question for the question
        new_evaluation_question: EvaluationQuestionDto = EvaluationQuestionService().set_current_evaluation_question(
            evaluation_id=evaluation_id, question_id=new_question.id)

        return None if new_evaluation_question is None else EvaluationQuestionHelper().map(new_evaluation_question,
                                                                                           technology_id)

    def calculate_next_difficulty(self, evaluation_id: str, technology_id: str) -> str:
        technology: TechnologyDto = TechnologyHelper().retrieve_by_index(technology_id)
        if technology is None:
            return Difficulty.D1.value

        if technology.type == TechnologyType.SIMPLE_QUESTION.value:
            return self.calculate_next_difficulty_for_simple_question(evaluation_id)

        return Difficulty.D1.value

    def calculate_next_difficulty_for_simple_question(self, evaluation_id: str) -> str:
        asked_questions: [EvaluationQuestionDto] = EvaluationQuestionService().get_closed_evaluation_questions(
            evaluation_id)

        # Return first difficulty if it's the first question
        if len(asked_questions) == 0:
            return Difficulty.D1.value

        # Difficulty up if correct answers
        last_question_asked: EvaluationQuestionDto = asked_questions[-1]
        if last_question_asked.state == EvaluationQuestionState.CORRECT.value:
            return self.calculate_difficulty_up(last_question_asked.question.difficulty)

        # Difficulty down if 2 successive errors
        if (len(asked_questions) > 1 and last_question_asked.state == EvaluationQuestionState.INCORRECT.value and
                asked_questions[-2].state == EvaluationQuestionState.INCORRECT.value):
            return self.calculate_difficulty_down(last_question_asked.question.difficulty)

        # Same difficulty if skipped or first error
        return last_question_asked.question.difficulty

    def evaluation_must_be_closed(self, evaluation: EvaluationDto) -> bool:
        if evaluation.technology.type == TechnologyType.SIMPLE_QUESTION.value:
            return self.evaluation_must_be_closed_for_simple_question(evaluation)

        return True

    def evaluation_must_be_closed_for_simple_question(self, evaluation: EvaluationDto) -> bool:
        bad_answer = list(
            filter(lambda q: q.state == EvaluationQuestionState.INCORRECT.value, evaluation.evaluation_question))
        max_difficulty_good_answer = list(filter(
            lambda q: q.question.difficulty == Difficulty.D5.value and q.state == EvaluationQuestionState.CORRECT.value,
            evaluation.evaluation_question))

        if (len(bad_answer) >= self.__max_error_simple_question
                or len(max_difficulty_good_answer) >= self.__max_difficulty_good_answer_simple_question):
            return True

        return False

    @staticmethod
    def close_evaluation(evaluation: EvaluationDto):
        EvaluationService().close_evaluation(evaluation.id)

    @staticmethod
    def calculate_difficulty_up(current: str) -> str:
        switcher: dict = {
            Difficulty.D1.value: Difficulty.D2.value,
            Difficulty.D2.value: Difficulty.D3.value,
            Difficulty.D3.value: Difficulty.D4.value
        }

        return switcher.get(current, Difficulty.D5.value)

    @staticmethod
    def calculate_difficulty_down(current: str) -> str:
        switcher: dict = {
            Difficulty.D5.value: Difficulty.D4.value,
            Difficulty.D4.value: Difficulty.D3.value,
            Difficulty.D3.value: Difficulty.D2.value
        }

        return switcher.get(current, Difficulty.D1.value)
