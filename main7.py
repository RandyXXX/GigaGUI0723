import tkinter
from tkinter import font
from tkinter.font import Font
from pprint import pprint

items = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '0', '#']

main = tkinter.Tk()
font1 = Font(family='Segoe UI', size=24)

for i in range(4):
    for j in range(3):
        btn = tkinter.Button(main, text=items[i * 3 + j], font=font1,padx=20)
        btn.grid(row=i,column=j)

main.mainloop()