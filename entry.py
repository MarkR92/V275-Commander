from tkinter import *

root = Tk()

e = Entry(root)
e.pack()

def myClick():
    mylabel = Label(root, text="login")
    mylabel.pack()


myButton = Button(root, text="Login", command=myClick)
myButton.pack()

root.mainloop()
