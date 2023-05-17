import html
from question_model import Question

class QuizBrain:
    """
    Manages the quiz such as getting questions and keeping track of score.
    """
    def __init__(self, question_list):
        self.question_number = -1
        self.score = 0
        self.question_list = question_list

    def __str__(self):
        string = ""
        for question in self.question_list:
            string += f"Q: {question.text}, A: {question.answer}\n"
        return string

    def next_question(self):
        """
        Manages questions and formats them before passing it on to the UI component.
        :return: question as a string
        """
        self.question_number += 1
        question_text = html.unescape(self.get_cur_question().text)
        return f"Q.{self.question_number+1}: {question_text} (True/False)"
        # user_answer = input(f"Q.{self.question_number}: {question_text} (True/False)")
        # self.check_score(user_answer, cur_question.answer)

    def still_has_questions(self):
        """
        Checks if the question list is empty
        :return: True if there are still questions in the question list. Otherwise, returns false.
        """
        return self.question_number+1 < len(self.question_list)

    def get_cur_question(self) -> Question:
        return self.question_list[self.question_number]

    def check_score(self, user_answer: str):
        """
        Keeps the score for the game.
        :param user_answer: The user's answer to the question
        """
        # Sanitise API response.
        valid_strings = ["False", "True"]
        if self.get_cur_question().answer in valid_strings:
            # Check if user's answer is the same as question's answer.
            if user_answer == self.get_cur_question().answer:
                self.score += 1
                return True
            else:
                return False
        else:
            raise ValueError(f"Unexpected value found in Trivia API's correct answer: {self.get_cur_question().answer}")
