import tkinter as tk

#root window
window = tk.Tk()
window.title("Resturant Manager")
window.config(bg="#0000FF")

listlabel=[]
i=0
def add():
    global i, listlabel
    i+=1
    
    listlabel.append(tk.Label(current,text=str(i)))
    listlabel[-1].pack()
    #current.create_window(0,0,window=tk.Label(current,text="2",bg="orange"))
def remove():
    global i, listlabel
    i-=1
    listlabel[-1].destroy()
    listlabel.pop(-1)

#file menubar
menubar=tk.Menu(window)
fm=tk.Menu(menubar,tearoff=0)
fm.add_command(label="2")
fm.add_separator()
fm.add_command(label="exit",command=window.quit)
menubar.add_cascade(label="File",menu=fm)
menubar.add_cascade(label="Connections",command=window.quit)

#root window sizing configuration
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)

#root frame
mainframe=tk.Frame(window)
mainframe.grid(sticky=tk.N+tk.S+tk.E+tk.W)

#framing and resizing unit
def resizer(event,canvas,canvasWindow):
    canvas.itemconfig(canvasWindow,width=event.width)
def scrSet(event,canvas):
    canvas.configure(scrollregion=canvas.bbox('all'))

#billdesk
mainframe.rowconfigure(0,weight=100)#setting sizing weights
mainframe.columnconfigure(0,weight=25)#...^
billWin=tk.Frame(mainframe,bg="indigo")#billdesk window
billWin.grid(column=0,row=0,rowspan=2,sticky=tk.N+tk.S+tk.E+tk.W)#packing billdesk window
billCan=tk.Canvas(billWin,height=False,width=False,bg="pink")#billdesk canvas inside billdesk window
billdesk=tk.Frame(billCan)#billdesk frame inside canvas
billCanWin= billCan.create_window(0,0,anchor='nw',window=billdesk)#canvas' window formatting for billdesk frame
billScr=tk.Scrollbar(billWin,orient='vertical',command=billCan.yview)#scrollbar inside billdesk window
billScr=tk.Scrollbar(billWin,orient='vertical',command=billCan.yview)#scrollbar inside billdesk window
billCan.config(yscrollcommand = billScr.set)#setting scrollbar for canvas
billScr.pack(fill=tk.Y,side=tk.RIGHT)#packing scrollbar
billCan.pack(fill=tk.BOTH,expand=True)#packing billdesk canvas
billCan.bind('<Configure>', lambda event: scrSet(event,billCan))#resizing configuration
billdesk.bind("<Configure>",lambda event: scrSet(event,billCan))#...^
billCan.bind("<Configure>", lambda event: resizer(event,billCan,billCanWin))#...^

#current
mainframe.rowconfigure(0,weight=70)#setting sizing weights
mainframe.columnconfigure(1,weight=75)#...^
curWin=tk.Frame(mainframe,bg="indigo")#current window
curWin.grid(column=1,row=0,columnspan=2,sticky=tk.N+tk.S+tk.E+tk.W)#packing current window
curCan=tk.Canvas(curWin,height=False,width=False,bg="pink")#current canvas inside current window
current=tk.Frame(curCan)#current frame inside canvas
curCanWin= curCan.create_window(0,0,anchor='nw',window=current)#canvas' window formatting for current frame
curScr=tk.Scrollbar(curWin,orient='vertical',command=curCan.yview)#scrollbar inside current window
curCan.config(yscrollcommand = curScr.set)#setting scrollbar for canvas
curScr.pack(fill=tk.Y,side=tk.RIGHT)#packing scrollbar
curCan.pack(fill=tk.BOTH,expand=True)#packing current canvas
curCan.bind('<Configure>', lambda event: scrSet(event,curCan))#resizing configuration
current.bind("<Configure>",lambda event: scrSet(event,curCan))#...^
curCan.bind("<Configure>", lambda event: resizer(event,curCan,curCanWin))#...^

#reserved
mainframe.rowconfigure(1,weight=30)#setting sizing weights
mainframe.columnconfigure(1,weight=38)#...^
resWin=tk.Frame(mainframe,bg="indigo")#reserved window
resWin.grid(column=1,row=1,sticky=tk.N+tk.S+tk.E+tk.W)#packing reserved window
resCan=tk.Canvas(resWin,height=False,width=False,bg="pink")#reserved canvas inside reserved window
reserved=tk.Frame(resCan)#reserved frame inside canvas
resCanWin= resCan.create_window(0,0,anchor='nw',window=reserved)#canvas' window formatting for reserved frame
resScr=tk.Scrollbar(resWin,orient='vertical',command=resCan.yview)#scrollbar inside reserved window
resCan.config(yscrollcommand = resScr.set)#setting scrollbar for canvas
resScr.pack(fill=tk.Y,side=tk.RIGHT)#packing scrollbar
resCan.pack(fill=tk.BOTH,expand=True)#packing reserved canvas
resCan.bind('<Configure>', lambda event: scrSet(event,resCan))#resizing configuration
reserved.bind("<Configure>",lambda event: scrSet(event,resCan))#...^
resCan.bind("<Configure>", lambda event: resizer(event,resCan,resCanWin))#...^

#empty
mainframe.rowconfigure(1,weight=30)
mainframe.columnconfigure(2,weight=37)
empWin=tk.Frame(mainframe,bg="indigo")#empty window
empWin.grid(column=2,row=1,sticky=tk.N+tk.S+tk.E+tk.W)#packing empty window
empCan=tk.Canvas(empWin,height=False,width=False,bg="pink")#empty canvas inside empty window
empty=tk.Frame(empCan)#empty frame inside canvas
empCanWin= empCan.create_window(0,0,anchor='nw',window=empty)#canvas' window formatting for empty frame
empScr=tk.Scrollbar(empWin,orient='vertical',command=empCan.yview)#scrollbar inside empty window
empCan.config(yscrollcommand = empScr.set)#setting scrollbar for canvas
empScr.pack(fill=tk.Y,side=tk.RIGHT)#packing scrollbar
empCan.pack(fill=tk.BOTH,expand=True)#packing empty canvas
empCan.bind('<Configure>', lambda event: scrSet(event,empCan))#resizing configuration
empty.bind("<Configure>",lambda event: scrSet(event,empCan))#...^
empCan.bind("<Configure>", lambda event: resizer(event,empCan,empCanWin))#...^

#beta testing
tk.Label(billdesk,text="1",bg="red").pack(fill=tk.BOTH,expand=True)
#tk.Label(curWin,text="2",bg="orange").pack(fill=tk.BOTH,expand=True)
#current.create_window(0,0,window=tk.Label(current,text="2",bg="orange"))
#tk.Label(reserved,text="3",bg="green").pack(fill=tk.BOTH,expand=True)
tk.Button(reserved,text="Pull",bg="green",command=remove).pack(fill=tk.BOTH,expand=True)
tk.Button(empty,text="Push",bg="yellow",command=add).pack(fill=tk.BOTH,expand=True)

#root configuration
window.config(menu=menubar)
window.mainloop()
