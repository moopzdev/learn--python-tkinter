# input forms

from tkinter import *

root = Tk()
root.geometry("640x480-50-50")
root.title("Form Inputs")

# adding radio button to program
language = IntVar()
Radiobutton(text="Javascript", variable=language, value=0).grid(
    row=0, column=0)
Radiobutton(text="Python", variable=language, value=1).grid(
    row=1, column=0)
Radiobutton(text="Solidity", variable=language, value=2).grid(
    row=2, column=0)
Radiobutton(text="Dart", variable=language, value=3).grid(
    row=3, column=0)


# main loop
root.mainloop()
