from tkinter import *
root = Tk()

#________________________________________WAY-1_________________________________
def printname_1():
    print("Button Clicked")
button_event1 = Button(root,text="Click",command=printname_1)
button_event1.pack()

#________________________________________WAY-2_________________________________
def printname_2(event):
    print("Button Clicked-2")
button_event2 = Button(root, text="Click-2")
button_event2.bind('<Button-1>',printname_2)
button_event2.pack()




root.mainloop()