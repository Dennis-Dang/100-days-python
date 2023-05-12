from tkinter import *
from PIL import Image, ImageTk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


def get_canvas_size(event):
    canvas_width = event.width
    canvas_height = event.height
    print(canvas_width, canvas_height)


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(master=window, height=200, width=200)
logo_img = PhotoImage(file="logo.png")
image_item = canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0)

canvas.bind("<Configure>", get_canvas_size)

window.mainloop()
