from tkinter import *

window = Tk()

def greeting():
    label.config (text = "Hello")

def farewell():
    label.config (text = "Goodbye")

label = Label(window, text = "Press a button")
label.grid(row = 0, column = 0, columnspan = 2)

button1 = Button(window, text="Greeting", width=7, command = greeting)
button1.grid(row = 1, column = 0)

button2 = Button(window, text = "Farewell", width = 7, command = farewell)
button2.grid(row = 1, column = 1)

window.mainloop()