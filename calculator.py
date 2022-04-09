# calculator

from tkinter import *
root = Tk()
root.title("Calculator")

content = ""
txt_input = StringVar(value="0")


def btn(number):
    global content
    content = content + str(number)
    txt_input.set(content)


def equal():
    global content
    try:
        calculate = float(eval(content))
        txt_input.set(calculate)
        content = ""
    except Exception as e:
        print(e)
        txt_input.set("ERROR")
        content = ""


def clear():
    global content
    content = ""
    txt_input.set("")
    display.insert(0, "0")


# Display
display = Entry(font=('Courier', 24, 'bold'), fg='white',
                bg="darkblue", textvariable=txt_input, justify="right")
display.grid(columnspan=4)

# Inputs
# row1
btn7 = Button(fg="black", font=('Courier', 16, 'bold'),
              padx=30, pady=4, text="7", command=lambda: btn(7)).grid(row=1, column=0)
btn8 = Button(fg="black", font=('Courier', 16, 'bold'),
              padx=30, pady=4, text="8", command=lambda: btn(8)).grid(row=1, column=1)
btn9 = Button(fg="black", font=('Courier', 16, 'bold'),
              padx=30, pady=4, text="9", command=lambda: btn(9)).grid(row=1, column=2)
btnC = Button(fg="white", bg="red", font=('Courier', 16, 'bold'),
              padx=30, pady=4, text="C", command=clear).grid(row=1, column=3)

# row2
btn4 = Button(fg="black", font=('Courier', 16, 'bold'),
              padx=30, pady=4, text="4", command=lambda: btn(4)).grid(row=2, column=0)
btn5 = Button(fg="black", font=('Courier', 16, 'bold'),
              padx=30, pady=4, text="5", command=lambda: btn(5)).grid(row=2, column=1)
btn6 = Button(fg="black", font=('Courier', 16, 'bold'),
              padx=30, pady=4, text="6", command=lambda: btn(6)).grid(row=2, column=2)
btnPlus = Button(fg="black", bg="orange", font=('Courier', 16, 'bold'),
                 padx=30, pady=4, text="+", command=lambda: btn("+")).grid(row=2, column=3)

# row3
btn1 = Button(fg="black", font=('Courier', 16, 'bold'),
              padx=30, pady=4, text="1", command=lambda: btn(1)).grid(row=3, column=0)
btn2 = Button(fg="black", font=('Courier', 16, 'bold'),
              padx=30, pady=4, text="2", command=lambda: btn(2)).grid(row=3, column=1)
btn3 = Button(fg="black", font=('Courier', 16, 'bold'),
              padx=30, pady=4, text="3", command=lambda: btn(3)).grid(row=3, column=2)
btnMinus = Button(fg="black", bg="orange", font=('Courier', 16, 'bold'),
                  padx=30, pady=4, text="-", command=lambda: btn("-")).grid(row=3, column=3)

# row4

btnDot = Button(fg="black", font=('Courier', 16, 'bold'),
                padx=30, pady=4, text=".", command=lambda: btn(".")).grid(row=4, column=0)
btn0 = Button(fg="black", font=('Courier', 16, 'bold'),
              padx=30, pady=4, text="0", command=lambda: btn(0)).grid(row=4, column=1)
btnDiv = Button(fg="black", font=('Courier', 16, 'bold'),
                padx=30, pady=4, text="/", command=lambda: btn("/")).grid(row=4, column=2)
btnMult = Button(fg="black", bg="orange", font=('Courier', 16, 'bold'),
                 padx=30, pady=4, text="x", command=lambda: btn('*')).grid(row=4, column=3)

# row5

btnEqual = Button(fg="black", bg="lightblue", font=('Courier', 16, 'bold'),
                  padx=30, pady=4, text="ANS", command=equal).grid(row=5, column=0, columnspan=2)
btnOpen = Button(fg="black", bg="olive", font=('Courier', 16, 'bold'),
                 padx=30, pady=4, text="(", command=lambda: btn("(")).grid(row=5, column=2)
btnClose = Button(fg="black", bg="olive", font=('Courier', 16, 'bold'),
                  padx=30, pady=4, text=")", command=lambda: btn(")")).grid(row=5, column=3)

root.mainloop()
