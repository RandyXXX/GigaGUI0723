import tkinter
from tkinter import font
from tkinter.font import Font
from pprint import pprint

def func1():
    l1.config(text="button clecked")

def func2(ev):
    l1.config(text="cusor enter@(%d,%d)" % (ev.x,ev.y) ,bg="#AA22FF")
    print("ev=%s" % ev)

def func3(ev):
    l1.config(text="cusor leave@(%d,%d)" % (ev.x,ev.y),bg="#0122FF")

main=tkinter.Tk()
#pprint(font.families())
font1=Font(family="Segoe UI",size=24)
font2 = Font(family="標楷體", size=28)
l1 = tkinter.Label(main, text="status", font=font1, bg="#EEC0FF")
b1 = tkinter.Button(main, text="area", bg="#C0FFEE", font=font1, padx=20, pady=20,command=func1)
l1.pack(fill=tkinter.X)
b1.pack()
b1.bind("<Enter>",func2)
b1.bind("<Leave>",func3)
main.minsize(300, 200)
main.maxsize(300, 200)
main.mainloop()