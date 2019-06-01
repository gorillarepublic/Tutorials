from tkinter import *

def doNothing():
    print("This will print something")
root = Tk()

frame = Frame(root, width=1100, height=550)
frame.pack_propagate(0)

#Add a text box which is the same size as the frame
Tb = Text(frame, width=1100, height=550)
Tb.pack()
#Enter some test text
Tb.insert(END, "Just a text Widget\nin two lines\n")

frame.pack()

menu = Menu(root)
root.config(menu=menu)

#Add a File menu
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)

subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Save As", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=frame.quit)

#Add a Edit menu
editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo",command=doNothing)

#Add a View menu
viewMenu = Menu(menu)
menu.add_cascade(label="View", menu=viewMenu)
viewMenu.add_command(label="Toggle Screen",command=doNothing)

#Add a Find menu
findMenu = Menu(menu)
menu.add_cascade(label="Find", menu=findMenu)
findMenu.add_command(label="Find in Buffer",command=doNothing)

#Add a Help menu
helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About",command=doNothing)

root.mainloop()
