from tkinter import *

#This is a blank window
root = Tk()

one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="two", bg="green", fg="black")
two.pack(fill=X)
three = Label(root, text="three", bg="blue", fg="black")
three.pack(side=RIGHT, fill=Y)

#Display the window
root.mainloop()