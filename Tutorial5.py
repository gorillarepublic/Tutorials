from tkinter import *

root = Tk()

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

#Now define their positions on a grid layout
label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

#Now add a check box and span it for 2 rows
c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)

root.mainloop()
