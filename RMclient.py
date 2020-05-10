from socket import *
from tkinter import *
import pickle
from functools import partial
import datetime





def askmenu():
    s= socket(AF_INET,SOCK_STREAM)
    s.connect((gethostname(),25258))
    s.send(bytes("menu","utf-8"))
    msg=s.recv(10).decode("utf-8")
    s.send(bytes("ok","utf-8"))
    msg1=s.recv(1024)
    s.send(bytes("ok","utf-8"))
    msg2=s.recv(1024)
    s.close()
    return pickle.loads(msg1),pickle.loads(msg2)

def sendOr(order):
    s= socket(AF_INET,SOCK_STREAM)
    s.connect((gethostname(),25258))
    s.send(bytes("order","utf-8"))
    s.recv(10)
    s.send(pickle.dumps(order))
    s.close()

def sendBill(billlist):
    s= socket(AF_INET,SOCK_STREAM)
    s.connect((gethostname(),25258))
    s.send(bytes("bill","utf-8"))
    s.recv(10)
    s.send(pickle.dumps(billlist))
    s.close()

menu=None
tax=None
menu,tax=askmenu()
tableNumber=""
#print(tax)

#table Name/Number prompt
w=Tk()
w.resizable(0,0)
w.title("Table Name/Number")
llflll=Label(w,text="Please give the\n  Table Name/Number  \n",font=("Helvetica",15,"bold"))
llflll.pack(fill=BOTH)
ennnnn=Entry(w,bd=4,width=20)
ennnnn.pack()
Label(w).pack()
def checkNsaveTN():
    global ennnnn, tableNumber,llflll,w
    sttttt=ennnnn.get()
    if(len(sttttt)>0):
        tableNumber=sttttt
        w.destroy()
    else:
        llflll.config(fg="red")

buuuut=Button(w,text="OK",width=10,anchor=CENTER,command=checkNsaveTN).pack(side=BOTTOM)

def forceCloseTN():
    raise SystemExit()

w.protocol("WM_DELETE_WINDOW",forceCloseTN)
w.mainloop()


window=Tk()
window.title("New Order! Table: "+tableNumber)
#window.geometry("420x180")
#window.pack_propagate(0)
window.resizable(0,0)
menuLabel=[]
menuFrame=[]
finish=None
f=None
menuList=[[menu[x][0],menu[x][1],0] for x in range(len(menu))]



def destroy_and_regain():
    global window, menuLabel, menuFrame, finish, menuList, menu, f
    window.destroy()
    menu,tax=askmenu()
    window=Tk()
    window.title("New Order! Table: "+tableNumber)
    #window.geometry("420x180")
    #window.pack_propagate(0)
    window.resizable(0,0)
    window.protocol("WM_DELETE_WINDOW",closingsend)
    menuLabel=[]
    menuFrame=[]
    finish=None
    f=None
    menuList=[[menu[x][0],menu[x][1],0] for x in range(len(menu))]
    #print(menuList)

def addItem(lis,lab):
    lis[2]+=1
    sendOr([lis[0],tableNumber])
    lab.config(text="x"+str(lis[2]))
def genB():
    global menuList,tax
    #print(menuList)
    now = str(datetime.datetime.now())
    #print(now)
    q=Tk()
    q.title("Bill Summary")
    q.resizable(0,0)
    Label(q,text="Item",font=("Helvetica" ,10,"bold"),width=20,anchor=W).grid(column=0,row=0)
    Label(q,text="Quantity",font=("Helvetica" ,10,"bold"),width=10,anchor=CENTER).grid(column=1,row=0)
    Label(q,text="Price",font=("Helvetica" ,10,"bold"),width=10,anchor=CENTER).grid(column=2,row=0)
    sum=0
    i=0
    for i in range(len(menuList)):
        Label(q,text=menuList[i][0],font=("Helvetica" ,10),width=20,anchor=W).grid(column=0,row=1+i)
        Label(q,text="x"+str(menuList[i][2]),font=("Helvetica" ,10),width=10,anchor=CENTER).grid(column=1,row=1+i)
        ee=menuList[i][1]*menuList[i][2]
        Label(q,text="₹"+str(ee),font=("Helvetica" ,10),width=10,anchor=CENTER).grid(column=2,row=1+i)
        sum+=ee
    Label(q,text="Total",width=20,font=("Helvetica" ,10,"bold"),anchor=W).grid(column=0,row=i+2)
    Label(q,text="₹"+str(sum),width=10,font=("Helvetica" ,10,"bold"),anchor=CENTER).grid(column=2,row=i+2)
    taxsum=0
    n=0
    for n,x in enumerate(tax,start=1):
        Label(q,text=x[0],font=("Helvetica" ,10),width=20,anchor=W).grid(column=0,row=i+2+n)
        Label(q,text=str(x[1])+"%",width=10,font=("Helvetica" ,10),anchor=CENTER).grid(column=2,row=i+2+n)
        taxsum+=x[1]
    Label(q,text="Final",width=20,font=("Helvetica" ,10,"bold"),anchor=W).grid(column=0,row=i+3+n)
    finalsum=sum*(taxsum/100+1)
    Label(q,text="₹"+str(finalsum),width=10,font=("Helvetica" ,10,"bold"),anchor=CENTER).grid(column=2,row=i+3+n)

    sendBill([tableNumber,menuList,sum,tax,finalsum,now])

    q.attributes('-topmost', True)
    q.update()
    destroy_and_regain()
    maker()
    window.update()
    q.attributes("-topmost",False)

def maker():
    global window, menuLabel, menuList, finish,f
    f=Frame(window)
    Label(f,text="Item Name",width=20,font=("Helvetica" ,10,"bold"),anchor=W).grid(column=0,row=0)
    Label(f,    text="Price",width=10,font=("Helvetica" ,10,"bold"),anchor=W).grid(column=1,row=0)
    Label(f, text="Quantity",width=10,font=("Helvetica" ,10,"bold"),anchor=W).grid(column=2,row=0)
    Label(f,    text="Order",width=10,font=("Helvetica" ,10,"bold"),anchor=CENTER).grid(column=3,row=0)
    f.pack(fill=BOTH)
    for i in menuList:
        y=Frame(window)
        menuFrame.append(y)
        x1=Label(y,    text=str(i[0]),width=20,font=("Helvetica" ,10),anchor=W)
        x2=Label(y,text="₹"+str(i[1]),width=10,font=("Helvetica" ,10),anchor=W)
        x3=Label(y,text="x"+str(i[2]),width=10,font=("Helvetica" ,10),anchor=W)
        x4=Button(y,       text="ADD",width=10,font=("times new roman" ,10),anchor=CENTER,command=partial(addItem,i,x3))
        menuLabel.append([x1,x2,x3,x4])
        x1.grid(column=0,row=0)
        x2.grid(column=1,row=0)
        x3.grid(column=2,row=0)
        x4.grid(column=3,row=0)

        y.pack(fill=BOTH)
    finish=Button(window, text="Finish. Generate Bill.",font=("times new roman" ,11),anchor=CENTER,command=genB)
    finish.pack(fill=BOTH)


maker()

def closingsend():
    if(sum([i[2] for i in menuList])>0):
        genB()
    window.destroy()
window.protocol("WM_DELETE_WINDOW",closingsend)

window.mainloop()