import tkinter as tk
from time import sleep

canvasHeight = 400
canvasWidth = 400


def moveTheLine():
    print('move the line')
    coOrds = myCanvas.coords(line1)
    y = int(coOrds[1]) + 10
    print(f'y is {y}')
    myCanvas.move(line1, 0, 10)
    """
    for i in range(10):
        print(i)
        myCanvas.move(line, 0, i*10)
        print('line1 coords are : ', line)
        sleep(1)
    """


window = tk.Tk()
myCanvas = tk.Canvas(window, width=canvasWidth, height=canvasHeight)


line1 = myCanvas.create_line(0,5, 250,5, width=5, fill='red')
line2 = myCanvas.create_line(0,50, 250,50, width=5, fill='blue')
myCanvas.pack()

exitButton = tk.Button(window, text='exit', padx=15, pady=5, command=quit).pack(side='left')
moveButton = tk.Button(window, text='move', padx=15, pady=5, command= moveTheLine).pack(side='left')

print("Coordinates of line1 are: ", myCanvas.coords(line1))



window.mainloop()