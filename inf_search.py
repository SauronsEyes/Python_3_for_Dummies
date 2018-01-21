import urllib.request
from tkinter import *
import re

infData =''
root = Tk()
root.title = 'Wiki Search'
def perform_search():
    global infData
    fetch_status.configure(text = 'Query String:'+search.get())
    try:
        url='https://en.wikipedia.org/wiki/'+search.get()
        resp = urllib.request.urlopen(url)
        respData = resp.read()
        infData = re.findall(r'<p>(.*?)</p>',str(respData))
        file_name =  search.get()+'.html'
        html_gen = open(file_name,'w')
        for eachP in infData:
            html_gen.write(eachP)
        html_gen.close
        fetch_status.configure(text = '''Information fetching success.
                 Check the html file to see the inf''')
        
    except Exception as e:
        fetch_status.configure(text = str(e))    

search = StringVar()
frame = Frame(root,bg='#3f3f3f')
frame.pack(fill=X,side=TOP)
inf_disp = Frame(root)
inf_disp.pack(fill=Y,side=BOTTOM)
fetch_status = Label(inf_disp,text=infData)
fetch_status.pack(side=TOP)



search_label = Label(frame,text='Search Query:',bg='#3f3f3f',fg='#ffffff')
search_label.pack(side=LEFT,padx=4,pady=4)
searchBar = Entry(frame,textvariable=search)
searchBar.pack(side=LEFT,padx=4,pady=4)
search_button = Button(frame,text="Search",command=perform_search)
search_button.pack(side=LEFT,padx=10,pady=4)



root.mainloop()