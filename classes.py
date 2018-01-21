from tkinter import *

class  myButtons:
         
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
    
        self.click = Button(frame,text="Click",command=self.printit)
        self.click.pack(side=LEFT)
        
        self.quitButton = Button(frame,text="quit",command=frame.master.destroy)
        self.quitButton.pack(side=LEFT) 
        
        
    def printit(self):
        print("CLICKED")
   
        
root= Tk()
b = myButtons(root)
root.mainloop()