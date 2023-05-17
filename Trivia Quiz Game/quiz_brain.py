import html


class QuizBrain:
    """
    Manages the quiz such as getting questions and keeping track of score.
    """
    def __init__(self, question_list):
        self.question_number = 0
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
        cur_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = html.unescape(cur_question.text)
        return f"Q.{self.question_number}: {question_text} (True/False)"
        # user_answer = input(f"Q.{self.question_number}: {question_text} (True/False)")
        # self.check_score(user_answer, cur_question.answer)

    def still_has_questions(self):
        """
        Checks if the question list is empty
        :return: True if there are still questions in the question list. Otherwise, returns false.
        """
        return self.question_number < len(self.question_list)

    def check_score(self, user_answer, correct_answer):
        """
        Keeps the score for the game.
        :param user_answer: The user's answer to the question
        :param correct_answer: The correct answer to the question
        """
        if user_answer.lower() == correct_answer.lower():
            print("You've got it right!")
            self.score += 1
        else:
            print("You've got it wrong.")
        print("The correct answer was: "+correct_answer)
        print(f"Your current score is: {self.score}/{self.question_number}\n")
