#Display a red square moving down the canvas window.



from tkinter import *

def start():
    #moves the item
    #moves the y coordinate by 1
    #change the first letter to move the x coordinate
    canvas.move('blueSquare',450,250)

    #update the canvas
    canvas.update()

window = Tk()
button = Button(window,text="Jump", height = 5, width =12, command = start)
button.pack()

canvas = Canvas(window,width = 1000, height =700)
canvas.pack()

#create polygon - first parameters are the four corners to the make square
#there is also create_oval method

canvas.create_polygon(10,10,10,150,150,150,150,10,fill="blue", tag='blueSquare')

#move the image


window.mainloop()