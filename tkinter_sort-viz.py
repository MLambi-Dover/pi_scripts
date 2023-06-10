#!/usr/bin/env python

import tkinter as tk
import random
from time import sleep


numberList = []  # we need a list to keep each row/value. rows will be the index and the y

canvasWidth = 800
canvasHeight= 800



# myCanvas.create_line(x1,y1,x2,y2, fill="green", width=5)
def makeList():
    global numberList
    for i in range(100):
        y1 = i
        y2 = y1
        x1 = 0
        x2 = random.randint(1, 800)
        numberList.append(x2)
        'line'+i = myCanvas.create_line(x1,y1,x2,y2, width=1)
    print('made a list')
    # print(numberList)
    return numberList

def makeLines():


def drawList():
    print('DRAWLIST')
    sleep(.1)
    myCanvas.delete('all')
    sleep(.1)
    for i in range(len(numberList)):
        y1 = i
        y2 = y1
        x1 = 0
        x2 = numberList[i]
        myCanvas.create_line(x1,y1,x2,y2, width=1)

def bubbleSort():
    global numberList
    print('got to bubbleSort')
    # print(f'numberList is {numberList}')

    n = len(numberList)
    for i in range(n):  # this iterates over the index / list-length
        print(f'Hi, i is {i}')
        for j in range(0, n-i-1):
            print(f'numList-J is {numberList[j]}, numList-J+1 is {numberList[j+1]}')
            if numberList[j] > numberList[j+1]:
                numberList[j], numberList[j+1] = numberList[j+1], numberList[j]
        sleep(1)
    
            
window = tk.Tk()

frameTop = tk.Frame(window, width=600, height=50, relief='sunken', border=1)
frameTop.pack()
frameBottom = tk.Frame(window, relief='sunken', border=1)
frameBottom.pack()

topLabel = tk.Label(frameTop, text='this would be the text').pack()
exitButton = tk.Button(frameTop, text='Exit', padx=15, pady=5, command=window.quit).pack(side=tk.LEFT)

sortButton = tk.Button(frameTop, text='sort', padx=15, pady=5, command=lambda: bubbleSort()).pack()

myCanvas = tk.Canvas(frameBottom, width=canvasWidth, height=canvasHeight)
myCanvas.pack()


makeList()
# print("Coordinates of line1 are: ", myCanvas.coords(line1))
# bubbleSort(numberList)

window.mainloop()