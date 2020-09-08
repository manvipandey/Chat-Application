from tkinter import *
from tkinter import ttk
import tkinter.font as font
import socket,_thread
import smtplib,ssl
hname=socket.gethostname()
host=socket.gethostbyname(hname)
host=""
nickname=""
addr=""
port=1234
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
class mail:
    def __init__(self):
        self.myfont = ("Arial",13)
        self.i=False
        self.b=False
        self.top=Tk()
        self.var=IntVar()
        self.var.set(13)
        self.top.title("EMAIL")
        #self.combostyle=ttk.Style()
        #self.combostyle.map('TCombobox',fieldbackground=[("readonly","black")])
        #self.combostyle.map('TCombobox',selectbackground=[("readonly","black")])
        #self.combostyle.map('TCombobox',selectforeground=[("readonly","white")])
        #self.top.configure(bg="")
        self.top.geometry("600x700")
        self.top.resizable(width=FALSE,height=FALSE)
        self.label1=Label(self.top,text="ENTER YOUR EMAIL ADDRESS : ",font=("Arial",10,"bold"))
        self.label2=Label(self.top,text="ENTER YOUR PASSWORD : ",font=("Arial",10,"bold"))
        self.label3=Label(self.top,text="ENTER RECIEPENTS EMAIL ADDRESS :",font=("Arial",10,"bold"))
        self.label4=Label(self.top,text="SUBJECT : ",font=("Arial",10,"bold"))
        self.label5=Label(self.top,text="TYPE YOUR MESSAGE : ",font=("Arial",10,"bold"))
        self.mess=Text(self.top,bd=0,bg="white",font=self.myfont,height=50,width=150)
        self.scrollbar=Scrollbar(self.top,command=self.mess.yview)
        self.mess["yscrollcommand"]=self.scrollbar.set
        self.entry1=Entry(self.top,font=("Arial",11,"bold"))
        self.entry2=Entry(self.top,show="*",font=("Arial",11,"bold"))
        self.entry3=Entry(self.top,font=("Arial",11,"bold"))
        self.entry4=Entry(self.top,font=("Arial",11,"bold"))
        self.button=Button(self.top,height="30",width="5",bg="black",fg="white",text="SEND MAIL",font=("Arial",15,"bold"),command=lambda:self.sendmail())
        self.b1=Button(self.top,height=15,width=5,bg="black",fg="white",text="I",font=("Arial",15,"italic"),command=lambda:self.italic())
        self.b2=Button(self.top,height=15,width=5,bg="black",fg="white",text="B",font=("Arial",15,"bold"),command=lambda:self.bold())
        self.b3=Button(self.top,height=12,width=10,bg="black",fg="white",text="APPLY",font=("Arial",10,"bold"),command=lambda:self.fontsize())
        self.combox=ttk.Combobox(self.top,state="readonly",values=["Arial","Times","Helvetica","Courier New",'Fixedsys',"Verdana","Comic Sans MS","MS Seriff"])
        self.combox.current(0)
        self.combox.bind("<<ComboboxSelected>>",self.combocall)
        self.fsize=Spinbox(self.top,from_=10,to=50,bg="black",fg="white",textvariable=self.var,font=("Arial",12,"bold"))
        #self.fsize.bind("<<Increment>>",self.fontsize)
        #self.fsize.bind("<<Decrement>>",self.fontsize)
        self.label1.place(x=50,y=40,height=50)
        self.label2.place(x=50,y=90,height=50)
        self.label3.place(x=50,y=140,height=50)
        self.label4.place(x=50,y=190,height=50)            
        self.label5.place(x=50,y=240,height=50)
        self.entry1.place(x=300,y=40,height=40,width=230)
        self.entry2.place(x=300,y=90,height=40,width=230)
        self.entry3.place(x=300,y=140,height=40,width=230)
        self.entry4.place(x=300,y=190,height=40,width=230)
        self.mess.place(x=210,y=240,height=350,width=370)
        self.button.place(x=210,y=650,height=45,width=150)
        self.b1.place(x=210,y=590,height=30,width=50)
        self.b2.place(x=265,y=590,height=30,width=50)
        self.b3.place(x=340,y=620,height=20,width=50)
        self.scrollbar.place(x=570,y=240,height=350)
        self.fsize.place(x=320,y=590,height=30,width=100)
        self.combox.place(x=425,y=590,height=30,width=105)
        self.top.mainloop()
    def sendmail(self):
        sender_email=self.entry1.get()
        sender_pass=self.entry2.get()
        recipent_email=self.entry3.get()
        subject=self.entry4.get()
        msg=self.mess.get("0.0",END)
        message="""\
        Subject: %s

        %s."""%(subject,msg)

        context=ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
            server.login(sender_email,sender_pass)
            server.sendmail(sender_email,recipent_email,message)
    def italic(self):
        if self.i==False:
            temp=list(self.myfont)
            temp.append("italic")
            self.myfont=tuple(temp)
            self.mess.config(font=self.myfont)
            self.i=True
        else:
            temp=list(self.myfont)
            temp.remove("italic")
            self.myfont=tuple(temp)
            self.mess.config(font=self.myfont)
            self.i=False
    def bold(self):
        if self.b==False:
            temp=list(self.myfont)
            temp.append("bold")
            self.myfont=tuple(temp)
            self.mess.config(font=self.myfont)
            self.b=True
        else:
            temp=list(self.myfont)
            temp.remove("bold")
            self.myfont=tuple(temp)
            self.mess.config(font=self.myfont)
            self.b=False
    def fontsize(self):
        font_size=self.fsize.get()
        temp=list(self.myfont)
        temp[1]=int(font_size)
        self.myfont=tuple(temp)
        self.mess.config(font=self.myfont)
        
    def combocall(self,event):
        font_style=self.combox.get()
        temp=list(self.myfont)
        temp[0]=font_style
        self.myfont=tuple(temp)
        self.mess.config(font=self.myfont)

def emailselect():
    m=mail()

def loadconninfo(chatlog,entrytext):
    if entrytext!="":
        chatlog.config(state=NORMAL)
        if chatlog.index('end')!=None:
            chatlog.insert(END,entrytext+"\n")
            chatlog.config(state=DISABLED)
            chatlog.yview(END)
def loadmyentry(chatlog,entrytext):
    if entrytext!="":
        chatlog.config(state=NORMAL)
        if chatlog.index('end')!=None:
            lineno=float(chatlog.index('end'))-1.0
            chatlog.insert(END,"YOU : "+entrytext)
            chatlog.tag_add("YOU",lineno,lineno+0.4)
            chatlog.tag_config("YOU",foreground="red",font=("Arial",13,"bold"))
            chatlog.config(state=DISABLED)
            chatlog.yview(END)
def loadotherentry(chatlog,entrytext,tag):
    if entrytext!="":
        chatlog.config(state=NORMAL)
        if chatlog.index('end')!=None:
            try:
                lineno=float(chatlog.index('end'))-1.0
            except:
                pass
            l=len(tag)/10
            chatlog.insert(END,entrytext)
            chatlog.tag_add(tag,lineno,lineno+l)
            chatlog.tag_config(tag,foreground="green",font=("Arial",13,"bold"))
            chatlog.config(state=DISABLED)
            chatlog.yview(END)
def recieveconn(server,name):
    global nickname
    global host
    host=server
    nickname=name
    try:
        name="@:"+nickname
        s.sendto(name.encode(),(host,port))
        #name=s.recv(1024)
        #server_name=name.decode()
        #chatlog.insert(END,"\n\n\n\n\t\t\t\t\tWELCOME {}".format(nickname))
        loadconninfo(chatlog,"\n SUCCESSFULLY CONNECTED TO {}\n------------------------------------------------------------------".format("SERVER"))
    except:
        loadconninfo(chatlog,"\n UNABLE TO CONNECT.....\n-----------------------------------------------------------------\n")
        return
    while 1:
        try:
            global addr
            data,addr=s.recvfrom(4096)
            data=data.decode()
        except:
            loadconninfo(chatlog,"\n [ YOUR PARTNER HAS DISCONNECTED ]\n")
            break
        if data!="":
            if data[1:4]=='>>>':
                loadconninfo(chatlog,data)
            else:
                i=data.find(":")
                name=data[:i]
                loadotherentry(chatlog,data,name)
        else:
            loadconninfo(chatlog,"\n [ YOUR PARTNER HAS DISCONNECTED ]\n")
            break
def clickaction():
    entrytext=filtermsg(entrybox.get("0.0",END))
    loadmyentry(chatlog,entrytext)
    chatlog.yview(END)
    entrybox.delete("0.0",END)
    entrytext=nickname+" : "+entrytext
    s.sendto(entrytext.encode(),addr)
def pressaction(event):
    entrybox.config(state=NORMAL)
    clickaction()
def disableentry(event):
    entrybox.config(state=DISABLED)
def filtermsg(entrytext):
    endfilter=''
    for i in range(len(entrytext)-1,-1,-1):
        if entrytext[i]!="\n":
            endfilter=entrytext[0:i+1]
            break
    for i in range(0,len(endfilter),1):
        if endfilter[i]!="\n":
            return endfilter[i:]+"\n"
    return ""
'''def connect():
    global host
    host=entry.get()
    top.destroy()
    #recieveconn(host)
    root.mainloop()'''
class top:
    def __init__(self):
        self.top=Tk()
        self.top.title("WELCOME TO THE CHAT ROOM")
        self.top.geometry("450x600")
        self.top.resizable(width=FALSE,height=FALSE)
        self.c=Canvas(self.top,bg="white",height=300,width=550)
        pic=PhotoImage(file="chatimg.png")
        self.img=self.c.create_image(450,0,anchor=NE,image=pic)
        self.c.pack()
        self.label=Label(self.top,text="ENTER THE HOST ADDRESS : ",font=("Arial",10,"bold"))
        self.label1=Label(self.top,text="CHOOSE A NICKNAME : ",font=("Arial",10,"bold"))
        self.entry=Entry(self.top,font=("Arial",12,"bold"))
        self.entry1=Entry(self.top,font=("Arial",12,"bold"))
        self.button=Button(self.top,height="30",width="5",bg="yellow",text="CONNECT",font=("Arial",15,"bold"),command=lambda:self.startchat())
        self.label.place(x=2,y=320,height=50)
        self.label1.place(x=2,y=380,height=50)
        self.entry.place(x=200,y=320,height=40,width=230)
        self.entry1.place(x=200,y=380,height=40,width=230)
        self.button.place(x=150,y=490,height=50,width=150)
        self.top.mainloop()
    def startchat(self):
        self.conn=self.entry.get()
        self.nickname=self.entry1.get()
        self.top.destroy()
top=top()
root=Tk()
root.title("CLIENT")
root.geometry("500x500")
root.resizable(width=FALSE, height=FALSE)
chatlog=Text(root,bd=0,bg="white",height=8,width=50,font="Arial")
chatlog.insert(END,"INITIALISING......")
chatlog.insert(END,"\nCONNECTING TO YOUR FRIEND...\n")
chatlog.config(state=DISABLED)
scrollbar=Scrollbar(root,command=chatlog.yview,cursor="heart")
chatlog["yscrollcommand"]=scrollbar.set
sendbutton=Button(root,font=("Arial",15,"bold"),text="SEND",width=10,height=3,bd=0,fg="white",bg="black",activebackground="#FACC2E",command=lambda:clickaction())
emailbutton=Button(root,font=("Arial",15,"bold"),width=10,text="EMAIL",height=3,bg="black",fg="white",command=lambda:emailselect())
entrybox=Text(root,bd=0,bg="white",width="29",height="5",font="Arial")
entrybox.bind("<Return>",disableentry)
entrybox.bind("<KeyRelease-Return>",pressaction)
emailbutton.place(x=6,y=450,height=40)
scrollbar.place(x=476,y=6,height=386)
chatlog.place(x=6,y=6,height=386,width=470)
entrybox.place(x=128,y=401,height=90,width=365)
sendbutton.place(x=6,y=401,height=45)
_thread.start_new_thread(recieveconn,(top.conn,top.nickname,))
root.mainloop()


    
    

