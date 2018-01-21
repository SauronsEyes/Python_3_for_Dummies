from tkinter import *
import math
import time


root = Tk()

init_speed = input('Initial Speed:')
project_ang = input('Projection Angle:')
str_gravity = input('Gravity:')

fl_gravity=float(str_gravity)
fl_speed=float(init_speed)
fl_angle=float(project_ang)

time=0.0
y=0.0
x=0.0
xa=0.0
ya=0.0

canvas = Canvas(root,width =900,height = 550)
canvas.pack()

canvas.create_line(0,300,900,300)

while(ya<0.1):
    time = time + 0.1
    xa = fl_speed * math.cos(fl_angle * (3.14 / 180.0)) * time
    ya = ((-fl_speed * math.sin(fl_angle * (3.14 / 180.0)) * time) + (0.5 * fl_gravity * (time ** 2)))
    canvas.create_line(x+10,y+300,xa+10,ya+300,fill='red')
    x=xa
    y=ya
        
root.mainloop()