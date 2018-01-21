from tkinter import *
import math


root = Tk()

canvas= Canvas(root,width =400,height=400)
canvas.pack()
canvas.create_line(20,30,100,100,fill='red')   
canvas.create_line(100,300,100,400)
for x in range(0,100):
    canvas.create_rectangle(x,x,x+10,x+20,fill='red') 
   
    

root.mainloop()