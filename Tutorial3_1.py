from tkinter import *

#This is a blank window
root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

two = Label(topFrame, text="two", bg="green", fg="black")
two.pack(fill=X)


#Display the window
root.mainloop()