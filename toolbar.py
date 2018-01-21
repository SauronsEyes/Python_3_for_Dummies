from tkinter import *

root = Tk()

menu = Menu(root)
root.config(menu = menu)

def nth():
    print("CLICKED")


#_________________________________Main Menu____________________________________
SubMenu = Menu(menu)
menu.add_cascade(label = 'File',menu=SubMenu)
SubMenu.add_command(label = 'New',command=nth )
SubMenu.add_command(label = 'Open',command=nth)
SubMenu.add_separator()
SubMenu.add_command(label = 'Exit',command=nth)


editMenu = Menu(menu)
menu.add_cascade(label = 'Edit',menu=editMenu)
editMenu.add_command(label = 'Undo',command=nth)
editMenu.add_command(label = 'Redo', command=nth)

#__________________________________Toolbar_____________________________________

toolbar = Frame(root,bg = 'blue')

insertButton = Button(toolbar,text = "Insert",command=nth)
insertButton.pack(side=LEFT,padx=2,pady=2)
printButton = Button(toolbar,text = 'Print',command=nth)
printButton.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)

#_________________________________Status Bar___________________________________

statusBar = Label(root,text="Loading.......",bd=1,relief=SUNKEN,anchor=W)
statusBar.pack(side=BOTTOM,fill =  X)


root.mainloop()