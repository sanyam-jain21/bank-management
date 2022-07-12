from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import os
#import mysql.connector


root = Tk()

root.title("Bank Management System")
root.state("zoomed")
root.geometry("1920x1080")
state1='disabled'
state2="disabled"
state3='normal'


num=0


#Creating Directory for database
path=os.environ["userprofile"]
try:
    os.mkdir(path+"\\Documents\\bank managment")
except FileExistsError:
    pass

con = sqlite3.connect(path+"\\Documents\\bank managment\mydatabase.db")
#con=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="bankmanagmentsystem")
cur = con.cursor()

#Creating Tables
con.execute("create table if not exists accountdetail   (account_no int NOT NULL PRIMARY KEY,name varchar(30),password varchar(30));")

######################################################################################################################################################
def gettingDetails():
    
    Id = ent1.get()
    name = ent2.get()
    password = ent3.get()
    try:
            if (type(int(Id)) == int):
                pass
            else:
                messagebox.showinfo("Invalid Value","Unique ID should be an integer")
                return
    except:
            messagebox.showinfo("Invalid Value","Unique ID should be an integer")
            return
        
    
    sql = "insert into accountdetail values ('"+Id+"','"+name+"','"+password+"')"
    try:
            cur.execute(sql)
            con.commit()
            sql2="create table if not exists "+name+"   (account_no int, action varchar(30),amount varchar(30));"
            cur.execute(sql2)
            messagebox.showinfo("Success", "Successfully registered")

    except:
            messagebox.showinfo("Error inserting","Cannot add data to Database")
            
  
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
#########################################################################################################################################################
def gettingLoginDetails():

    global role,state1,state2,state3,btn1,btn2,btn3,btn4,btn5,btn6,state2,Id ,name,password

    
    Id = ent1.get()
    name = ent2.get()
    password = ent3.get()
    
    try :
        sql="select * from accountdetail ;"
        cur.execute(sql)
        record=cur.fetchall()
        for i in record:
            if int(Id)==i[0] and name==i[1] and password==i[2]:
                messagebox.showinfo("SUCCESS","You have successfully logged in")
                btn1.destroy()
                btn2.destroy()
                btn3.destroy()
                btn4.destroy()
                btn5.destroy()
                btn6.destroy()
                
                state1='normal'
                state2='normal'
                state3='disabled'
                Menu()
                break
                
        else:
                messagebox.showerror("Failure","Can't log in, check your credentials")
    except:
            messagebox.showinfo("FAILED","Please check your credentials")
            
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)

    
######################################################################################################################################################
def destroys():
    global num

    if num==1:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        lb4.destroy()
        en3.destroy()
        en4.destroy()
        SubmitBtn.destroy()

    elif num==2:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        SubmitBtn.destroy()

    elif num==3:
        lb.destroy()
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        en3.destroy()
        transferBtn.destroy()

    elif num==4:
        scroll_y.destroy()
    #    issue_table.destroy()

    elif num==6:
        lb1.destroy()
        en1.destroy()
        lb2.destroy()
        en2.destroy()
        lb3.destroy()
        lb4.destroy()
        en3.destroy()
        en4.destroy()
        headingLabel.destroy()
        SearchBtn.destroy()

    elif num==7 or num==8:
        scroll_y.destroy()
        account_table.destroy()

    else:
        pass



def logout():
    global num,state1,state2,state3

    destroys()

    state1="disabled"
    state2="disabled"
    state3="normal"
    Menu()
    messagebox.showinfo("Logged out", "You have Successfully logged out")

def Menu():

    global state1,state2,state3,btn1,btn2,btn3,btn4,btn5,btn6,photoimage1, photoimage2, photoimage3, photoimage4, photoimage5, photoimage6
    
    photo1 = PhotoImage(file =r".icons\deposit.png")
    photoimage1 = photo1.subsample(9,9)
    btn1 = Button(moduleFrame,text="    Deposit",font=("arial",14,'bold'),image=photoimage1,compound = LEFT, command=deposits, state=state1)
    btn1.place(relx=0,rely=0.17, relwidth=1,relheight=0.12)
    
    photo2 = PhotoImage(file =r"icons\withdraw.png")
    photoimage2 = photo2.subsample(8,8)
    btn2 = Button(moduleFrame,text="    Withdraw",font=("arial",14,'bold'),image=photoimage2, compound= LEFT, command=withdraws,state=state1)
    btn2.place(relx=0,rely=0.31, relwidth=1,relheight=0.12)
    
    photo3 = PhotoImage(file =r"icons\passbook.png")
    photoimage3 = photo3.subsample(9,9)
    btn3 = Button(moduleFrame,text="    Passbook",font=("arial",14,'bold'),image=photoimage3, compound= LEFT, command=passbooks,state=state1)
    btn3.place(relx=0, rely=0.44, relwidth=1,relheight=0.12)
    
    photo4 = PhotoImage(file =r"icons\changepin.png")
    photoimage4 = photo4.subsample(4,4)
    btn4 = Button(moduleFrame,text="Change Account Details",font=("arial",10,'bold'),image=photoimage4, compound= LEFT, command=changepin,state=state1)
    btn4.place(relx=0,rely=0.58, relwidth=1,relheight=0.12)
    
    photo5 = PhotoImage(file =r"icons\transaction.png")
    photoimage5 = photo5.subsample(15,15)
    btn5 = Button(moduleFrame,text="    Transaction",font=("arial",14,'bold'),image=photoimage5, compound = LEFT, command = Transactions,state=state1)
    btn5.place(relx=0,rely=0.72, relwidth=1,relheight=0.12)
    
    photo6 = PhotoImage(file =r"icons\exit.png")
    photoimage6 = photo6.subsample(2,2)
    btn6 = Button(moduleFrame, text="    Exit",font=("arial",14,'bold'), image=photoimage6, compound = LEFT, command=root.destroy)
    btn6.place(relx=0,rely=0.86, relwidth=1,relheight=0.12)

    loginBtn = Button(headingFrame,text="LOGIN", font=("arial",10,'bold'),state=state3,command=gettingLoginDetails)
    loginBtn.place(relx=0.87,rely=0.4, relwidth=0.1)

    regBtn=Button(headingFrame,text="REGISTER", font=("arial",10,'bold'),state=state3,command=gettingDetails)
    regBtn.place(relx=0.87,rely=0.1, relwidth=0.1)

    logoutBtn=Button(headingFrame, text="LOGOUT", font=('arial',10,'bold'),  state=state2,command=logout)
    logoutBtn.place(relx=0.87, rely=0.7, relwidth=0.1)

def deposits(): 
    
    global en1,en2,en3,en4,lb1,lb2,lb3,lb4,SubmitBtn,lb,num,Id,name,password

    destroys()

    lb=Label(displayFrame,text='Account Details',font=("Times New Roman",26,'bold'),bg='white')
    lb.place(relx=0.34,rely=0)

    # Account no. 
    lb1 = Label(displayFrame,text="Account No : ",font=("arial",14,'bold'),bg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    en1 = Label(displayFrame,text=Id,font=("arial",14,'bold'),bg='#FFDFA4')
    en1.place(relx=0.3,rely=0.2, relwidth=0.62)
        
    # Account password
    lb2 = Label(displayFrame,text="Account password",font=("arial",14,'bold'),bg='white')
    lb2.place(relx=0.03,rely=0.35)
        
    en2 = Label(displayFrame,text=password,font=("arial",14,'bold'),bg='#FFDFA4')
    en2.place(relx=0.3,rely=0.35, relwidth=0.62)
        
    # Owner Name
    lb3 = Label(displayFrame,text="Owner Name:",font=("arial",14,'bold'),bg='white')
    lb3.place(relx=0.07,rely=0.5)
        
    en3 = Label(displayFrame,text=name, font=("arial",14,'bold'), bg='#FFDFA4')
    en3.place(relx=0.3,rely=0.5, relwidth=0.62)
        
    # deposit Amount 
    lb4 = Label(displayFrame,text="deposit Amount : ",font=("arial",14,'bold'),bg='white')
    lb4.place(relx=0.05,rely=0.65)
        
    en4 = Entry(displayFrame,font=("arial",14,'bold'), bg='#FFDFA4')
    en4.place(relx=0.3,rely=0.65, relwidth=0.62)
   
    #Submit Button
    SubmitBtn = Button(displayFrame,text="Deposit",font=("arial",12,'bold'),bg='white',command=addamount)
    SubmitBtn.place(relx=0.65,rely=0.8, relwidth=0.18,relheight=0.08)

    num=1
def addamount():
    global name,Id
    add=en4.get()
    x="insert into "+name+" values (%s,'deposit',%s)"%(Id,add)
    cur.execute(x)
    con.commit()

def withdraws(): 
    
    global en1, lb1,lb2,en2, SubmitBtn,lb,num,Id

    destroys()
    # Withdraw
    lb = Label(displayFrame,text='Withdraw',font=("Times New Roman",26,'bold'),bg='white')
    lb.place(relx=0.37,rely=0)

    # Account No 
    lb1 = Label(displayFrame,text="Account No : ",font=("arial",14,'bold'),bg='white')
    lb1.place(relx=0.05,rely=0.2)

    en1 = Label(displayFrame,text=Id,font=("arial",14,'bold'),bg='#FFDFA4')
    en1.place(relx=0.3,rely=0.2, relwidth=0.62)   
    
    # Withdraw Amount 
    lb2 = Label(displayFrame,text="Withdraw Amount :",font=("arial",12,'bold'), bg='white')
    lb2.place(relx=0.05,rely=0.45)
        
    en2 = Entry(displayFrame,font=("arial",12,'bold'),bg='#FFDFA4')
    en2.place(relx=0.3,rely=0.45, relwidth=0.62)
    
    # WITHDRAW Button
    SubmitBtn = Button(displayFrame,text="WITHDRAW", font=("arial",12,'bold'),bg='white',command=subamount)
    SubmitBtn.place(relx=0.6,rely=0.65, relwidth=0.18,relheight=0.08)

    num=2

def subamount():
    global name,Id
    sub=en2.get()
    x="insert into "+name+" values (%s,'Withdraw',%s)"%(Id,sub)
    cur.execute(x)
    con.commit()

def Transactions(): 
    
    global en1,en2,en3,transferBtn,lb1,lb2,lb3,en1,en2,en3,lb,num

    destroys()
    # Transaction
    lb = Label(displayFrame,text="Transaction", font=('Times New Roman',26,'bold'), bg='white')
    lb.place(relx=0.27,rely=0)
    # Account no 
    lb1 = Label(displayFrame,text="Account no : ",font=('arial', 12,'bold'), bg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    en1 = Entry(displayFrame,font=('arial', 12,'bold'),bg='#FFDFA4')
    en1.place(relx=0.35,rely=0.2, relwidth=0.55)
    
    # Transfer Money 
    lb2 = Label(displayFrame,text="Transfer Money to \n account no : ",font=('arial', 12,'bold'),bg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    en2 = Entry(displayFrame,font=('arial', 12,'bold'),bg='#FFDFA4')
    en2.place(relx=0.35,rely=0.4, relwidth=0.55)
    
    # Amount to be transfer
    lb3 = Label(displayFrame,text="Amount to be transfer : ",font=('arial', 12,'bold'), bg='white')
    lb3.place(relx=0.05,rely=0.6)
        
    en3 = Entry(displayFrame,font=('arial', 12,'bold'),bg='#FFDFA4')
    en3.place(relx=0.35,rely=0.6, relwidth=0.55)
    
    # Transfer Button
    transferBtn = Button(displayFrame,text="Transfer",bg='white',font=("arial",12,'bold'), command=transferamount)
    transferBtn.place(relx=0.7,rely=0.75, relwidth=0.18,relheight=0.08)


    num=3

def transferamount():
    global name,Id
    transfer=en3.get()
    x="insert into "+name+" values (%s,'transfer',%s)"%(Id,transfer)
    cur.execute(x)
    con.commit()

def changepin(): 
    
    global en1,SearchBtn,lb1,lb2,en2,lb3,en3,lb4,en4, headingLabel,num,Id

    destroys()
    #   change pin
    headingLabel = Label(displayFrame, text="change pin",font=("Times New Roman",26,'bold'), bg='white')
    headingLabel.place(relx=0.35,rely=0.05)

    # Account No
    lb1 = Label(displayFrame,text="Account No : ",font=("arial",12,'bold'),bg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    en1 = Label(displayFrame,text=Id,font=("arial",14,'bold'),bg='#FFDFA4')
    en1.place(relx=0.3,rely=0.2, relwidth=0.62)
   
    # Previous password
    lb2 = Label(displayFrame,text="Previous password : ",font=("arial",12,'bold'), bg='white')
    lb2.place(relx=0.05,rely=0.35)
        
    en2 = Entry(displayFrame,font=("arial",12,'bold'),bg='#FFDFA4')
    en2.place(relx=0.3,rely=0.35, relwidth=0.62)

    # New password
    lb3 = Label(displayFrame,text="New password :",font=("arial",12,'bold'),bg='white')
    lb3.place(relx=0.05,rely=0.5)
        
    en3 = Entry(displayFrame, font=("arial",12,'bold'), bg='#FFDFA4')
    en3.place(relx=0.3,rely=0.5, relwidth=0.62)
        
    # Confirm password 
    lb4 = Label(displayFrame,text="Confirm password : ",font=("arial",12,'bold'),bg='white')
    lb4.place(relx=0.05,rely=0.65)
        
    en4 = Entry(displayFrame,font=("arial",12,'bold'), bg='#FFDFA4')
    en4.place(relx=0.3,rely=0.65, relwidth=0.62)

    
    
    # change pin Button
    SearchBtn = Button(displayFrame,text="change pin",font=('arial',12,'bold'),bg='white',command=updatepassword)
    SearchBtn.place(relx=0.66,rely=0.75, relwidth=0.18,relheight=0.08)

    

    num=6

def updatepassword() :
    global Id
    paswd=en4.get()
    sql="update accountdetail set password="+paswd+" where account_no=%s;"%(Id,)
    cur.execute(sql)
    con.commit()
    
def passbooks():
    global scroll_y, account_table,num,headingLabel,name

    destroys()
    
    scroll_y=Scrollbar(displayFrame,orient=VERTICAL)
    account_table=ttk.Treeview(displayFrame,columns=("account_no","status","amount"),yscrollcommand=scroll_y.set)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.config(command=account_table.yview)
    account_table.heading("account_no",text="Account_NO.")
    account_table.heading("status",text="Status")
    account_table.heading("amount",text="Amount")
    account_table["show"]="headings"
    account_table.column("account_no",width=50)
    account_table.column("status",width=50)
    account_table.column("amount",width=50)
    account_table.pack(fill=BOTH,expand=1)

    num=8


    getBooks = "select * from "+name
    try:
        cur.execute(getBooks)
        con.commit()
        rows=cur.fetchall()
        for row in rows:
            account_table.insert('',END,values=row)
    except:
        messagebox.showinfo("Error","Can't fetch data from database")

#################################### MENU #######################################################
headingFrame = Frame(root,bd=20, relief=RIDGE)
headingFrame.place(relx=0,rely=0,relwidth=1,relheight=0.2)
heading=Label(headingFrame,font=('Times New ROman', 40, 'bold'), text="Bank Management System")
heading.place(relx=0, rely=0.2)

moduleFrame = Frame(root,bd=20, relief=RIDGE)
moduleFrame.place(relx=0,rely=0.2,relwidth=0.2,relheight=0.8)

headingLabel = Label(moduleFrame, text="MENU",font=("Times New Roman",26,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=0.15)

dFrame= Frame(root,bd=20, relief=RIDGE)
dFrame.place(relx=0.2,rely=0.2,relwidth=0.8,relheight=0.8)

displayFrame=Frame(dFrame, bd=10, relief=SOLID, bg='white')
displayFrame.place(relx=0.2,rely=0.05, relwidth=0.6, relheight=0.9)
########################################### Interface for login and registration ############################################
lb1=Label(headingFrame,text='Account no. :',font=('arial', 12,'bold'))
lb1.place(relx=0.63, rely=0.01)

ent1=Entry(headingFrame, font=('arial', 12,'bold'))
ent1.place(relx=0.7, rely=0.01, relwidth=0.15)

#Name
lb2=Label(headingFrame,text='Name:',font=('arial', 12,'bold'))
lb2.place(relx=0.63, rely=0.25)

ent2=Entry(headingFrame, font=('arial', 12,'bold'))
ent2.place(relx=0.7, rely=0.25, relwidth=0.15)

#Password
lb3=Label(headingFrame,text='Password:',font=('arial', 12,'bold'))
lb3.place(relx=0.63, rely=0.48)

ent3=Entry(headingFrame, font=('arial', 12,'bold'),show="\u2022")
ent3.place(relx=0.7, rely=0.48, relwidth=0.15)




Menu()
root.mainloop()

