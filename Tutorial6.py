from tkinter import *

root = Tk()

def printName():
    print("hello my name is bucky")

button_1 = Button(root, text="Print my Name", command=printName)
button_1.pack()

root.mainloop()