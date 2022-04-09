from tkinter import font, ttk
from tkinter import *


# currency converters


'''
1 THB = 0.026 EUR
1 THB = 3.3486 JPY
1 THB = 0.031 USD
1 THB = 0.023 GBP
'''


root = Tk()
root.title("Currency Converter")

money = IntVar()
Label(text="Amount", padx=10, ).grid(row=0, sticky=W)
et1 = Entry(width=30, textvariable=money)
et1.grid(row=0, column=1)

choice = StringVar(value="Select a currency")
Label(text="Select a Currency", padx=10,).grid(row=1, sticky=W)
combo = ttk.Combobox(width=30, textvariable=choice)
combo["values"] = ("EUR", "JPY", "USD", "GBP")
combo.grid(row=1, column=1)

# output
Label(text="Amount in converted currency",
      padx=10).grid(row=2, sticky=W)
et2 = Entry(width=30)
et2.grid(row=2, column=1)

# calculate


def calculate():
    result = IntVar()
    amount = money.get()
    currency = choice.get()
    et2.delete(0, END)
    if currency == "EUR":
        result = amount * 0.026
        et2.insert(0, result)
    elif currency == "JPY":
        result = amount * 3.3486
        et2.insert(0, result)
    elif currency == "USD":
        result = amount * 0.031
        et2.insert(0, result)
    elif currency == "GBP":
        result = amount * 0.023
        et2.insert(0, result)
    else:
        pass


def clear_input():
    et1.delete(0, END)
    et2.delete(0, END)


Button(text="Calculate", width=10, command=calculate).grid(
    row=3, column=1, sticky=W)
Button(text="Clear", width=10, command=clear_input).grid(
    row=3, column=1, sticky=E)

root.mainloop()
