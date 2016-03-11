from tkinter import *

import tkinter.messagebox as tkMessageBox



def sound_message():

    root.bell()



root = Tk()

root.title("Welcome")

#button = Button(root, text="Click Me", command=show_alert)
button = Button(root, text ="Press here", command = sound_message)
button.grid(row=10, column=10)

root.mainloop()
