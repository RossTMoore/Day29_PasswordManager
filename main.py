from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list1 = [choice(letters) for char in range(randint(8, 10))]
    password_list2 = [choice(symbols) for char in range(randint(2, 4))]
    password_list3 = [choice(numbers) for char in range(randint(2, 4))]
    password_list = password_list1 + password_list2 + password_list3

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    new_web = web_entry.get()
    new_email = email_entry.get()
    new_password = password_entry.get()

    if len(new_web) == 0 or len(new_password) == 0:
        empty_field = messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=new_web, message=f"These are the details entered: \nEmail: {new_email} "
                                                          f"\nPassword: {new_password} \nIs it okay to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{new_web} | {new_email} | {new_password}\n")
                web_entry.delete(0, END)
                password_entry.delete(0, END)
                web_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
mypass_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_logo)
canvas.grid(row=0, column=1)

#Labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2, sticky='EW')


email_entry = Entry(width=35)
email_entry.insert(0, "ross@email.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky='EW')

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='EW')

#Buttons

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky='EW')

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

# --- LAST LINE ---#
window.mainloop()

