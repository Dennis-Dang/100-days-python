from tkinter import *
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"

to_learn_dict = {}
try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    original_data = pandas.read_csv("./data/EN-VN.csv")
    to_learn_dict = original_data.to_dict(orient='records')
else:
    to_learn_dict = df.to_dict(orient='records')
cur_card = {}

# ---------------------------- PICK RANDOM CARD ------------------------------- #


def next_card():
    global cur_card, flip_timer
    window.after_cancel(flip_timer)
    if len(to_learn_dict) != 0:
        cur_card = random.choice(to_learn_dict)
        chosen_word = cur_card['Vietnamese']
        canvas.itemconfig(card, image=img_card_front)
        canvas.itemconfig(title, text="Vietnamese", fill='black')
        canvas.itemconfig(word, text=chosen_word, fill='black')
        flip_timer = window.after(3000, func=flip_card)
    else:
        canvas.itemconfig(card, image=img_card_front)
        canvas.itemconfig(title, text="Congrats!", fill='black')
        canvas.itemconfig(word, text="You've learned\n the whole list!")

# ---------------------------- FLIP CARD ------------------------------- #


def flip_card():
    canvas.itemconfig(card, image=img_card_back)
    canvas.itemconfig(title, text="English", fill='white')
    canvas.itemconfig(word, text=cur_card["English"], fill='white')


# ------------------------- Update list ---------------------------------#
def is_known():
    if len(to_learn_dict) != 0:
        to_learn_dict.remove(cur_card)
        next_card()
        data = pandas.DataFrame(to_learn_dict)
        data.to_csv("./data/words_to_learn.csv", index=False)
# --------------------------UI ELEMENTS--------------------------------#
window =Tk()

window.title("Flash Card App")
window.config(background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(master=window, width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
img_card_front = PhotoImage(file="./images/card_front.png")
img_card_back = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(400, 263, image=img_card_front)
title = canvas.create_text((400, 150), text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text((400, 263), text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2, padx=50, pady=50)

control_frame = Frame(master=window, width=500, height=500, bg=BACKGROUND_COLOR)
img_right = PhotoImage(file="./images/right.png")
img_wrong = PhotoImage(file="./images/wrong.png")
btn_right = Button(master=control_frame, image=img_right, highlightthickness=0, command=is_known)
btn_wrong = Button(master=control_frame, image=img_wrong, highlightthickness=0, command=next_card)

btn_wrong.grid(column=0, row=0, padx=(0, 100))
btn_right.grid(column=1, row=0, padx=(100, 0))
control_frame.grid(column=0, row=1, columnspan=2, pady=(0, 50))

next_card()

window.mainloop()
