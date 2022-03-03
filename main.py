from tkinter import *

# ---------------------------- CONSTANTS  ---------------------------------- #
CHARBLACK = "#203239"
FONT_NAME = "Calibri"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    pwd = pwd_entry.get()

    with open("myinfo.txt", "a") as data:
        data.write(f"{website} | {email} | {pwd}\n")
    website_entry.delete(0, END)
    pwd_entry.delete(0, END)


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
website_label = Label(text="Website:", fg=CHARBLACK,)
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
generate_button = Button(text="Generate Password", width=20)
generate_button.grid(column=2, row=3, sticky= "nw")

add_button = Button(text="Add", fg=CHARBLACK, width=43, command= save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
