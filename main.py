import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
import random
# import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for char in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]
    random.shuffle(password_list)

    password = "".join(password_list)

    global pswd_entry
    pswd_entry.insert(0, f'{password}')
    # pyperclip.copy(password)

# ------SEARCHING FOR THE DATA ----------#
def search():
    saved_web = web_entry.get()
    try:
        with open("saved_pswd.json", mode= "r") as search_file:
            search_data = json.load(search_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No data", message=f"No details file found")
    else:
        if saved_web in search_data:
            web_key = search_data[saved_web]
            s_mail = web_key["email"]
            s_password = web_key["password"]
            messagebox.showinfo(title=f"Details for {saved_web} ", message=f"email:{s_mail}\n   password:{s_password}")
        else:
            messagebox.showinfo(title="No details ", message=f"No details found for {saved_web}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    saved_web= web_entry.get()
    saved_psw = pswd_entry.get()
    saved_user = user_entry.get()

    web_len = len(saved_web)
    pas_len = len(saved_psw)
    new_data = {
        saved_web:{
            "email": saved_user,
                "password": saved_psw,
        }
    }

    if web_len == 0 or pas_len == 0:
        messagebox.showinfo(title="No information Entered", message="Please type in a web address or a password")

    # -----AN OPTIONAL CONFIRMATORY MESSAGE AFTER INPUT-----#
    # else:
    #     confirm = messagebox.askokcancel(title=f'{saved_web}',message=f'confirm your details\nUsername:{saved_user}\n'
    #                                                      f'Password:{saved_psw}')
    # -----WRITING FILES IN A TXT FORMAT--------#
    # svd.write(f'Username:{saved_user}|| Web Address:{saved_web}|| Password:{saved_psw}\n')

    else:
        try:
            with open("saved_pswd.json", mode="r") as svd:
                data = json.load(svd)
        except FileNotFoundError:
            with open("saved_pswd.json", mode="w") as svd:
                json.dump(new_data, svd, indent=4)
        else:
            data.update(new_data)
            with open("saved_pswd.json", mode="w") as svd:
                json.dump(data, svd, indent=4)
        finally:
            web_entry.delete(0, END)
            pswd_entry.delete(0, END)
            web_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(pady=40, padx=40)
canvas = Canvas(width=200, height=200)
image1 = PhotoImage(file="logo.png")
canvas.create_image(130, 100, image=image1)
canvas.grid(row=0, column=1)


# --------WEBSITE LABEL --------#
web_label = Label()
web_label.config(text="Website:", font=("Courier"))
web_label.grid(row=1, column=0)

# -------WEB ENTRY-------#
web_entry = Entry(width=32)
web_entry.grid(row=1, column=1, columnspan=1)
web_entry.focus()

# -------USERNAME--------#
user_name = Label()
user_name.config(text="Username/Email:", font=("Courier"))
user_name.grid(row=2, column=0)


# ----USER ENTRY ------#
user_entry = Entry(width=63)
user_entry.grid(row=2, column= 1, columnspan=2)
user_entry.insert(END, "DonPee@yahoo.com")

# ------PASSWORD LABEL--------#
pswd_label = Label()
pswd_label.config(text="Password:", font=("Courier"))
pswd_label.grid(row=3, column=0)


# -----PASSWORD ENTRY--------#
pswd_entry = Entry(width=32)
pswd_entry.grid(row=3, column=1, columnspan=1)


# ------GENERATE BUTTON------#
gen_btn = Button()
gen_btn.config(text="Generate Password", font=("Courier"), command=pass_generator)
gen_btn.grid(row=3, column=2)


# ------SEARCH BUTTON------#
search_btn = Button(width=16)
search_btn.config(text="Search", font=("Courier"), command=search)
search_btn.grid(row=1, column=2)


# -------ADD BUTTON-------#
add_btn = Button(width= 38)
add_btn.config(text="Add", font=("Courier"), command=save_pass)
add_btn.grid(row=4, column=1, columnspan=2)







window.mainloop()