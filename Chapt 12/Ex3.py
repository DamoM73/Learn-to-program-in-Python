from tkinter import *

def greeting():
    label.config (text = "Hello!")

def farewell():
    label.config (text = "Goodbye!")

window = Tk()
window.geometry("200x150")
window.title("Demo")
window.resizable(False, False)
window.configure(background = "Light blue")

label = Label(window, text = "Press a button")
label.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = 20)

button1 = Button(window, text="Greeting", width=7, command = greeting)
button1.grid(row = 1, column = 0, padx = 20)

button2 = Button(window, text = "Farewell", width = 7, command = farewell)
button2.grid(row = 1, column = 1, padx = 20)

window.mainloop()