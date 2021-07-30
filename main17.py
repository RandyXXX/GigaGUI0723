import tkinter
from tkinter import font,messagebox
from tkinter.font import Font
from pprint import pprint
from PIL import Image, ImageTk

def func1():
    tkinter.messagebox.showinfo("About this","我要疫苗啦，幹")


# get a image to images\ directory
main = tkinter.Tk()
pprint(font.families())
font1 = Font(family='Segoe UI', size=24)
font2 = Font(family="標楷體", size=28)
PATH="D:\\tmp\\images\\test.jpg"
image=Image.open(PATH)
print(type(image))
photoImage=ImageTk.PhotoImage(image)
label1 = tkinter.Label(main, image=photoImage, bg="#C0FFEE")
label2 = tkinter.Label(main,text="超人", font=font2)
buttin1=tkinter.Button(main,text="AAA",font=font2,command=func1)
label1.pack()
label2.pack()
buttin1.pack()


main.mainloop()