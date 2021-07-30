import tkinter
from tkinter import font
from tkinter.font import Font
from pprint import pprint


def func1(ev):
    label1.config(text=message % int(ev))


message = "your value=%d"
main = tkinter.Tk()
value = tkinter.IntVar()
pprint(font.families())
font1 = Font(family='Segoe UI', size=24)
font2 = Font(family="標楷體", size=28)
label1 = tkinter.Label(main, text=message % value.get(), font=font1, bg="#C0FFEE")
scale1 = tkinter.Scale(main, label="volumn", font=font1, orient='h', variable=value,
                       command=func1)
label1.pack()
scale1.pack(fill=tkinter.X)
main.minsize(400, 300)
main.maxsize(400, 300)
main.mainloop()
