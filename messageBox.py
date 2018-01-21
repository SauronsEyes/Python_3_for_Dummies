from tkinter import *
import tkinter.messagebox as mbox

root = Tk()

mbox.showinfo('Warning','Missile Launch Detected')

decision = mbox.askquestion('Alert!!Decision Required!!','Do you want to activate the Anti-Missile Sys')
if(decision=='yes'):
    print('Anti Missile Sys Activated')
else:
    print('Meet your fate')

root.mainloop()