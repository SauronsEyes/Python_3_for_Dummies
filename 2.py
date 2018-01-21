from tkinter import *
class Window(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master= master
        self.init_Window
        
    def init_Window(self):
        self.master.title("Hello")
        self.pack(fill=BOTH,expand=1)
        quitButton=Button(self,text="Quit")
        quitButton.place(x=0,y=0)
        
root = Tk()

root.geometry('400x300')
root.title('GUI')
quitButton = Button(root, text='Quit')
quitButton.pack()
quitButton.place(x=0, y=0)

app = Window(root)
root.mainloop()
