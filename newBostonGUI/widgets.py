from tkinter import *

root = Tk()

one = Label(root, text="One", bg="red",fg="white")
one.pack()
two = Label(root, text="Two", bg="green",fg="black")
two.pack(fill=X)#This means to fill the label the size of the parent
three = Label(root, text="Three", bg="gold",fg="white")
three.pack(side=LEFT, fill =Y)
root.mainloop()