from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = email_username_input.get()
    password = password_input.get()
    new_data = {website: {
        "email": username,
        "password": password,
    }}

    if website == "" or password == "":
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as file:
                # Read old data
                data = json.load(file)
                # Update old data with new data
                data.update(new_data)

            with open("data.json", mode="w") as file:
                # Save updated data
                json.dump(data, file, indent=4)

        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                # Save updated data
                json.dump(new_data, file, indent=4)

        finally:
            website_input.delete(0, END)
            website_input.focus()
            password_input.delete(0, END)


# ---------------------------- WEBSITE SEARCH ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        # search for the website in the data.json file
        # return the message box with the website as the title and the username / password as text / OK button
        with open("data.json", mode="r") as file:
            data = json.load(file)
            if website in data:
                username = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
            else:
                messagebox.showinfo(title=website, message="No details for that website exist.")
    except FileNotFoundError:
        # catch an exception that might occur to access the data.json showing a messagebox "No Data File Found"
        messagebox.showerror(title="File Not Found Error", message="No Data File Found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=240, height=240)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_image)
canvas.grid(column=0, row=0, columnspan=3)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

website_search = Button(text="Search", width=10, command=find_password)
website_search.grid(column=2, row=1)

email_username_label = Label(text="Username:")
email_username_label.grid(column=0, row=2)

email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "angela@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

password_button = Button(text="Generate Password", width=10, command=password_generator)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
