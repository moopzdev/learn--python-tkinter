# entrybox
from tkinter import *

# root initilization
root = Tk()
root.title("Entry Box")
# root.geometry("640x480-50-50")

Label(text="First Name: ").grid(row=0)
Label(text="Last Name: ").grid(row=1)
Label(text="Contact Tel.no: ").grid(row=2)

# entrybox
et1 = Entry()
et1.grid(row=0, column=1)
et1.insert(0, "Pongsathorn")
et2 = Entry()
et2.grid(row=1, column=1)
et2.insert(0, "Tiranun")
et3 = Entry()
et3.grid(row=2, column=1)
et3.insert(0, "090-996-9848")


def clear_data():
    et1.delete(0, END)
    et2.delete(0, END)
    et3.delete(0, END)


button = Button(text="Clear Data", command=clear_data).grid(row=3)
# mainloop
root.mainloop()
