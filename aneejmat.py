import matplotlib.pyplot as plt
import math
import pylab as p
ang=(float(input("Enter angle: ")))*3.1415/180
ur=float(input("Enter velocity: "))
g=(float(input("Enter acceleration due to gravity: ")))*(-1)
uh=ur*math.cos(ang)
uv=ur*math.sin(ang)
h=(-1)*(uv**2)/(2*g)
time=(-2*uv)/g
x=[]
y=[]
t=0
while t <= time:
    x.append(uh*t)
    y.append((uv*t)+((g/2)*(t**2)))
    t=t+0.01
plt.plot(x,y)
p.axis('equal')
plt.show()