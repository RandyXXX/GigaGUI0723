import tkinter
from tkinter import font
from tkinter.font import Font
from pprint import pprint


def func1(ev):
    message1.config(text=default_message % (ev.x, ev.y))


main = tkinter.Tk()
pprint(font.families())
font1 = Font(family='Segoe UI', size=24)
font2 = Font(family="標楷體", size=28)

default_message = "move to(%d,%d)"
message1 = tkinter.Message(main, text=default_message % (0, 0), font=font1, bg="#C0FFEE")
message1.pack(expand=True, fill=tkinter.BOTH)
message1.bind("<Motion>", func1)
main.minsize(800, 600)
main.maxsize(800, 600)
main.mainloop()
