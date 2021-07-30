import tkinter
from tkinter import font
from tkinter.font import Font
from pprint import pprint

main = tkinter.Tk()
pprint(font.families())
font1 = Font(family='Segoe UI', size=24)
font2 = Font(family="標楷體", size=28)
reliefs = ['flat', 'raised', 'sunken', 'solid', 'groove']
for r in reliefs:
    #button = tkinter.Button(main, font=font1, border=5 + i * 3)
    button = tkinter.Button(main, font=font1, relief=r,bg="#AA2570")
    button.pack()

main.mainloop()