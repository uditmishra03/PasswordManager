from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

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


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=f"Error", message=f"No Data File found.")
    else:
        if website not in data:
            messagebox.showinfo(title=f"{website}", message=f"No details for the {website} exists.")
        else:
            email = data[website]['email']
            password = data[website]['password']

            messagebox.showinfo(title=f"{website}", message=f"Email: {email} \nPassword: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    pwd = pwd_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": pwd,
        }
    }

    if len(website) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating the old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving the update d data
                json.dump(data, data_file, indent=4)

        finally:
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
website_entry = Entry(width=25)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "uditmishra.um@gmail.com")

pwd_entry = Entry(width=25)
pwd_entry.grid(column=1, row=3)

# Button
search_button = Button(text="Search", width=20, command=find_password)
search_button.grid(column=2, row=1, sticky="nw")

generate_button = Button(text="Generate Password", width=20, command=generate_password, )
generate_button.grid(column=2, row=3, sticky="nw")

add_button = Button(text="Add", fg=CHARBLACK, width=43, command=save, highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
