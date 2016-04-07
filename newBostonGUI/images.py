#importing Tkinter library
from tkinter import *


root =  Tk()

photo = PhotoImage(file="first_Logo.png")
label = Label(root, image= photo)
label.pack()
root.mainloop()
