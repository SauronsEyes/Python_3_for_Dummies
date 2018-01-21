from tkinter import *

root = Tk()

def nth():
    print("Suceessfully done nth")

menu = Menu(root,)
root.config(menu = menu,bg="#3f3f3f")

subMenu = Menu(menu,bg="#2f2f2f",fg="#ffffff")
menu.add_cascade(label="file" , menu=subMenu)
subMenu.add_command(label="New",command=nth)
subMenu.add_cascade(label="Open",command= nth)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=nth)

subMenu_2 = Menu(menu,bg="#2f2f2f",fg="#ffffff")
menu.add_cascade(label="Edit",menu=subMenu_2)
subMenu_2.add_command(label="Undo",command=nth)
subMenu_2.add_command(label="Redo",command=nth)

label_user = Label(root,text="Name",bg="#3f3f3f",fg="#ffffff")
label_pass = Label(root,text="Password",bg="#3f3f3f",fg="#ffffff")
entry_user = Entry(root)
entry_pass = Entry(root)
save_log = Checkbutton(root,text="Keep me logged in",bg="#3f3f3f",fg="#ffffff")

label_user.grid(row=0)
label_pass.grid(row=1,)
entry_user.grid(row=0,column=1)
entry_pass.grid(row=1,column=1)
save_log.grid(columnspan=2)

root.title("Login to Continue")
root.geometry('200x80')
root.resizable(width=False, height=False)
root.mainloop()