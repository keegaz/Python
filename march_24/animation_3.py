#Display a red square moving down the canvas window.
from tkinter import *
window = Tk()
canvas = Canvas (window,width = 1000, height =700)
canvas.pack()
canvas.pack( side = RIGHT)


#create polygon - first parameters are the four corners to the make square
#there is also create_oval method

canvas.create_polygon(850,10,850,150,1530,150,1530,10,fill="blue", tag='blueSquare')
canvas.pack (side = RIGHT)

#move the image

for x in range(0,500):
    #moves the y coodinate by 1
    #you change the frirst letter to mve the x coordinate
    canvas.move('blueSquare',0,1)

    #sets the gime fo the update therefore speed of the animation
    canvas.after(2)

    #update the canvas
    canvas.update()
window.mainloop()