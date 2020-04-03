import tkinter as tk
import tkinter.ttk as ttk
window = tk.Tk()
window.title("Resturant Manager")
window.config(bg="#0000FF")

i=0
def do():
    global i
    i+=1
    
    ttk.Label(current,text=str(i)).pack()
    #current.create_window(0,0,window=tk.Label(current,text="2",bg="orange"))
menubar=tk.Menu(window)
fm=tk.Menu(menubar,tearoff=0)
fm.add_command(label="2")
fm.add_separator()
fm.add_command(label="exit",command=window.quit)
menubar.add_cascade(label="File",menu=fm)
menubar.add_cascade(label="Connections",command=window.quit)

window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)

mainframe=tk.Frame(window)
mainframe.grid(sticky=tk.N+tk.S+tk.E+tk.W)

mainframe.rowconfigure(0,weight=100)
mainframe.columnconfigure(0,weight=25)
billdesk=tk.Frame(mainframe)
billdesk.grid(column=0,row=0,rowspan=2,sticky=tk.N+tk.S+tk.E+tk.W)

def resizer(event):
    global curCan
    global curCanWin
    curCan.itemconfig(curCanWin,width=event.width)
    #curCan.itemconfig(curCanWin,height=event.height)
def scrSet(event):
    global curCan
    curCan.configure(scrollregion=curCan.bbox('all'))
mainframe.rowconfigure(0,weight=70)
mainframe.columnconfigure(1,weight=75)
curWin=tk.Frame(mainframe,bg="indigo")
curWin.grid(column=1,row=0,columnspan=2,sticky=tk.N+tk.S+tk.E+tk.W)
curCan=tk.Canvas(curWin,bg="pink")
current=ttk.Frame(curCan)
#curCan.bind("<Configure>",resizer)
#current.bind("<Configure>",scrSet)
#lab=tk.Label(text="2",bg="orange")
curCanWin= curCan.create_window(0,0,anchor='nw',window=current)
#curCan.configure(scrollregion=curCan.bbox("all"))
curScr=ttk.Scrollbar(curWin,orient='vertical',command=curCan.yview)
curCan.config(yscrollcommand = curScr.set,scrollregion=curCan.bbox('all'))
curScr.pack(fill=tk.Y,side=tk.RIGHT)
curCan.pack(fill=tk.BOTH,expand=True)
curCan.bind('<Configure>', scrSet)
current.bind("<Configure>",scrSet)
curCan.bind("<Configure>",resizer)

mainframe.rowconfigure(1,weight=30)
mainframe.columnconfigure(1,weight=38)
reserved=tk.Frame(mainframe)
reserved.grid(column=1,row=1,sticky=tk.N+tk.S+tk.E+tk.W)

mainframe.rowconfigure(1,weight=30)
mainframe.columnconfigure(2,weight=37)
empty=tk.Frame(mainframe)
empty.grid(column=2,row=1,sticky=tk.N+tk.S+tk.E+tk.W)

tk.Label(billdesk,text="1",bg="red").pack(fill=tk.BOTH,expand=True)
#tk.Label(curWin,text="2",bg="orange").pack(fill=tk.BOTH,expand=True)
#current.create_window(0,0,window=tk.Label(current,text="2",bg="orange"))
tk.Label(reserved,text="3",bg="green").pack(fill=tk.BOTH,expand=True)
tk.Button(empty,text="Push",bg="yellow",command=do).pack(fill=tk.BOTH,expand=True)

window.config(menu=menubar)
window.mainloop()
