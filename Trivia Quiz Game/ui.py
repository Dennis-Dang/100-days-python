from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    """
    Interfaces the questions to put them onto a GUI screen display.
    """
    def __init__(self, quiz_brain: QuizBrain):
        """
        Creates the UI elements on display.
        :param quiz_brain: generates questions and keeps score
        """
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Trivia Quiz Game")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.lbl_score = Label(master=self.window, text="Score: 0", fg="white", bg=THEME_COLOR)
        self.lbl_score.grid(column=1, row=0, pady=20)

        self.canvas = Canvas(master=self.window, width=300, height=250)
        self.cnv_question = self.canvas.create_text((150, 125), width=280, text="Text", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, columnspan=2, row=1, rowspan=2, padx=20, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        self.btn_false = Button(master=self.window, image=false_img, highlightthickness=0, command=self.next_question)
        self.btn_true = Button(master=self.window, image=true_img, highlightthickness=0)
        self.btn_false.grid(column=0, row=3)
        self.btn_true.grid(column=1, row=3)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        """
        Generates a new question and displays it on the screen.
        """
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.cnv_question, text=question)