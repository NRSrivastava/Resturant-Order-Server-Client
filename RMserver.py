import tkinter
window = tkinter.Tk()
window.title("Resturant Manager")
window.config(bg="blue")
i=0
def do():
    global i
    i+=1
    tkinter.Label(current,text=str(i),bg="blue").pack(expand=0)
    #current.create_window(0,0,window=tkinter.Label(current,text="2",bg="orange"))
menubar=tkinter.Menu(window)
fm=tkinter.Menu(menubar,tearoff=0)
fm.add_command(label="2")
fm.add_separator()
fm.add_command(label="exit",command=window.quit)
menubar.add_cascade(label="File",menu=fm)
menubar.add_cascade(label="Connections",command=window.quit)

window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)

mainframe=tkinter.Frame(window)
mainframe.grid(sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

mainframe.rowconfigure(0,weight=100)
mainframe.columnconfigure(0,weight=25)
billdesk=tkinter.Frame(mainframe)
billdesk.grid(column=0,row=0,rowspan=2,sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

def resizer(event):
    global curCan
    global curCanWin
    curCan.itemconfig(curCanWin,width=event.width)
    #curCan.itemconfig(curCanWin,height=event.height)
def scrSet(event):
    global curCan
    #curCan.configure(scrollregion=curCan.bbox("all"))
mainframe.rowconfigure(0,weight=70)
mainframe.columnconfigure(1,weight=75)
curCan=tkinter.Canvas(mainframe,bg="pink")
current=tkinter.Frame(curCan,bg="black")
curCan.bind("<Configure>",resizer)
current.bind("<Configure>",scrSet)
#lab=tkinter.Label(text="2",bg="orange")
curCanWin= curCan.create_window(0,0,window=current,anchor=tkinter.NW)
curCan.grid(column=1,row=0,columnspan=2,sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)
curCan.configure(scrollregion=curCan.bbox("all"))
curScr=tkinter.Scrollbar(curCan,orient=tkinter.VERTICAL,command=curCan.yview)
#curCan.config(yscrollcommand = curScr.set)
curScr.pack(side=tkinter.RIGHT,fill=tkinter.Y)


mainframe.rowconfigure(1,weight=30)
mainframe.columnconfigure(1,weight=38)
reserved=tkinter.Frame(mainframe)
reserved.grid(column=1,row=1,sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

mainframe.rowconfigure(1,weight=30)
mainframe.columnconfigure(2,weight=37)
empty=tkinter.Frame(mainframe)
empty.grid(column=2,row=1,sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

tkinter.Label(billdesk,text="1",bg="red").pack(fill=tkinter.BOTH,expand=True)
tkinter.Label(current,text="2",bg="orange").pack(fill=tkinter.BOTH,expand=True)
#current.create_window(0,0,window=tkinter.Label(current,text="2",bg="orange"))
tkinter.Label(reserved,text="3",bg="green").pack(fill=tkinter.BOTH,expand=True)
tkinter.Button(empty,text="Push",bg="yellow",command=do).pack(fill=tkinter.BOTH,expand=True)

window.config(menu=menubar)
window.mainloop()
