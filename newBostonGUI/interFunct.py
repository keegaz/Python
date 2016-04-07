#importing Tkinter library
from tkinter import *

root =  Tk()

def printName(event):
    print("Hello my name is Bucky!")

button_1 = Button(root,text="Print my name")
button_1.bind("<Button-1>",printName)#lft button click for event

button_1.pack()
#button_1 = Button(root,text="Print my name", command=printName)

root.mainloop()