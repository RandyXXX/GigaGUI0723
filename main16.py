import tkinter
from tkinter import font
from tkinter.font import Font
from pprint import pprint


def display(event):
    print(type(event), event)
    label1.config(text=entry1.get())


main = tkinter.Tk()
pprint(font.families())
font1 = Font(family='Segoe UI', size=24)
font2 = Font(family="標楷體", size=28)
label1 = tkinter.Label(main, font=font1, text="status")
entry1 = tkinter.Entry(main, font=font2)
button1 = tkinter.Button(main, font=font1, text="submit")
label1.pack()
entry1.pack()
button1.pack()
entry1.bind("<Return>", display)
button1.bind("<Button-1>", display)
main.mainloop()
