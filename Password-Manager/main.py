from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    Password_Entry.delete(0, END)
    Password_Entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if len(Website_Entry.get()) == 0 or len(Email_Entry.get()) == 0 or len(Password_Entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=Website_Entry.get(), message=f"These are the details entered: \nEmail: {Email_Entry.get()} \nPassword: {Password_Entry.get()} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as add:
                add.write(f"{Website_Entry.get()} | {Email_Entry.get()} | {Password_Entry.get()}\n")
                Website_Entry.delete(0, END)
                Password_Entry.delete(0, END)

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

Password_Button = Button(text="Generate Password", command=generate_password)
Password_Button.grid(column=2, row=3, sticky="w")

Add_Button = Button(text="Add", width=44, command=save)
Add_Button.grid(column=1, row=4, columnspan=2, sticky="w")






window.mainloop()