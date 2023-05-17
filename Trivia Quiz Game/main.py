from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for trivia in question_data:
    question_bank.append(Question(trivia["question"], trivia["correct_answer"]))

quiz = QuizBrain(question_bank)
ui = QuizInterface(quiz)
# print(quiz.next_question())

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")