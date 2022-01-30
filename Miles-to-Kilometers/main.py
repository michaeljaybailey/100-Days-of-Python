from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)


def button_clicked():
    km = round(float(input.get()) * 1.609, 2)
    km_amount.config(text=km)


equal_to = Label(text="is equal to", font=("Arial", 16))
equal_to.grid(column=0, row=1)

km_amount = Label(font=("Arial", 16))
km_amount.grid(column=1, row=1)

mile_text = Label(text="Miles", font=("Arial", 16))
mile_text.grid(column=2, row=0)

km_text = Label(text="Km", font=("Arial", 16))
km_text.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

input = Entry(width=10)
input.grid(column=1, row=0)




window.mainloop()