from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)


def convert_to_km():
    kilometers = int(miles.get()) * 1.609344
    kilometers_conversion.config(text=round(kilometers, 2))


miles = Entry(width=10)
miles.grid(column=1, row=0)

text_miles = Label(text="Miles", font=("Arial", 24))
text_miles.grid(column=2, row=0)

text_is_equal_to = Label(text="is equal to", font=("Arial", 24))
text_is_equal_to.grid(column=0, row=1)

text_km = Label(text="km", font=("Arial", 24))
text_km.grid(column=2, row=1)

kilometers_conversion = Label(text='0', font=("Arial", 24))
kilometers_conversion.grid(column=1, row=1)

calculate = Button(text="calculate", command=convert_to_km)
calculate.grid(column=1, row=2)

window.mainloop()
