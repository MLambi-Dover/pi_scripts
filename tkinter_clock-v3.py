#!/usr/bin/env python
# This is a tkinter version of the Berlin Uhr
# A quantity didactic clock; lights are arranged in rows of various values
# At the top a blinking seconds circle, followed by rows of rectangles
# 4x 5 hours each
# 4x 1 hour each
# 11x 5 minutes, arranged vertically
# 4x 1 minute

# This is a tkinter exercise, so that gets imported
# We also need to be able to get a time string to tell the time
# importing ttk was/is aspirational
import tkinter as tk
# from tkinter import ttk  # haven't done anything with this so...
from time import strftime

# These variables are for the size of the canvas and the title of the window

title = "Yup"
width = 800
height = 800
# colors
red = 'red'
lightRed = 'beige'
grey = 'grey'
secondsYellow = 'yellow'
green = 'green'

window = tk.Tk()
window.title(title)
window.iconbitmap('e:/images/icons/saucer.ico') # if you don't have this comment the line out

# exit buttons are always convenient. I like them on the bottom, but this is easier
exitButton = tk.Button(window, text='Exit', command=window.quit, padx=25)
exitButton.pack() # don't forget, packing is order dependent; this will be on top

myCanvas = tk.Canvas(window, width=width, height=height)
myCanvas.pack()

# cross hair; used these for early testing to make sure things were where I thought/wanted
# myCanvas.create_line(0,200,400,200)
# myCanvas.create_line(200,0,200,400)

circleSize = width/8
topOfCircle = width/8
rowNumber = 1 # initializing; will be incremented when building the different rows
rowWidth = .9 * width  # this makes the clock take up 90% of the width of the canvas
paddingLeft = (.1 * width) / 2  # the padding on the left and right are 1/2 of 10%
spacerSize = (.1 * width) / 3  # this is the space between rectangles for 3 of the rows
spacerSizeTall = (.2 * width) / 10  # this is the spacer for the 11x 5-Minute columns
sizeX = (.8*width)/4  # this sets the width of the rectangles for Hx5, H, and M
sizeXtall = (.7*width)/11  # sets the width of the 5x-Minute row
sizeY = width/16  # all of the rows should be the same height, for now
sizeYtall = sizeX  # all of the rows should be the same height, for now

# print(f"rowWidth: {rowWidth}, paddingLeft: {paddingLeft}, spacerSize: {spacerSize}, sizeX: {sizeX}")

# draw the circle
def drawCircle(seconds):
    if int(seconds) %2 == 0: # on/off for even/odd seconds
        color = secondsYellow
    else:
        color = 'grey99'
    circleMiddle = (width/2) # centers the circle at half the width
    x1 = circleMiddle-(circleSize/2)
    x2 = circleMiddle+(circleSize/2)
    # print(f'circleMiddle: {circleMiddle}, x1: {x1}')  # lots of print statements left behind from debugging
    # the size of the circle is 50, created statically below, that should probably be defined in above
    myCanvas.create_oval(x1, topOfCircle, x2, topOfCircle+(width/8), fill=color)

# this functions draws the rows for the 5x-Hour, Hour and Minute rows
# the rowName designates which. time is called in the original loop and passed here
# each time this function is called
def makeRowX4(rowName, timeString): # make a row of four rectangles; can be used for Hx5, Hx1 and Mx1
    color = 'grey99'
    startingY = topOfCircle + circleSize + spacerSize
    if rowName == 'hoursX1':
        startingY = startingY + spacerSize + sizeY
    elif rowName == 'minX1':
        startingY = startingY + spacerSize + sizeY*2 + spacerSize*2 + sizeYtall + spacerSize/2

    x1 = (width - rowWidth)/2 # we start at 1/2 of the space left from rowWidth; centers it
    y1 = startingY
    x2 = x1 + sizeX
    y2 = y1 + sizeY
    for i in range(4):
        if rowName == 'minX1':
            if i + 1 <= int(timeString) % 5:  # bottom row or 1 minute rectangles
                color = 'green'
            else:
                color = 'grey99'
        elif rowName == 'hoursX1':
            if i + 1 <= int(timeString) % 5:  # like the minute row, below the top row
                color = 'green'
            else:
                color = 'grey99'
        elif rowName == 'hoursX5':
            if i + 1 <= int(timeString) / 5:  # the top row, 5 hour blocks (the math is different)
                color = 'green'
            else:
                color = 'grey99'
        # print(f"cycle: {i} - x1={x1}, y1={y1}, x2={x2}, y2={y2}")  # more amateur debugging
        myCanvas.create_rectangle(x1,y1,x2,y2, fill=color)
        x1 = x2 + spacerSize  # increment x
        x2 = x2 + spacerSize + sizeX  # increment x2

# the function for the 5-minute x11 blocks row
def makeRowX11(minutesString):
    startingYtall = topOfCircle + circleSize + spacerSize + sizeX
    # print(f'startingY is {startingYtall}')  # even more amateur debugging
    x1 = (width - rowWidth)/2
    x2 = x1 + sizeXtall
    y1 = startingYtall
    y2 = y1 + sizeYtall
    for i in range(11):
        # print(f'i is {i} and {(i+1)%3}')  # yep, that's right, more
        if (i+1)%3 == 0:
            color = lightRed
        else:
            color = grey
        if i + 1 <= int(minutesString) / 5:
            color = green
            if (i + 1) % 3 == 0:
                color = red
        # rint(f"cycle: {i} - x1={x1}, y1={y1}, x2={x2}, y2={y2}")  # and more, I even lost the 'p'
        myCanvas.create_rectangle(x1,y1,x2,y2, fill=color)
        x1 = x2 + spacerSizeTall
        x2 = x2 + spacerSizeTall + sizeXtall

# dumb name, but this redraws the clock and makes things go
def goGoGo():
    hoursString = int(strftime('%H'))    # This          Maybe in one call to strftime
    minuteString = int(strftime('%M'))   # can be
    secondsString = int(strftime('%S'))  # done better
    # print(f'hoursString: {hoursString}, minutesString: {minuteString}, secondsString: {secondsString}')
    drawCircle(secondsString)            # This block of code
    makeRowX4('hoursX5', hoursString)    # calls the functions
    makeRowX4('hoursX1', hoursString)    # for the hours and minutes
    makeRowX11(minuteString)             #
    makeRowX4('minX1', minuteString)     # the next part is the magic
    myCanvas.after(1000, goGoGo)         # the .after replaces sleep and does not block the mainloop

# blocking the mainloop would be bad. our buttons and other things would not work
# performance does not

goGoGo()
window.mainloop()