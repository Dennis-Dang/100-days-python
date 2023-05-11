from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
# Color Hex
PINK = "#e2979c"
RED = "#ff6b6b"
GREEN = "#88cb00"
WHITE = "#f7fff7"
YELLOW = "#ffe66d"
ORANGE = "#fdaf75"

FONT_NAME = "Courier"

# Pomodoro minute intervals
# Default Pomodoro:
# 3 sets of (25-min Work + 5-min Short Break sessions)
# 1 final 25-min Work session
# 1 final 20-min Long Break session.
INTERVALS = {
    "WORK_MIN": 25,
    "SHORT_BREAK_MIN": 5,
    "LONG_BREAK_MIN": 20
}
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def cancel_timer():
    window.after_cancel(timer)


def reset_timer():
    if timer is not None:
        window.after_cancel(timer)
        global REPS
        REPS = 0
        canvas.itemconfig(timer_text, text='00:00', fill='white')
        btn_start.config(text="▶")
        lbl_title.config(text='Timer', fg=RED)
        lbl_status.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS

    if REPS == 8:
        reset_timer()

    REPS += 1

    if timer is not None:
        cancel_timer()

    btn_start.config(text="⏭")
    if REPS % 8 == 0:
        count_down(INTERVALS["LONG_BREAK_MIN"] * 60)
        lbl_title.config(text="20 Min Break", fg=RED)
        btn_start.config(text="🔄")
    elif REPS % 2 == 0:
        count_down(INTERVALS["SHORT_BREAK_MIN"] * 60)
        lbl_title.config(text="5 Min Break", fg=PINK)
    else:
        count_down(INTERVALS["WORK_MIN"]*60)
        lbl_title.config(text="25 Min Work", fg=GREEN)

    marks = ""
    num_work_sessions = floor(REPS / 2)
    for _ in range(num_work_sessions):
        marks += "✔"
    lbl_status.config(text=marks)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.resizable(False, False)
window.title("Pomodoro")
window.config(padx=20, pady=10, bg=YELLOW)

window.columnconfigure(0, weight=1, minsize=400)

# Create a canvas to layer UI objects.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=bg)
timer_text = canvas.create_text(100, 130, text="00:00", fill=WHITE, font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=0)

lbl_title = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=RED, bg=YELLOW)
lbl_title.grid(row=0, column=0)

frm_buttons = Frame(master=window, bg=YELLOW)
frm_buttons.grid(row=2, column=0, pady=(10, 0))

btn_start = Button(master=frm_buttons, text="▶", command=start_timer, font=(FONT_NAME, 25, "bold"),
                   fg=WHITE, bg=ORANGE, padx=20)
btn_start.pack(side="left", padx=(0, 50), pady=20)
btn_reset = Button(master=frm_buttons, text="Reset", command=reset_timer, font=(FONT_NAME, 25, "bold"),
                   fg=WHITE, bg=ORANGE)
btn_reset.pack(side="right", padx=(50, 0), pady=20)
lbl_status = Label(font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
lbl_status.grid(row=3, column=0, pady=20)


window.mainloop()
