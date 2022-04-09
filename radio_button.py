# input forms

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("640x480-50-50")
root.title("Form Inputs")


def showChoice():
    choice = language.get()
    if choice == 0:
        messagebox.showinfo("Alert", "You have chosen Javascript")
    if choice == 1:
        messagebox.showinfo("Alert", "You have chosen Python")
    if choice == 2:
        messagebox.showinfo("Alert", "You have chosen Solidity")
    if choice == 3:
        messagebox.showinfo("Alert", "You have chosen Dart")
    print(choice)


# adding radio button to program
language = IntVar()
language.set(2)
Radiobutton(text="Javascript", variable=language, value=0, command=showChoice).grid(
    row=0, column=0)
Radiobutton(text="Python", variable=language, value=1, command=showChoice).grid(
    row=1, column=0)
Radiobutton(text="Solidity", variable=language, value=2, command=showChoice).grid(
    row=2, column=0)
Radiobutton(text="Dart", variable=language, value=3, command=showChoice).grid(
    row=3, column=0)


# main loop
root.mainloop()
