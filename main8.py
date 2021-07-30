import tkinter
from tkinter import font
from tkinter.font import Font
from pprint import pprint

main = tkinter.Tk()
font1 = Font(family='Segoe UI', size=24)

b1 = tkinter.Button(main, text="Python", font=font1)
b2 = tkinter.Button(main, text="VB.net", font=font1)
b3 = tkinter.Button(main, text="Java", font=font1)

b1.place(anchor=tkinter.NW,x=0,y=0,height=100, width=200)
b2.place(anchor=tkinter.CENTER,x=200,y=0,height=100, width=200)
b3.place(anchor=tkinter.SW,x=500,y=100,height=100, width=200)

main.minsize(800,800)
main.maxsize(800,800)
main.mainloop()
