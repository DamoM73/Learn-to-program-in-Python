# Program name: Ch 13 Sample app 2 validate password aaaaa.py
# Program askss use to login, then checks password
# in this program password is "aaaaaa"

from tkinter import *
from tkinter import messagebox

def submit():
    password = entry_password.get()
    username = entry_username.get()
    messageAlert = Label(root, width = 30)
    messageAlert.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)

    if password != "aaaaaa":
        messageAlert.config(text = "Password incorrect")
        entry_username.delete(0,"END")
        entry_password.delete(0,"END")
        entry_username.focus_set()

    else:
        messageAlert.config(text = "Password accepted")
        print("password accepted")
        print("Username: ", username)
        print("Password: ", password)
        messagebox.showinfo(title = "Password Ok", message = "Press OK to continue")
        root.destroy()

# display a message box with a hint for password
def hint():
    messagebox.showinfo(title = "Password hint", message = "Hint: Try password aaaaaa")

# create main window
root = Tk()
root.geometry("250x180")
root.title("Login Screen")
root.resizable(False,False)
root.configure(background = "Light blue")

# place a frame round labels and user entries
frame_entry = Frame(root, bg = 'Light blue')
frame_entry.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)

# place a frame around the buttons
frame_buttons = Frame(root, bg = "Light blue")
frame_buttons.grid(row = 2, column = 0, columnspan = 3, padx = 10 , pady = 10)

# place the labels and text entry fields
Label(frame_entry, text = "Enter username: ")\
    .grid(row = 0, column = 0, padx = 5, pady = 5)

entry_username = Entry(frame_entry, width = 15, bg = "white")
entry_username.grid(row = 0, column = 1, padx = 5, pady = 5)

Label(frame_entry, text = "Enter password: ")\
    .grid(row = 1, column = 0, padx = 10, pady = 10)

entry_password = Entry(frame_entry, width = 15, bg = "white", show = "*")
entry_password.grid(row = 1, column = 1, padx = 5, pady = 5)

# place the submit button
submit_button = Button(frame_buttons, text = "Submit", width = 8, command = submit)
submit_button.grid(row = 0, column = 0, padx = 5, pady = 5)

# place the Hint button
hint_button = Button(frame_buttons, text = "Hint", width = 15, command = hint)
hint_button.grid(row = 0, column = 1, padx = 5, pady = 5)

# run mainloop
root.mainloop()
print("carry on now...")