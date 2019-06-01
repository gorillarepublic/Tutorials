from tkinter import *

root = Tk()

def printName(event):
    print("hello my name is bucky")

button_1 = Button(root, text="Print my Name")
button_1.bind("<Button-1>", printName)
button_1.pack()


root.mainloop()
