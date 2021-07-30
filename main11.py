import tkinter
from tkinter import font
from tkinter.font import Font
from pprint import pprint

counter=0
counter2=[0]

class Counter:
    def __init__(self):
        self.value=0

counter3=Counter()

def func1():
    #沒這個不會吃全域變數
    global counter
    counter += 1
    l1.config(text="button1 clicked %d times" % counter ,bg="#FFEEFF")


def func2():
    #global counter
    counter2[0]+=1
    l2.config(text="button2 clicked %d times" % counter2[0],bg="#FF11FF")

def func4():
    b4.pack_forget()

def func3():
    l3.config(text="button3 clicked %d times" % counter3.value, bg="#AA00FF")
    counter3.value+=1
    b4.pack()

print("func1 is",type(func1))
#print("func1() is",type(func1()))
main = tkinter.Tk()
#pprint(font.families())
font1 = Font(family='Segoe UI', size=24)
font2 = Font(family="標楷體", size=28)
l1=tkinter.Label(main,text="Label1",font=font1,bg="#AA6589")
l2=tkinter.Label(main,text="Label2",font=font2,bg="#BB1122")
l3=tkinter.Label(main,text="Label3",font=font2,bg="#BBFF22")
b1=tkinter.Button(main,text="Button1",font=font1,command=func1)
b2=tkinter.Button(main,text="Button2",font=font2,command=func2)
b3=tkinter.Button(main,text="Button3",font=font2,command=func3)
b4=tkinter.Button(main,text="Button4",font=font2,command=func4)

l1.pack()

l2.pack()
l3.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()


main.minsize(800,800)
main.maxsize(800,800)
main.mainloop()