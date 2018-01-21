from tkinter import *
import math


color_values = ['red','blue','yellow','green','purple']
indexs= 0
root = Tk()
frame = Frame(root,bg='#3f3f3f')
frame.pack(side=TOP,fill=X)
canvas = Canvas(root,width=1300,height=800)
canvas.pack(side=BOTTOM,fill=X)

initial_speed = StringVar()
gravity_value = StringVar()
pro_ang = StringVar()

def start_projection():
    global indexs
    
    print(initial_speed.get())
    print(gravity_value.get())
    print(pro_ang.get())  
    fl_gravity=float(gravity_value.get())
    fl_speed=float(initial_speed.get())
    fl_angle=float(pro_ang.get())  
    time=0.0
    y=0.0
    x=0.0
    xa=0.0
    ya=0.0  
    canvas.create_line(0,500,1800,500)  

    while(ya<0.1):
        if(indexs>4):
            indexs=0
        time = time + 0.1
        xa = fl_speed * math.cos(fl_angle * (3.14 / 180.0)) * time
        ya = ((-fl_speed * math.sin(fl_angle * (3.14 / 180.0)) * time) + (0.5 * fl_gravity * (time ** 2)))
        canvas.create_line(x+10,y+500,xa+10,ya+500,fill=color_values[indexs])
        x=xa
        y=ya
        indexs=indexs+1

def scrn_clr():
    canvas.delete("all")
    
label_speed = Label(frame,text="Initial Speed:",bg='#3f3f3f',fg='white')
label_speed.pack(side=LEFT,padx=4,pady=4)    
init_speed = Entry(frame,textvariable=initial_speed)
init_speed.pack(side=LEFT,padx=4,pady=4)

label_ang= Label(frame,text="Projection Angle:",bg='#3f3f3f',fg='white')
label_ang.pack(side=LEFT,padx=4,pady=4)    
project_ang = Entry(frame,textvariable=pro_ang)
project_ang.pack(side=LEFT,padx=4,pady=4)

label_gravity= Label(frame,text="Gravity:",bg='#3f3f3f',fg='white')
label_gravity.pack(side=LEFT,padx=4,pady=4)    
gravity = Entry(frame,textvariable=gravity_value)
gravity.pack(side=LEFT,padx=4,pady=4)

launch = Button(frame,text = "Launch Projectile",command = start_projection)
launch.pack(side=LEFT,padx=30,pady=4)

clear_canvas = Button(frame,text="Clear",command=scrn_clr)
clear_canvas.pack(side=LEFT,padx=4,pady=4)
root.title('Path of Projectile')
root.mainloop()