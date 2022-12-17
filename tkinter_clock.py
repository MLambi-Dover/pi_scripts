#!/usr/bin/env python

# an attempt at laying out a Berlin Uhr
# using tkinter, grids

# grid layout
# second pulsar
# 4 x5 hour boxes on top
# 4 hour boxes
# 11 x5 minutes boxes, every third red, or a different color
# 4 minute boxes

import tkinter as tk
from tkinter import ttk

from time import strftime, sleep

window = tk.Tk()
window.title("clock")
window.iconbitmap('e:/images/icons/saucer.ico')
#window.geometry("405x170")

frameTop = tk.Frame(window, relief='sunken', borderwidth=6)
frameBottom = tk.Frame(window)

frameTop.pack()
frameBottom.pack()

def time_now():
    time_string = strftime('%H:%M:%S %p')
    l1.config(text=time_string)
    # l1.after(1000, time_now) # time delay of 1000 milliseconds

my_font=('times',52,'bold')  # dislplay size and style
my_font2=('times',12,'bold')  # dislplay size and style

l1 = tk.Label(frameTop, font=my_font,bg='yellow')
l1.grid(row=0, column=1, rowspan=2)

# I called this here, once, when i first wrote this. its at the bottom
# time_now()
"""
secRow = tk.Label(window, bg='orange')
secRow.grid(row=0, pady=10, padx=5, columnspan=4)
hour5 = tk.Label(window, bg='red').grid(row=1, column=0)
hour10 = tk.Label(window, bg='blue').grid(row=1, column=1)
hour15 = tk.Label(window, bg='red').grid(row=1, column=2)
hour20 = tk.Label(window, bg='blue').grid(row=1, column=3)
"""


def changecolor(color):
    l1.configure(fg=color)
def changeBGcolor(color):
    l1.configure(bg=color)

# button = Button(root, text='Choose Color', command=changecolor).pack(pady=20)
# label = Label(root, text="Color", fg="black")


buttonL1 = ttk.Button(frameTop, text="L1", command=lambda: changecolor('blue'))
buttonL2 = ttk.Button(frameTop, text="L2", command=lambda: changecolor('brown'))
buttonR1 = ttk.Button(frameTop, text="R1", command=lambda: changeBGcolor("steel blue"))
buttonR2 = ttk.Button(frameTop, text="R2", command=lambda: changeBGcolor("goldenrod"))

buttonL1.grid(row=0, column=0)
buttonR1.grid(row=0, column=3)
buttonL2.grid(row=1, column=0)
buttonR2.grid(row=1, column=3)

exitButton = ttk.Button(frameTop, text="Exit", command=window.quit)
exitButton.grid(row=2, column=1, padx=50, pady=20)


# putting this in frame 2
l2 = tk.Label(frameBottom, font=my_font2,bd=2, bg='white', width=24)
l2.grid(row=0, column=0)

myCanvas = tk.Canvas(frameBottom, height=400, width=400, background="grey75")
myCanvas.grid(row=1, column=0)

color = 'grey'
sizeY = 25  # all of the rows should be the same height


def goGoGo():
    seconds = int(strftime('%S'))
    minutes = int(strftime('%M'))
    hours = int(strftime('%H'))
    if int(seconds) %2 == 0:
        color = 'yellow'
    else:
        color = 'grey'
    circleX = ((25*11)/2) +60
    circleY = 25
    myCanvas.create_oval(circleX-25, 25, circleX+25, 75, fill=color)
# 4 5-hour blocks
    for x in range(4):
        y=1
        color = 'grey'
        sizeX = (25*11)/4
        x1 = x*sizeX
        y1 = y*sizeY
        x2 = x1 + sizeX
        y2 = y1 + sizeY
        if x+1 <= int(hours)/5:
            color = 'green'
        myCanvas.create_rectangle((x1 +60, y1 +50, x2 +60, y2 + 50), fill=color)
# 4 1-hour blocks
    for x in range(4):
        y=1
        color = 'grey'
        sizeX = (25*11)/4
        x1 = x*sizeX
        y1 = y*sizeY
        x2 = x1 + sizeX
        y2 = y1 + sizeY
        if x+1 <= int(hours)%5:
            color = 'green'
        myCanvas.create_rectangle((x1 +60, y1 +75, x2 +60, y2 + 75), fill=color)

# minutes - 11 columns of 5 minutes every 3rd red
    for x in range(11):
        y=1
        sizeX = 25
        x1 = x*sizeX
        y1 = y*sizeY
        x2 = x1 + sizeX
        y2 = y1 + sizeY
        if (x+1)%3 == 0:
            color = 'red'
        else:
           color = 'grey'
        if x+1 < int(minutes)/5:
            color = 'green'
        myCanvas.create_rectangle((x1 +60, y1+100, x2 +60, y2+125), fill=color)
# one minute row - 4 sections bottom row
# def minuteSqares():
    for x in range(4):
        if x +1 <=int(minutes)%5:
            color='green'
        else:
            color='grey'
        y=1
        sizeX = (25*11)/4
        x1 = x*sizeX
        y1 = y*sizeY
        x2 = x1 + sizeX
        y2 = y1 + sizeY
        myCanvas.create_rectangle((x1 +60, y1 +150, x2 +60, y2 + 150), fill=color)
        # myCanvas.after(1000, goGoGo)


anotherExitButton = tk.Button(frameBottom, text="Exit Again", command=window.quit)

def startfunc():
    time_now()
    goGoGo()
    myCanvas.after(500, startfunc)

startfunc()
window.mainloop()
