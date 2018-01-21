from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()

button1 = Button(topFrame,text = "Button1",bg='#2f2f2f',fg = 'white')
button1.pack(side=RIGHT)
button2 = Button(topFrame,text = "Button1",bg='#2f2f2f',fg = 'white')
button2.pack(side=RIGHT)
button3 = Button(topFrame,text = "Button1",bg='#2f2f2f',fg = 'white')                 
button3.pack()

root.mainloop()
