import tkinter
from tkinter import font
from tkinter.font import Font
from pprint import pprint

message="您選擇的是:%s"

def func1():
    label1.config(text=message % 'pixel5')

def func2():
    label1.config(text=message % 'iPhone12')

def funcX():
    if sel1.get()==1:
        label1.config(text=message % 'pixel5')
        pass
    else:
        label1.config(text=message % 'iPhone12')
        pass

main = tkinter.Tk()
sel1 = tkinter.IntVar()
sel1.set(2)
#pprint(font.families())
font1 = Font(family='Segoe UI', size=24)
font2 = Font(family="標楷體", size=28)
label1 = tkinter.Label(main, text=message % '', font=font2)
rb1 = tkinter.Radiobutton(main, text="Android", font=font1,
                          value=1, variable=sel1,command=funcX)
rb2 = tkinter.Radiobutton(main, text="iOS", font=font1,
                          value=2, variable=sel1,command=funcX)
label1.pack()
rb1.pack()
rb2.pack()
main.mainloop()