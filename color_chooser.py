from tkinter import *
from tkinter.colorchooser import *
from tkinter.dialog import *
from tkinter.filedialog import askopenfile

# initializing project
root = Tk()
root.geometry("640x480-50-50")
root.title("Color Picker")


def select_color():
    color = askcolor()
    print(color[0])  # RGB color code
    print(color[1])  # Hex color code
    myLabel = Label(text="Hello Python", bg=color[1]).pack()


def select_file():
    fileopen = askopenfile()
    myLabel = Label(text=fileopen).pack()


btn = Button(root, text="Pick a color", command=select_color).pack()
btn = Button(root, text="Select a file", command=select_file).pack()

# mainloop
root.mainloop()
