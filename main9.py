import tkinter
from tkinter import font
from tkinter.font import Font
from pprint import pprint

main = tkinter.Tk()
font1 = Font(family='Segoe UI', size=24)

b1 = tkinter.Button(main, text="button1", font=font1,bg="#C0FEEF")
b2 = tkinter.Button(main, text="button2", font=font1,bg="#22FEEF")
b3 = tkinter.Button(main, text="button3", font=font1,bg="#22CDAA")
b4 = tkinter.Button(main, text="button4", font=font1,bg="#50FEAB")
b5 = tkinter.Button(main, text="button5", font=font1,bg="#65AAEF")
b6 = tkinter.Button(main, text="button6", font=font1,bg="#89F34F")
#b1.pack(expand=True,fill=tkinter.X)
b1.pack(fill=tkinter.X)
#b2.pack(expand=True,fill=tkinter.Y)
b2.pack(side=tkinter.LEFT)

#b3.pack(side=tkinter.LEFT)
#b4.pack(side=tkinter.TOP)
#b5.pack(side=tkinter.RIGHT)
#b6.pack(side=tkinter.BOTTOM)

b3.pack(side=tkinter.LEFT,fill=tkinter.Y)
b4.pack(side=tkinter.TOP)
b5.pack(side=tkinter.TOP,fill=tkinter.X)
b6.pack(side=tkinter.TOP,expand=True,fill=tkinter.BOTH)
main.minsize(800,800)
main.maxsize(800,800)
main.mainloop()