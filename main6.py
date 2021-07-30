import tkinter
from tkinter import font as font
from tkinter.font import   Font
from pprint import pprint
main=tkinter.Tk()

pprint(font.families())
#@是轉90度的字體
font1=Font(family='@微軟正黑體',size=24)
label1=tkinter.Label(main,text="按我",font=font1,padx=10,pady=30,bg="#321255")
button=tkinter.Button(main,text="Press Me",font=font1,padx=5,pady=20,bg="#665544")
label1.pack()
button.pack()
main.mainloop()