import pyshorteners
from tkinter import *

win = Tk()
win.geometry("400x370")
win.configure(bg="pink")
#button function
def short():
    url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    entry2.insert(END,s)

#label for entering user url
Label(win,text="Enter your url link",font="impack 17 bold",bg="black", fg="white").pack(fill="x")

#entry box
entry1 = Entry(win,font="10",bd=3,width=40)
entry1.pack(pady=30)

#button
Button(win,text="Click me",font="impack 12 bold ",bg="blue", fg="white",width="12",command=short).pack()

#entry
entry2=Entry(win,font="impack 16 bold ",bg="pink",width=24,bd=0)
entry2.pack(pady=30)


mainloop()