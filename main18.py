import tkinter
from tkinter import font
from tkinter.font import Font
from pprint import pprint
from PIL import Image,ImageTk
import cv2

print(cv2.__version__)

main=tkinter.Tk()
main.geometry("640x480")

#pprint(font.families())
font1 = Font(family='Segoe UI', size=24)
font2 = Font(family="標楷體", size=28)

label1=tkinter.Label(main,bg="#00FFFF",text="Text")
label1.grid(row=0,column=0)
cap=cv2.VideoCapture(0)


def show_frames():
    cv2Image=cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    img=Image.fromarray(cv2Image)
    imageTk=ImageTk.PhotoImage(image=img)
    label1.imgtk=imageTk
    label1.configure(image=imageTk)
    label1.after(20,show_frames)
    pass

show_frames()


main.mainloop()