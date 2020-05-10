import threading
from socket import *
import tkinter as tk
import datetime
import pickle
import sys
from functools import partial

menu=[["Fries Meal",50],["Lunch",250],["Burger Meal",100],["Pizza",200],["Cheese Burger",150],["Drinks",50]]
tax=[["CGST",9],["SGST",9]]
bdlist=[]
culist=[]
relist=[]
emlist=[]



def main():
    global menu,tax,window,billdesk,current,reserved,empty
    s=socket(AF_INET,SOCK_STREAM)
    s.bind((gethostname(),25258))
    s.listen(5)

    def popit(fr):
        fr.destroy()
    def mtp(n,t,fr):
        fr.destroy()
        frr=tk.Frame(reserved, borderwidth=2, relief="ridge")
        ll1=tk.Label(frr,text=n).pack(side=tk.LEFT)
        ll4=tk.Button(frr,text="WaitList",width=8,command=partial(mtw,n,t,frr)).pack(side=tk.RIGHT)
        ll3=tk.Button(frr,text="Done!",width=8,command=partial(popit,frr)).pack(side=tk.RIGHT)
        ll2=tk.Label(frr,text="Table: "+t).pack(side=tk.RIGHT)
        frr.pack(fill=tk.X)
    def mtw(n,t,fr):
        fr.destroy()
        frr=tk.Frame(empty, borderwidth=2, relief="ridge")
        ll1=tk.Label(frr,text=n).pack(side=tk.LEFT)
        ll4=tk.Button(frr,text="Cancel",width=7,command=partial(popit,frr)).pack(side=tk.RIGHT)
        ll3=tk.Button(frr,text="Prepare",width=7,command=partial(mtp,n,t,frr)).pack(side=tk.RIGHT)
        ll2=tk.Label(frr,text="Table: "+t).pack(side=tk.RIGHT)
        frr.pack(fill=tk.X)
    def mtc(n,t):
        frr=tk.Frame(current, borderwidth=2, relief="ridge")
        ll1=tk.Label(frr,text=n).pack(side=tk.LEFT)
        ll4=tk.Button(frr,text="WaitList",width=20,command=partial(mtw,n,t,frr)).pack(side=tk.RIGHT)
        ll3=tk.Button(frr,text="Prepare",width=20,command=partial(mtp,n,t,frr)).pack(side=tk.RIGHT)
        ll2=tk.Label(frr,text="Table: "+t).pack(side=tk.RIGHT)
        frr.pack(fill=tk.X)
    def mtb(bL):
        frr=tk.Frame(billdesk, borderwidth=2, relief="ridge")
        ll1=tk.Label(frr,text="Table: "+bL[0]+"\n"+str(bL[5])).pack(side=tk.TOP)
        ll4=tk.Button(frr,text="Delete",width=6,command=partial(popit,frr)).pack(side=tk.LEFT)
        ll3=tk.Button(frr,text="View",width=6,command=partial(viewBill,bL)).pack(side=tk.RIGHT)
        #ll2=tk.Label(frr,text=str(s)).pack(side=tk.RIGHT)
        frr.pack(fill=tk.X)
    def viewBill(bL):
        menuList=bL[1]
        sum=bL[2]
        tax=bL[3]
        finalsum=bL[4]
        q=tk.Tk()
        q.title("View Bill")
        q.resizable(0,0)
        tk.Label(q,text="Table: "+bL[0],font=("Helvetica" ,10,"bold")).grid(column=0,columnspan=3,row=0)
        tk.Label(q,text="Date & Time: "+bL[5],font=("Helvetica" ,10,"bold")).grid(column=0,columnspan=3,row=1)
        tk.Label(q,text="Item",font=("Helvetica" ,10,"bold"),width=15,anchor=tk.W).grid(column=0,row=2)
        tk.Label(q,text="Quantity",font=("Helvetica" ,10,"bold"),width=10,anchor=tk.CENTER).grid(column=1,row=2)
        tk.Label(q,text="Price",font=("Helvetica" ,10,"bold"),width=10,anchor=tk.CENTER).grid(column=2,row=2)
        i=0
        for i in range(len(menuList)):
            tk.Label(q,text=menuList[i][0],font=("Helvetica" ,10),width=15,anchor=tk.W).grid(column=0,row=3+i)
            tk.Label(q,text="x"+str(menuList[i][2]),font=("Helvetica" ,10),width=10,anchor=tk.CENTER).grid(column=1,row=3+i)
            tk.Label(q,text="₹"+str(menuList[i][1]*menuList[i][2]),font=("Helvetica" ,10),width=10,anchor=tk.CENTER).grid(column=2,row=3+i)
        tk.Label(q,text="Total",width=15,font=("Helvetica" ,10,"bold"),anchor=tk.W).grid(column=0,row=i+4)
        tk.Label(q,text="₹"+str(sum),width=10,font=("Helvetica" ,10,"bold"),anchor=tk.CENTER).grid(column=2,row=i+4)
        n=0
        for n,x in enumerate(tax,start=1):
            tk.Label(q,text=x[0],font=("Helvetica" ,10),width=15,anchor=tk.W).grid(column=0,row=i+4+n)
            tk.Label(q,text=str(x[1])+"%",width=10,font=("Helvetica" ,10),anchor=tk.CENTER).grid(column=2,row=i+4+n)
        tk.Label(q,text="Final",width=15,font=("Helvetica" ,10,"bold"),anchor=tk.W).grid(column=0,row=i+5+n)
        tk.Label(q,text="₹"+str(finalsum),width=10,font=("Helvetica" ,10,"bold"),anchor=tk.CENTER).grid(column=2,row=i+5+n)
    
    while True:
        
        clientsocket,address=s.accept()
        m=clientsocket.recv(10).decode("utf-8")
        if(m=="menu"):
            clientsocket.send(bytes("ok","utf-8"))
            clientsocket.recv(10)
            clientsocket.send(pickle.dumps(menu))
            clientsocket.recv(10)
            clientsocket.send(pickle.dumps(tax))
        elif(m=="order"):
            clientsocket.send(bytes("ok","utf-8"))
            msg=clientsocket.recv(1024)
            order=pickle.loads(msg)
            mtc(order[0],order[1])
            print(order)
        elif(m=="bill"):
            clientsocket.send(bytes("ok","utf-8"))
            msg=clientsocket.recv(1024)
            blist=pickle.loads(msg)
            mtb(blist)
            for i in blist:
                print(i)

        #break




#window=billdesk=current=reserved=empty=None
#def GUI():

#global window

#root window
window = tk.Tk()
window.title("Resturant Manager")
window.config(bg="#0000FF")
window.minsize(800,400)

#beta testing
"""
listlabel=[]
i=0
def add():
    #nonlocal i, listlabel
    global i, listlabel
    i+=1
    
    listlabel.append(tk.Label(current,text=str(i)))
    listlabel[-1].pack()
    #current.create_window(0,0,window=tk.Label(current,text="2",bg="orange"))
def remove():
    #nonlocal i, listlabel
    global i,listlabel
    i-=1
    listlabel[-1].destroy()
    listlabel.pop(-1)"""

#file menubar
"""
menubar=tk.Menu(window)
fm=tk.Menu(menubar,tearoff=0)
fm.add_command(label="2")
fm.add_separator()
fm.add_command(label="exit",command=window.quit)
menubar.add_cascade(label="File",menu=fm)
menubar.add_cascade(label="Connections",command=window.quit)"""

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
#global billdesk
mainframe.rowconfigure(0,weight=100)#setting sizing weights
mainframe.columnconfigure(0,weight=25)#...^
billWin=tk.Frame(mainframe,bg="indigo")#billdesk window
billWin.grid(column=0,row=0,rowspan=2,sticky=tk.N+tk.S+tk.E+tk.W)#packing billdesk window
tk.Label(billWin,text="Bills",font=("Helvetica",15,"bold"),anchor=tk.CENTER, borderwidth=2, relief="ridge",bg="#ABD1C9").pack(fill=tk.BOTH)
billCan=tk.Canvas(billWin,height=False,width=False,bg="#DFDCE5")#billdesk canvas inside billdesk window
billdesk=tk.Frame(billCan,bg="#DFDCE5")#billdesk frame inside canvas
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
#global current
mainframe.rowconfigure(0,weight=70)#setting sizing weights
mainframe.columnconfigure(1,weight=75)#...^
curWin=tk.Frame(mainframe,bg="indigo")#current window
curWin.grid(column=1,row=0,columnspan=2,sticky=tk.N+tk.S+tk.E+tk.W)#packing current window
tk.Label(curWin,text="Current Orders",font=("Helvetica",15,"bold"),anchor=tk.CENTER, borderwidth=2, relief="ridge",bg="#DBB04A").pack(fill=tk.BOTH)
curCan=tk.Canvas(curWin,height=False,width=False,bg="#DFDCE5")#current canvas inside current window
current=tk.Frame(curCan,bg="#DFDCE5")#current frame inside canvas
curCanWin= curCan.create_window(0,0,anchor='nw',window=current)#canvas' window formatting for current frame
curScr=tk.Scrollbar(curWin,orient='vertical',command=curCan.yview)#scrollbar inside current window
curCan.config(yscrollcommand = curScr.set)#setting scrollbar for canvas
curScr.pack(fill=tk.Y,side=tk.RIGHT)#packing scrollbar
curCan.pack(fill=tk.BOTH,expand=True)#packing current canvas
curCan.bind('<Configure>', lambda event: scrSet(event,curCan))#resizing configuration
current.bind("<Configure>",lambda event: scrSet(event,curCan))#...^
curCan.bind("<Configure>", lambda event: resizer(event,curCan,curCanWin))#...^

#reserved
#global reserved
mainframe.rowconfigure(1,weight=30)#setting sizing weights
mainframe.columnconfigure(1,weight=38)#...^
resWin=tk.Frame(mainframe,bg="indigo")#reserved window
resWin.grid(column=1,row=1,sticky=tk.N+tk.S+tk.E+tk.W)#packing reserved window
tk.Label(resWin,text="Preparing",font=("Helvetica",15,"bold"),anchor=tk.CENTER, borderwidth=2, relief="ridge",bg="#97B3D0").pack(fill=tk.BOTH)
resCan=tk.Canvas(resWin,height=False,width=False,bg="#DFDCE5")#reserved canvas inside reserved window
reserved=tk.Frame(resCan,bg="#DFDCE5")#reserved frame inside canvas
resCanWin= resCan.create_window(0,0,anchor='nw',window=reserved)#canvas' window formatting for reserved frame
resScr=tk.Scrollbar(resWin,orient='vertical',command=resCan.yview)#scrollbar inside reserved window
resCan.config(yscrollcommand = resScr.set)#setting scrollbar for canvas
resScr.pack(fill=tk.Y,side=tk.RIGHT)#packing scrollbar
resCan.pack(fill=tk.BOTH,expand=True)#packing reserved canvas
resCan.bind('<Configure>', lambda event: scrSet(event,resCan))#resizing configuration
reserved.bind("<Configure>",lambda event: scrSet(event,resCan))#...^
resCan.bind("<Configure>", lambda event: resizer(event,resCan,resCanWin))#...^

#empty
global empty
mainframe.rowconfigure(1,weight=30)
mainframe.columnconfigure(2,weight=37)
empWin=tk.Frame(mainframe,bg="indigo")#empty window
empWin.grid(column=2,row=1,sticky=tk.N+tk.S+tk.E+tk.W)#packing empty window
tk.Label(empWin,text="WaitList",font=("Helvetica",15,"bold"),anchor=tk.CENTER, borderwidth=2, relief="ridge",bg="#97B3D0").pack(fill=tk.BOTH)
empCan=tk.Canvas(empWin,height=False,width=False,bg="#DFDCE5")#empty canvas inside empty window
empty=tk.Frame(empCan,bg="#DFDCE5")#empty frame inside canvas
empCanWin= empCan.create_window(0,0,anchor='nw',window=empty)#canvas' window formatting for empty frame
empScr=tk.Scrollbar(empWin,orient='vertical',command=empCan.yview)#scrollbar inside empty window
empCan.config(yscrollcommand = empScr.set)#setting scrollbar for canvas
empScr.pack(fill=tk.Y,side=tk.RIGHT)#packing scrollbar
empCan.pack(fill=tk.BOTH,expand=True)#packing empty canvas
empCan.bind('<Configure>', lambda event: scrSet(event,empCan))#resizing configuration
empty.bind("<Configure>",lambda event: scrSet(event,empCan))#...^
empCan.bind("<Configure>", lambda event: resizer(event,empCan,empCanWin))#...^

#beta testing
#tk.Label(billdesk,text="1",bg="red").pack(fill=tk.BOTH,expand=True)
#tk.Label(curWin,text="2",bg="orange").pack(fill=tk.BOTH,expand=True)
#current.create_window(0,0,window=tk.Label(current,text="2",bg="orange"))
#tk.Label(reserved,text="3",bg="green").pack(fill=tk.BOTH,expand=True)
#tk.Button(reserved,text="Pull",bg="green",command=remove).pack(fill=tk.BOTH,expand=True)
#tk.Button(empty,text="Push",bg="yellow",command=add).pack(fill=tk.BOTH,expand=True)

#root
#window.config(menu=menubar)

t2=threading.Thread(target=main)
t2.setDaemon(True)
t2.start()



window.mainloop()




#t1=threading.Thread(target=GUI)

#t1.start()
