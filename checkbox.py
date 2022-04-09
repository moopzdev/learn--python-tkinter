# checkbox
from tkinter import *

root = Tk()
root.title("Checkboxes")
root.geometry("640x480-50-50")


def showChoice():
    choice1 = language1.get()
    choice2 = language2.get()
    choice3 = language3.get()
    choice4 = language4.get()

    if choice1 == 1:
        Label(text="Python is selected.").pack(anchor=W)
    if choice2 == 1:
        Label(text="Javascript is selected.").pack(anchor=W)
    if choice3 == 1:
        Label(text="Dart is selected.").pack(anchor=W)
    if choice4 == 1:
        Label(text="solidity is selected.").pack(anchor=W)

#  0 means not-selected ; 1 means selected


language1 = IntVar()
Checkbutton(text="Python", variable=language1).pack(anchor=W)
language2 = IntVar()
Checkbutton(text="Javascript", variable=language2).pack(anchor=W)
language3 = IntVar()
Checkbutton(text="Dart", variable=language3).pack(anchor=W)
language4 = IntVar()
Checkbutton(text="Solidity", variable=language4).pack(anchor=W)

Button(text="Show Selected Answer", command=showChoice).pack(anchor=W)
root.mainloop()
