class QuizBrain:
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
        cur_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {cur_question.text} (True/False)")
        self.check_score(user_answer, cur_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_score(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You've got it right!")
            self.score += 1
        else:
            print("You've got it wrong.")
        print("The correct answer was: "+correct_answer)
        print(f"Your current score is: {self.score}/{self.question_number}\n")
