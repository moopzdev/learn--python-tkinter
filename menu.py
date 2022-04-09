from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Menu GUI")
root.geometry("640x480-50-50")


# Initializing-menu
myMenu = Menu()
root.config(menu=myMenu)


# COMMANDS

# creating a new window


def show_window():
    window = Tk()
    window.title("New Window")
    window.geometry("320x240")
    window.mainloop()

# about


def aboutProgram():
    messagebox.showinfo("About this program",
                        "Moopz_Dev develops this software.")

# exit


def exitProgram():
    confirm = messagebox.askquestion(
        "Confirm Exit?", "Are you sure you would like to close this program?")
    if confirm == "yes":
        root.destroy()


# preparing sub-menu-items
menuItem = Menu()
menuItem.add_command(label="New Window", command=show_window)
menuItem.add_command(label="Open...")
menuItem.add_command(label="Save")
menuItem.add_command(label="About", command=aboutProgram)
menuItem.add_command(label="Exit", command=exitProgram)


# adding menus
myMenu.add_cascade(label="File", menu=menuItem)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="View")


# main loop
root.mainloop()
