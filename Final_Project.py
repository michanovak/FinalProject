#Final_Project

from tkinter import *
from tkinter import messagebox

import os
import csv
import hashlib

LABEL = 'Portal'

class FieldNamesEnum(object):
    FIRST_NAME = 'First Name'
    LAST_NAME = 'Last Name'
    MAIL = 'E-Mail'
    USER = 'User Name'
    PASSWORD = 'Password'
    GENDER = 'Gender'

FIELD_NAMES = [FieldNamesEnum.FIRST_NAME, FieldNamesEnum.LAST_NAME, FieldNamesEnum.MAIL,
               FieldNamesEnum.USER, FieldNamesEnum.PASSWORD, FieldNamesEnum.GENDER]

#CSV File Path Saved Location
CSV_FILE_PATH = "users_info.csv"

#Fonts
FONT = ('Calibri', 14)

#Portal Menu Bar Definitions
def newFile():
    messagebox.showinfo(LABEL, 'New File')
    with open('New File.csv', 'w', newline='') as f:
     thewriter = csv.writer(f)

def openFile():
    messagebox.showinfo(LABEL, 'Open File')

def exit_app():
    messagebox.showinfo(LABEL, 'Good Bye')
    root.quit()

def about():
    messagebox.showinfo(LABEL, 'Designd By Micha')

#Password Hash Definitions
def get_password_hash_encode(password):
    result = hashlib.sha256(password.encode())

    return result.hexdigest()

#Portal Registration Definitions
def register():
    def _save_to_file():
        row_data = {FieldNamesEnum.FIRST_NAME: entry_first_name.get(),
                    FieldNamesEnum.LAST_NAME: entry_last_name.get(),
                    FieldNamesEnum.MAIL: entry_mail.get(),
                    FieldNamesEnum.USER: entry_user.get(),
                    FieldNamesEnum.PASSWORD: get_password_hash_encode(entry_password.get()),
                    FieldNamesEnum.GENDER: gender.get()}

        is_write_header = False
        if not os.path.exists(CSV_FILE_PATH):
            is_write_header = True
        with open(CSV_FILE_PATH, 'a+') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=FIELD_NAMES)
            if is_write_header:
                writer.writeheader()

            writer.writerow(row_data)

        messagebox.showinfo(
            LABEL,
            "The following data: {} written to file: {}".format(row_data, CSV_FILE_PATH))

#Portal window Appearance
    register_window = Toplevel(root)
    register_window.title("Portal Registration")
    register_window.geometry('600x500')
    register_window.resizable(width=False, height=False)
    register_window.configure(bg="#4c9bd4")

    label_first_name = Label(register_window, text="First Name: ", font=FONT)
    label_last_name = Label(register_window, text="Last Name: ", font=FONT)
    label_mail = Label(register_window, text="E-Mail: ", font=FONT)
    label_gender = Label(register_window, text="Gender: ", font=FONT)
    label_user = Label(register_window, text="User name: ", font=FONT)
    label_password = Label(register_window, text="Password: ", font=FONT)

    for curr_row_index, curr_label in enumerate([
        label_first_name, label_last_name, label_mail, label_user, label_password, label_gender],
            start=1):
        curr_label.grid(row=curr_row_index, column=0, columnspan=3)

    entry_first_name = Entry(register_window)
    entry_last_name = Entry(register_window)
    entry_mail = Entry(register_window)

# Radio variable
    gender = IntVar()
# Create two radio buttons
    male = Radiobutton(register_window, text="Male", variable=gender, value=1)
    female = Radiobutton(register_window, text="Female", variable=gender, value=0)

    entry_user = Entry(register_window)
    entry_password = Entry(register_window, show="*")

    entry_first_name.insert(0, "Enter your name")
    entry_last_name.insert(0, "Enter your last name")
    entry_mail.insert(0, "Enter your E-Mail")

    entry_user.insert(0, "Enter your user name")
    entry_password.insert(0, "Enter your password")

    for curr_row_index, curr_entry in enumerate([
        entry_first_name, entry_last_name, entry_mail, entry_user, entry_password],
            start=1):
        curr_entry.grid(row=curr_row_index, column=5)

    male.grid(row=curr_row_index + 1, column=4, columnspan=1)
    female.grid(row=curr_row_index + 1, column=5, columnspan=1)

    save_to_file = Button(register_window, text="Register", height="0", width="20", command=_save_to_file)
    save_to_file.grid(row=curr_row_index + 3, column=1)


def login():
    def _check_user_password():

        is_match = False
        if os.path.exists(CSV_FILE_PATH):
            with open(CSV_FILE_PATH, 'r') as csv_file:
                dict_reader = csv.DictReader(csv_file)

                for curr_dict in dict_reader:
                    if (curr_dict[FieldNamesEnum.USER] == entry_user.get() and
                            curr_dict[FieldNamesEnum.PASSWORD] == get_password_hash_encode(entry_password.get())):
                        is_match = True

                        break
        message_is_match = 'Welcome'
        message_is_not_match = 'User Name or Password incorrect!'

        message = message_is_not_match
        if is_match:
            message = message_is_match

        messagebox.showinfo(LABEL, message)

    login_window = Toplevel(root)
    login_window.title("Portal Login")
    login_window.geometry('600x500')
    login_window.resizable(width=False, height=False)
    login_window.configure(bg="#4c9bd4")

    label_user = Label(login_window, text="User Name In System: ", font=FONT)
    label_password = Label(login_window, text="Password In System: ", font=FONT)

    for curr_row_index, curr_label in enumerate([label_user, label_password], start=1):
        curr_label.grid(row=curr_row_index, column=0, columnspan=3)

    entry_user = Entry(login_window)
    entry_password = Entry(login_window, show="*")

    entry_user.insert(0, 'User Name')
    entry_password.insert(0, 'Password')

    for curr_row_index, curr_entry in enumerate([entry_user, entry_password], start=1):
        curr_entry.grid(row=curr_row_index, column=3)

    login_action = Button(login_window, text="Login", height="0", width="20", command=_check_user_password)
    login_action.grid(row=curr_row_index + 1, column=1)

#Portal Main Window
root = Tk()

#Portal Menu Bar
menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu)
menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New", command=newFile)
file_menu.add_command(label="Open", command=openFile)
file_menu.add_command(label="Exit", command=exit)

help_menu = Menu(menu)
menu.add_cascade(label="Help",menu=help_menu)
help_menu.add_cascade(label="About",command=about)
checkboxVar1 = IntVar()

root.config(menu=menu)
#Portal Window Appearance
root.grid()

root.title("Portal")
root.minsize(600, 500)
root.maxsize(900, 900)
root.resizable(width=False, height=False)
root.configure(bg="#4c9bd4")

login = Button(root, text="Login", height="0", width="20", command=login)
login.grid(row=1, column=0, padx=(10, 0), pady=(20, 0))

register = Button(root, text="Register", height="0", width="20", command=register)
register.grid(row=1, column=3, padx=(350, 0), pady=(20, 0))

root.mainloop()