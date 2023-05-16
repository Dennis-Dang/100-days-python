from tkinter import *
import requests

BACKGROUND_COLOR = "#537188"
QUOTE_COLOR = "#CBB279"
AUTHOR_COLOR = "#E1D4BB"
BUTTON_COLOR = "#EEEEEE"


class WrappingLabel(Label):
    """A type of Label that automatically adjusts the wrap to the size"""
    def __init__(self, master=None, **kwargs):
        Label.__init__(self, master, **kwargs)
        self.bind('<Configure>', lambda e: self.config(wraplength=self.winfo_width()))


def get_quote():
    response = requests.get(url="https://zenquotes.io/api/random")
    data = response.json()[0]
    print(data["q"], data["a"])


window = Tk()
window.title("Motivational Quotes")
window.configure(bg=BACKGROUND_COLOR)
window.geometry("600x500")

frm_quote = Frame(master=window, background=BACKGROUND_COLOR)
lbl_quote = WrappingLabel(master=window, text="Quote", bg=BACKGROUND_COLOR, fg=QUOTE_COLOR, font=("Roboto", 20, "italic"))
lbl_author = Label(master=window, text="Author", bg=BACKGROUND_COLOR, fg=AUTHOR_COLOR, font=("Roboto", 20))

lbl_quote.pack(fill=X, pady=20)
lbl_author.pack()

btn_new_quote = Button(master=window, text="New Quote", background=BACKGROUND_COLOR, foreground=BUTTON_COLOR)
btn_new_quote.pack(pady=30)
window.mainloop()
