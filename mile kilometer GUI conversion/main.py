from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.config(padx=50, pady=50)


def convert_to_km():
    kilometers = int(miles.get()) * 1.609344
    kilometers_conversion.config(text=round(kilometers, 2))


miles = Entry(width=10)
miles.grid(column=0, row=0)

text_miles = Label(text="Miles", font=("Arial", 24))
text_miles.grid(column=1, row=0, sticky='w')

kilometers_conversion = Label(text='0', font=("Arial", 24))
kilometers_conversion.grid(column=0, row=1)

text_km = Label(text="Kilometers", font=("Arial", 24))
text_km.grid(column=1, row=1, sticky='w')

calculate = Button(text="calculate", command=convert_to_km)
calculate.config(padx="20")
calculate.grid(column=2, row=1)

window.mainloop()
