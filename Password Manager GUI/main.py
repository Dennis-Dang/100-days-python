from tkinter import *
from tkinter import messagebox
import password_gen
import pyperclip
import json

DEFAULT_EMAIL = "dennis@example.com"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    ent_password.delete(0, END)
    password = password_gen.generate_password()
    ent_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pwd():
    str_website = ent_website.get()
    str_username = ent_username.get()
    str_password = ent_password.get()

    json_data = {
        str_website: {
            "Email": str_username,
            "Password": str_password
        }
    }

    if len(str_website) == 0 or len(str_username) == 0 or len(str_password) == 0:
        messagebox.showinfo(title="Unfilled fields", message="All fields must be filled.")
    else:
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"Adding info to password file:\n\n"
                                                                     f"Website: \t{str_website}\n"
                                                                     f"Email/Username: \t{str_username}\n"
                                                                     f"Password: \t{str_password}")
        if is_ok:
            try:
                with open("data.json", mode='r') as file:
                    file_data = json.load(file)

            except FileNotFoundError:
                with open("data.json", mode='w') as file:
                    json.dump(json_data, file, indent=4)
            else:
                file_data.update(json_data)
                with open("data.json", mode='w') as file:
                    json.dump(file_data, file, indent=4)
            finally:
                ent_website.delete(0, END)
                ent_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.resizable(False, False)

canvas = Canvas(master=window, height=200, width=200)
logo_img = PhotoImage(file="logo.png")
image_item = canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0)

control_frame = Frame(master=window)
lbl_website = Label(master=control_frame, text="Website: ", pady=5)
lbl_username = Label(master=control_frame, text="Email/Username: ", pady=5)
lbl_password = Label(master=control_frame, text="Password: ", pady=5)
frame1 = Frame(master=control_frame)
ent_website = Entry(master=frame1)
ent_website.focus()
btn_search = Button(master=frame1, text="Search", width=15)
ent_website.grid(column=0, row=0, sticky="w",  padx=(0, 20))
btn_search.grid(column=1, row=0, sticky="e")
frame1.grid(column=1, row=0, sticky="ew")
ent_username = Entry(master=control_frame)


frame2 = Frame(master=control_frame)
ent_password = Entry(master=frame2)
btn_generate = Button(master=frame2, text="Generate Password", width=15, command=generate_password)
ent_password.grid(column=0, row=0, sticky="w", padx=(0, 20))
btn_generate.grid(column=1, row=0, sticky="e")
frame2.grid(column=1, row=2, sticky="w")

lbl_website.grid(column=0, row=0, sticky="w")
lbl_username.grid(column=0, row=1, sticky="w")
ent_username.grid(column=1, row=1, sticky="ew")
ent_username.insert(END, DEFAULT_EMAIL)
lbl_password.grid(column=0, row=2, sticky="w")


btn_add = Button(master=control_frame, text="Add", command=save_pwd)
btn_add.grid(column=1, row=3, columnspan=2, sticky="ew", pady=10)
control_frame.grid(column=0, row=1)

window.mainloop()
