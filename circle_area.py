# circle's area calculator

from cgitb import text
import math
from tkinter import *

# initiating root window
root = Tk()
root.title("Circle Area Calculator")

# interface
Label(root, text="Enter a circle's radius", font=16).grid(row=0, sticky=W)
radius = IntVar()
et = Entry(textvariable=radius, font=16, width=30)
et.grid(row=0, column=1)

Label(root, text="Area of the circle is", font=16).grid(row=1, sticky=W)
et2 = Entry(font=16, width=30)
et2.grid(row=1, column=1)


def calculate_area():
    r = radius.get()
    area = math.pi * r ** 2
    et2.delete(0, END)
    et2.insert(0, area)


def clear_input():
    et.delete(0, END)
    et2.delete(0, END)


btn1 = Button(text="Calculate", command=calculate_area).grid(
    row=2, column=1, sticky=W)
btn2 = Button(text="Clear", command=clear_input).grid(
    row=2, column=1, sticky=E)

# main loop
root.mainloop()
