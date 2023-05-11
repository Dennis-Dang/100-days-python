from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
# Color Hex
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"

YELLOW = "#eaea7f"
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

# ---------------------------- TIMER RESET ------------------------------- #
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    REPS += 1

    if REPS % 8 == 0:
        count_down(INTERVALS["LONG_BREAK_MIN"] * 60)
        lbl_title.config(text="20 Min Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(INTERVALS["SHORT_BREAK_MIN"] * 60)
        lbl_title.config(text="5 Min Break", fg=PINK)
    else:
        count_down(INTERVALS["WORK_MIN"]*60)
        lbl_title.config(text="25 Min Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

# Create a canvas to layer UI objects.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=bg)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=0)

lbl_title = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=RED, bg=YELLOW)
lbl_title.grid(row=0, column=0, sticky='ew')

frm_buttons = Frame(master=window, bg=YELLOW)
frm_buttons.grid(row=2, column=0, pady=20)

btn_start = Button(master=frm_buttons, text="Start", command=start_timer)
btn_start.pack(side="left", padx=(0, 50))
btn_reset = Button(master=frm_buttons, text="Reset")
btn_reset.pack(side="right", padx=(50, 0))
lbl_status = Label(text="✔", font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
lbl_status.grid(row=3, column=0)


window.mainloop()
