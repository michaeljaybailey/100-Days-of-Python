from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    with open("data.txt", "a") as add:
        add.write(f"{Website_Entry.get()} | {Email_Entry.get()} | {Password_Entry.get()}\n")
        Website_Entry.delete(0, END)
        Password_Entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

Website_Label = Label(text="Website:", font=("Courier", 12))
Website_Label.grid(column=0, row=1)

Email_Label = Label(text="Email/Username:", font=("Courier", 12))
Email_Label.grid(column=0, row=2)

Password_Label = Label(text="Password:", font=("Courier", 12))
Password_Label.grid(column=0, row=3)

Website_Entry = Entry(width=52)
Website_Entry.grid(column=1, row=1, columnspan=2, sticky="w")
Website_Entry.focus()

Email_Entry = Entry(width=52)
Email_Entry.grid(column=1, row=2, columnspan=2, sticky="w")
Email_Entry.insert(0, "FakeEmail@Fake.com")

Password_Entry = Entry(width=30)
Password_Entry.grid(column=1, row=3, sticky="w")

Password_Button = Button(text="Generate Password")
Password_Button.grid(column=2, row=3, sticky="w")

Add_Button = Button(text="Add", width=44, command=save)
Add_Button.grid(column=1, row=4, columnspan=2, sticky="w")






window.mainloop()