from tkinter import *

root = Tk()

#3 seperate functions which run on events
def rightClick(event):
    print("Right")

def middleClick(event):
    print("Middle")

def leftClick(event):
    print("Left")

#Specify the height and width of the frame which sits inside the form
frame = Frame(root, width=1100, height=550)

#bind events to the frame
frame.bind("<Button-1>",rightClick)
frame.bind("<Button-2>",middleClick)
frame.bind("<Button-3>",leftClick)
frame.pack()

root.mainloop()
