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
window.config(padx=50, pady=50)
window.resizable(False, False)

canvas = Canvas(master=window, height=200, width=200)
logo_img = PhotoImage(file="logo.png")
image_item = canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0)
canvas.bind("<Configure>", get_canvas_size)

control_frame = Frame(master=window)
lbl_website = Label(master=control_frame, text="Website: ", pady=5)
lbl_username = Label(master=control_frame, text="Email/Username: ", pady=5)
lbl_password = Label(master=control_frame, text="Password: ", pady=5)
ent_website = Entry(master=control_frame)
ent_username = Entry(master=control_frame)


frame2 = Frame(master=control_frame)
ent_password = Entry(master=frame2)
btn_generate = Button(master=frame2, text="Generate Password")
ent_password.grid(column=0, row=0, sticky="w", padx=(0, 50))
btn_generate.grid(column=1, row=0, sticky="e")
frame2.grid(column=1, row=2, sticky="w")

lbl_website.grid(column=0, row=0, sticky="w")
ent_website.grid(column=1, row=0, sticky="ew")
lbl_username.grid(column=0, row=1, sticky="w")
ent_username.grid(column=1, row=1, sticky="ew")
lbl_password.grid(column=0, row=2, sticky="w")


btn_add = Button(master=control_frame, text="Add")
btn_add.grid(column=1, row=3, columnspan=2, sticky="ew", pady=10)
control_frame.grid(column=0, row=1)

window.mainloop()
