from tkinter import *
from tkinter import messagebox
from password import Password



# import pandas
#
# # data_dic = {
# #     "website": [],
# #     "email": [],
# #     "password": []
# # }



# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
password_manager = Password()


def password_gen():
    password_entry.delete(0, END)
    print_password = password_manager.password_generate()
    password_entry.insert(END, string=str(print_password))

def update_password():
    password_entry.delete(0, END)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# using Pandas save password in csv

# def save_password():
#     web_save = website_entry.get()
#     email_save = email_entry.get()
#     pass_save = password_entry.get()
#
#     data_dic["website"].append(web_save)
#     data_dic["email"].append(email_save)
#     data_dic["password"].append(pass_save)
#
#     df = pandas.DataFrame(data_dic)
#     df.to_csv("password.csv")


def save_password():
    web_save = website_entry.get()
    email_save = email_entry.get()
    pass_save = password_entry.get()

    if len(web_save) == 0 or len(pass_save) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=web_save, message=f"These are the details entered: \nEmail: {email_save}"
                                                              f"\nPassword: {pass_save} \nIs it ok to save?")
        if is_ok:
            with open("password.txt", "a") as pass_file:
                pass_file.write(f" {web_save} | {email_save} | {pass_save} \n")

            password_entry.delete(0, END)
            website_entry.delete(0, END)
            update_password()


# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Generator")
windows.config(padx=100, pady=50, bg=YELLOW)

# canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# tomato_img = PhotoImage(file="tomato.png")
# canvas.create_image(100, 112, image=tomato_img)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.grid(column=1, row=1)

title_label = Label()
title_label.config(text="Password Manager", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=190, bg=YELLOW, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 85, image=logo_img)
canvas.grid(column=1, row=1)

website_label = Label(padx=10, pady=10)
website_label.config(text="Website :", fg=RED, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
website_label.grid(column=0, row=2)

email_label = Label(padx=10, pady=10)
email_label.config(text="Email :", fg=RED, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
email_label.grid(column=0, row=3)

password_label = Label(padx=10, pady=10)
password_label.config(text="Password :", fg=RED, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
password_label.grid(column=0, row=4)

website_entry = Entry(width=64)
website_entry.insert(END, string=" ")
website_entry.grid(column=1, row=2, columnspan=2)

email_entry = Entry(width=64)
email_entry.insert(END, string="maitrik.patel2025@gmail.com")
email_entry.grid(column=1, row=3, columnspan=2)

password_entry = Entry(width=35)
password_entry.insert(END, string="")
password_entry.grid(column=1, row=4)

password_button = Button(width=21, text="Generate password", command=password_gen, fg=RED, bg=GREEN, highlightthickness=0, font=(FONT_NAME, 10, "bold"))
password_button.grid(column=2, row=4)

Add_button = Button( width=70, text="Add",command=save_password, fg=RED, bg=GREEN, highlightthickness=0, font=(FONT_NAME, 10, "bold"))
Add_button.grid(column=1, row=5,columnspan=3)


windows.mainloop()