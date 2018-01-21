from tkinter import *

root = Tk()

root.title('Login')

label_user = Label(root,text="name")
label_pass = Label(root,text="password")
entry_user = Entry(root)
entry_pass = Entry(root)
save_log = Checkbutton(root,text="Keep me logged in")

label_user.grid(row=0,sticky=E)
label_pass.grid(row=1,sticky=E)
entry_user.grid(row=0,column=1)
entry_pass.grid(row=1,column=1)
save_log.grid(columnspan=2)

root.mainloop()
