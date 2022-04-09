from tkinter import *
from tkinter import ttk

root = Tk()
root.title("ComboBox")
Label(text="Address").grid(row=0, column=0)
choice = StringVar(value="Select Your Province")
combo = ttk.Combobox(textvariable=choice)
combo["values"] = ("Bangkok", "Chiang Mai", "Krabi", "Rayong")
combo.grid(row=0, column=1)


def select_city():
    Label(text="You selected the province of " +
          choice.get()+".").grid(row=2, columnspan=2)


btn = Button(text="Input", command=select_city)
btn.grid(row=1, column=1)
root.mainloop()
