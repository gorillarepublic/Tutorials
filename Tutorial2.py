from tkinter import *

#This is a blank window
root = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", bg="black", fg="red")
button2 = Button(topFrame, text="Button 2", fg="purple")
button3 = Button(topFrame, text="Button 3", fg="yellow")
button4 = Button(bottomFrame, text="Button 4", fg="orange")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

#Display the window
root.mainloop()
