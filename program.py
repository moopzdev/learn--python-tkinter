from tkinter import *

# initialize an instance of TKINTER , and naming the title
root = Tk()
root.title("My GUI")
# program window size and position ("{height}x{weight}+{x-offset}+{y-offset}")
root.geometry("640x480+50+50")


# commands


def open_report():
    # 2nd screen
    myWindow = Tk()
    myWindow.title("Report Log")
    myWindow.geometry("500x800-50+50")
    s2_label = Label(myWindow, text="Report Log", font=16).pack()``
    myText = Entry(myWindow, textvariable=txt).pack()


def show_message():
    message = txt.get()
    myLabel2 = Label(myWindow, text=message, font=8).pack()


# widgets:label
myLabel = Label(root, text="Learning GUI with Tkinter",
                font=8, fg="black", bg="white").pack()


# message box
txt = StringVar()


# widgets:button
btn1 = Button(root, text="save", bg="green", command=show_message).pack()
btn2 = Button(root, text="Open Report", bg="blue", command=open_report).pack()


root.mainloop()
