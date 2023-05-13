from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window =Tk()
window.title("Flash Card App")
window.config(background=BACKGROUND_COLOR)

canvas = Canvas(master=window, width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
img_card_front = PhotoImage(file="./images/card_front.png")
img_card_back = PhotoImage(file="./images/card_back.png")
canvas.create_image(400, 263, image=img_card_front)
canvas.create_text((400, 150), text="Title", font=("Arial", 40, "italic"))
canvas.create_text((400, 263), text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2, padx=50, pady=50)

control_frame = Frame(master=window, width=500, height=500, bg=BACKGROUND_COLOR)
img_right = PhotoImage(file="./images/right.png")
img_wrong = PhotoImage(file="./images/wrong.png")
btn_right = Button(master=control_frame, image=img_right, highlightthickness=0)
btn_wrong = Button(master=control_frame, image=img_wrong, highlightthickness=0)

btn_wrong.grid(column=0, row=0, padx=(0, 100))
btn_right.grid(column=1, row=0, padx=(100, 0))
control_frame.grid(column=0, row=1, columnspan=2, pady=(0, 50))

window.mainloop()
