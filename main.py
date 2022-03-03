import random
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- CONSTANTS  ---------------------------------- #
CHARBLACK = "#203239"
FONT_NAME = "Calibre"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    pwd_entry.delete(0, END)  # Deletes the previous entry and does not allow new password to append to last one.
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for each in range(randint(8, 10))]
    numbers_list = [choice(numbers) for each in range(randint(2, 4))]
    symbols_list = [choice(symbols) for each in range(randint(2, 4))]

    password_list = letters_list + numbers_list + symbols_list
    shuffle(password_list)

    password = "".join(password_list)
    pwd_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    pwd = pwd_entry.get()

    if len(website) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} \nPassword={pwd} \nIs it ok to save?")
        if is_ok:
            with open("myinfo.txt", "a") as data:
                data.write(f"{website} | {email} | {pwd}\n")
                website_entry.delete(0, END)
                pwd_entry.delete(0, END)  # Deletes the previous entry


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", fg=CHARBLACK, )
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", fg=CHARBLACK, )
email_label.grid(column=0, row=2)

pwd_label = Label(text="Password:", fg=CHARBLACK)
pwd_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "uditmishra.um@gmail.com")

pwd_entry = Entry(width=25)
pwd_entry.grid(column=1, row=3)

# Button
generate_button = Button(text="Generate Password", width=20, command=generate_password)
generate_button.grid(column=2, row=3, sticky="nw")

add_button = Button(text="Add", fg=CHARBLACK, width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
