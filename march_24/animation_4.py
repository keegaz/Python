#Display a red square moving down the canvas window.
from tkinter import *
window = Tk()
canvas = Canvas (window,width = 1000, height =700)
canvas.pack()

#create polygon - first parameters are the four corners to the make square
#there is also create_oval method

canvas.create_polygon(10,10,10,150,150,150,150,10,fill="blue", tag='blueSquare')

#move the image

for x in range(0,750):
    #moves the y coodinate by 1
    #you change the frirst letter to mve the x coordinate
    canvas.move('blueSquare',1,0)

    #sets the gime fo the update -therefore speed of the animation
    canvas.after(2)

    #update the canvas
    canvas.update()
window.mainloop()