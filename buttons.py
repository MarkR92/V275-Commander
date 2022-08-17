from tkinter import *

root = Tk()


def myClick():
    mylabel = Label(root, text="Click")
    mylabel.pack()


myButton = Button(root, text="Login", command=myClick)
myButton.pack()

root.mainloop()
