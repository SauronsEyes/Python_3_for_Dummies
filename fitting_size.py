from tkinter import *

root = Tk()

label1 = Label(root,text="File",fg='white',bg='#3f3f3f')
label2 = Label(root,text="File",fg='white',bg='#3f3f3f')
label3 = Label(root,text="File",fg='white',bg='#3f3f3f')
label1.pack()
label2.pack(fill=X)
label3.pack(side=LEFT,fill=Y)             

root.mainloop()
