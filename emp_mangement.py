from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.ttk import Treeview
import mysql.connector as ms
import time
import random

# Add New Employee
def addemployee():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        job = jobval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        
        try:
            strr = 'insert into employeedata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,job,dob,addeddate,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notifications','Id {} Name {} Added successfully.. and want to clean the form'.format(id,name),parent=addroot)
            if(res==True):
                idval.set('')
                nameval.set("")
                mobileval.set("")
                emailval.set("")
                addressval.set("")
                genderval.set("")
                jobval.set("")
                dobval.set("")
        except:
            messagebox.showerror('Notifications','Id Already Exist try another id...', parent=addroot)
        
        strr = 'select * from employeedata'
        mycursor.execute(strr)
        data = mycursor.fetchall()
        employeetable.delete(*employeetable.get_children())
        for i in data:
            row = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]]
            employeetable.insert('',END,values=row)

    addroot = Toplevel(master=entryframe)
    addroot.grab_set()
    addroot.geometry('470x540+220+100')
    addroot.title('Add New Employee')
    addroot.config(bg='lavender')
    addroot.resizable(False,False)

    # Add Employee Labels
    idlabel = Label(addroot,text='Enter Id :',bg='silver',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10, y=10)
    namelabel = Label(addroot,text='Enter Name :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12, anchor='w')
    namelabel.place(x=10, y=70)
    mobilelabel = Label(addroot,text='Enter Mobile :',bg='silver',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12, anchor='w')
    mobilelabel.place(x=10, y=130)
    emaillabel = Label(addroot, text='Enter Email :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12, anchor='w')
    emaillabel.place(x=10, y=190)
    addresslabel = Label(addroot,text='Enter Address :',bg='silver',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10, y=250)
    genderlabel = Label(addroot,text='Enter Gender :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10, y=310)
    joblabel = Label(addroot,text='Enter Job :',bg='silver',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    joblabel.place(x=10, y=370)
    doblabel = Label(addroot,text='Enter D.O.B:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10, y=430)

    # Add Employee Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    jobval = StringVar()
    dobval = StringVar()
    
    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250, y=10)
    mobileentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250, y=130)
    emailentry = Entry(addroot, font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250, y=190)
    addressentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250, y=250)
    genderentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250, y=310)
    jobentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=jobval)
    jobentry.place(x=250, y=370)
    dobentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250, y=430)

    # Add Employee Submit Button
    submitbtn = Button(addroot,text='Submit',font=('roman',15,'bold'), width=20,bd=5, activebackground='blue',activeforeground='white',bg='tomato',command=submitadd)
    submitbtn.place(x=150, y=490)

# Search Employee
def searchemployee():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        job = jobval.get()
        dob = dobval.get()
        date = time.strftime("%d/%m/%Y")
        
        if(id != ''):
            strr = 'select *from employeedata where id=%s'
            mycursor.execute(strr,(id,))
            datas = mycursor.fetchall()
            employeetable.delete(*employeetable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]]
                employeetable.insert('',END,values=vv)
        elif(name != ''):
            strr = 'select *from employeedata where name=%s'
            mycursor.execute(strr,(name,))
            datas = mycursor.fetchall()
            employeetable.delete(*employeetable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]]
                employeetable.insert('',END,values=vv)
        elif(mobile != ""):
            strr = 'select *from employeedata where mobile=%s'
            mycursor.execute(strr,(mobile,))
            datas = mycursor.fetchall()
            employeetable.delete(*employeetable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]]
                employeetable.insert('',END,values=vv)
        elif(email != ""):
            strr = 'select *from employeedata where email=%s'
            mycursor.execute(strr,(email,))
            datas = mycursor.fetchall()
            employeetable.delete(*employeetable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]]
                employeetable.insert('',END,values=vv)
        elif(address != ""):
            strr = 'select *from employeedata where address=%s'
            mycursor.execute(strr,(address,))
            datas = mycursor.fetchall()
            employeetable.delete(*employeetable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]]
                employeetable.insert('',END,values=vv)
        elif(gender != ""):
            strr = 'select *from employeedata where gender=%s'
            mycursor.execute(strr,(gender,))
            datas = mycursor.fetchall()
            employeetable.delete(*employeetable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]]
                employeetable.insert('',END,values=vv)
        elif(job != ''):
            strr = 'select *from employeedata where job=%s'
            mycursor.execute(strr,(job,))
            datas = mycursor.fetchall()
            employeetable.delete(*employeetable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]]
                employeetable.insert('',END,values=vv)
        elif(dob != ""):
            strr = 'select *from employeedata where dob=%s'
            mycursor.execute(strr,(dob,))
            datas = mycursor.fetchall()
            employeetable.delete(*employeetable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]]
                employeetable.insert('',END,values=vv)
        elif(date != ''):
            strr = 'select *from employeedata where date=%s'
            mycursor.execute(strr,(date,))
            datas = mycursor.fetchall()
            employeetable.delete(*employeetable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]]
                employeetable.insert('',END,values=vv)

    searchroot = Toplevel(master=entryframe)
    searchroot.grab_set()
    searchroot.geometry('470x585+220+100')
    searchroot.title('EMPLOYEE SEARCH')
    searchroot.config(bg='navy')
    searchroot.resizable(False,False)

    # Search Employee Labels
    idlabel = Label(searchroot,text='Enter Id :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10, y=10)
    namelabel = Label(searchroot,text='Enter Name :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10, y=70)
    mobilelabel = Label(searchroot,text='Enter Mobile :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)
    emaillabel = Label(searchroot, text='Enter Email :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10, y=190)
    addresslabel = Label(searchroot,text='Enter Address :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10, y=250)
    genderlabel = Label(searchroot,text='Enter Gender :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10, y=310)
    joblabel = Label(searchroot,text='Enter Job :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    joblabel.place(x=10, y=370)
    doblabel = Label(searchroot,text='Enter D.O.B :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10, y=430)
    datelabel = Label(searchroot,text='Enter Hiredate :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10, y=490)

    # Search Employee Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    jobval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250, y=10)
    nameentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250, y=70)
    mobileentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250, y=130)
    emailentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250, y=190)
    addressentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250, y=250)
    genderentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250, y=310)
    jobentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=jobval)
    jobentry.place(x=250, y=370)
    dobentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250, y=430)
    dateentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250, y=490)

    # Search Employee Submit Button
    submitbtn = Button(searchroot,text='Submit',font=('roman',15,'bold'), width=20,bd=5, activebackground='blue',activeforeground='white',bg='red',command=search)
    submitbtn.place(x=150, y=540)

# Delete Employee
def deleteemployee():
    focus = employeetable.focus()
    content = employeetable.item(focus)
    val = content['values'][0]
    strr = 'delete from employeedata where id=%s'
    mycursor.execute(strr,(val,))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted successfully...'.format(val))
    
    strr = 'select * from employeedata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    employeetable.delete(*employeetable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]]
        employeetable.insert('',END,values=vv)

# Update Employee
def updateemployee():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        job = jobval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()
        
        strr = 'update employeedata set name=%s, mobile=%s, email=%s, address=%s, gender=%s, job=%s, dob=%s, date=%s, time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,job,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified successfully...'.format(id), parent=updateroot)
        
        strr = 'select *from employeedata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        employeetable.delete(*employeetable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]]
            employeetable.insert('',END,values=vv)

    updateroot = Toplevel(master=entryframe)
    updateroot.grab_set()
    updateroot.geometry('470x685+220+50')
    updateroot.title('Update Employee')
    updateroot.config(bg='firebrick1')
    updateroot.resizable(False,False)

    # Update Employee Labels
    
    idlabel = Label(updateroot,text='Enter Id :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10, y=10)
    namelabel = Label(updateroot,text='Enter Name :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10, y=70)
    mobilelabel = Label(updateroot,text='Enter Mobile :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10, y=130)
    emaillabel = Label(updateroot,text='Enter Email :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10, y=190)
    addresslabel = Label(updateroot,text='Enter Address :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10, y=250)
    genderlabel = Label(updateroot,text='Enter Gender :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10, y=310)
    joblabel = Label(updateroot,text='Enter Job :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    joblabel.place(x=10, y=370)
    doblabel = Label(updateroot,text='Enter D.O.B :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10, y=430)
    datelabel = Label(updateroot,text='Enter Hiredate :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10, y=490)
    timelabel = Label(updateroot,text='Enter Hiretime :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    timelabel.place(x=10, y=550)

    # Update Employee Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    jobval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250, y=10)
    nameentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250, y=70)
    mobileentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250, y=130)
    emailentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250, y=190)
    addressentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250, y=250)
    genderentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250, y=310)
    jobentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=jobval)
    jobentry.place(x=250, y=370)
    dobentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250, y=430)
    dateentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250, y=490)
    timeentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=timeval)
    timeentry.place(x=250, y=550)

    # Update Employee Submit Button
    submitbtn = Button(updateroot,text='Submit',font=('roman',15,'bold'), width=20,bd=5, activebackground='blue',activeforeground='white',bg='red',command=update)
    submitbtn.place(x=150, y=600)

    # Show Employee
    def showemployee():
        strr = 'select *from employeedata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        employeetable.delete(*employeetable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]]
            employeetable.insert('',END,values=vv)

    # Exit
    def exitemployee():
        res = messagebox.askyesnocancel('Notification','Do you want to exit?')
        if(res == True):
            w.destroy()

    # Connection of Database
    def connectdb():
        def submitdb():
            global con, mycursor
            host = hostval.get()
            user = userval.get()
            password = passwordval.get()
            try:
                con = ms.connect(host=host,user=user,password=password)
                mycursor = con.cursor()
            except:
                messagebox.showerror('Notifications','Data is incorrect please try again',parent=dbroot)
                return
            try:
                strr = 'create database employeemanagementsystem'
                mycursor.execute(strr)
                strr = 'use employeemanagementsystem'
                mycursor.execute(strr)
                strr = 'create table employeedata(id int not null PRIMARY KEY, name varchar(20), mobile varchar(12), email varchar(30), address varchar(100), gender varchar(50), job varchar(50), dob varchar(50), date varchar(50),time varchar(50))'
                mycursor.execute(strr)
                messagebox.showinfo('Notification','database created and now you are connected connected to the database ....', parent=dbroot)
            except:
                strr = 'use employeemanagementsystem'
                mycursor.execute(strr)
                messagebox.showinfo('Notification','Now you are connected to the database .',parent=dbroot)
            dbroot.destroy()

        dbroot = Toplevel()
        dbroot.grab_set()
        dbroot.title('Database Connection')
        dbroot.geometry('470x250+800+230')
        dbroot.resizable(False,False)
        dbroot.config(bg='palegreen')

        # Connection Labels
        hostlabel = Label(dbroot,text="Enter Hostname :",bg='azure',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
        hostlabel.place(x=10, y=10)
        userlabel = Label(dbroot,text="Enter Username :",bg='azure',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
        userlabel.place(x=10, y=70)
        passwordlabel = Label(dbroot,text="Enter Password :",bg='azure',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
        passwordlabel.place(x=10, y=130)

        # Connection Entry
        hostval = StringVar()
        userval = StringVar()
        passwordval = StringVar()
        hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
        hostentry.place(x=250, y=10)
        userentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
        userentry.place(x=250, y=70)
        passwordentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval)
        passwordentry.place(x=250, y=130)

        # Connection Button
        submitbutton = Button(dbroot,text='Submit',font=('roman',15,'bold'),bg='gold2',bd=5,width=20,activebackground='blue',activeforeground='white',command=submitdb)
        submitbutton.place(x=150, y=190)

    # Front Label
    frontlabel = Label(entryframe, text='Welcome', width=50,font=('arial',22,'italic bold'),bg='gold2')
    frontlabel.pack()

    # Buttons
    addbtn = Button(entryframe,text='1.Add Employee',width=18,font=('chiller',15,'bold'),bd=6,bg='wheat',activebackground='blue',relief=RIDGE,activeforeground='white',command=addemployee)
    addbtn.pack(side=TOP,expand=True)
    searchbtn = Button(entryframe,text='2.Search Employee',width=18,font=('chiller',15,'bold'),bd=6,bg='wheat',activebackground='blue',relief=RIDGE,activeforeground='white',command=searchemployee)
    searchbtn.pack(side=TOP,expand=True)
    deletebtn = Button(entryframe,text='3.Delete Employee',width=18,font=('chiller',15,'bold'),bd=6,bg='wheat',activebackground='blue',relief=RIDGE,activeforeground='white',command=deleteemployee)
    deletebtn.pack(side=TOP,expand=True)
    updatebtn = Button(entryframe,text='4.Update Employee',width=18,font=('chiller',15,'bold'),bd=6,bg='wheat',activebackground='blue',relief=RIDGE,activeforeground='white',command=updateemployee)
    updatebtn.pack(side=TOP,expand=True)
    showallbtn = Button(entryframe,text='5.Show All Data',width=18,font=('chiller',15,'bold'),bd=6,bg='wheat',activebackground='blue',relief=RIDGE,activeforeground='white',command=showemployee)
    showallbtn.pack(side=TOP,expand=True)
    exitbtn = Button(entryframe,text='6.Exit',width=18,font=('chiller',15,'bold'),bd=6,bg='wheat',activebackground='blue',relief=RIDGE,activeforeground='white',command=exitemployee)
    exitbtn.pack(side=TOP,expand=True)

    # Show Data Frame
    showframe = Frame(w,bg="white",relief=SOLID,borderwidth=5)
    showframe.place(x=500,y=80,width=850,height=600)

    # Employee Table
    style = ttk.Style()
    style.configure('Treeview.Heading',font=('chiller',15,'bold'),foreground='blue')
    style.configure('Treeview',font=('times',15,'bold'),background='blue',foreground='black')
    scroll_x = Scrollbar(showframe,orient=HORIZONTAL)
    scroll_y = Scrollbar(showframe,orient=VERTICAL)
    employeetable = Treeview(showframe,columns=('Id','Name','Mobile No','Email','Address','Gender','Job','D.O.B','Hiredate','Hiretime'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=employeetable.xview)
    scroll_y.config(command=employeetable.yview)
    employeetable.heading('Id',text='Id')
    employeetable.heading('Name',text='Name')
    employeetable.heading('Mobile No',text='Mobile No')
    employeetable.heading('Email',text='Email')
    employeetable.heading('Address',text='Address')
    employeetable.heading('Gender',text='Gender')
    employeetable.heading('Job',text='Job')
    employeetable.heading('D.O.B',text='D.O.B')
    employeetable.heading('Hiredate',text='Hiredate')
    employeetable.heading('Hiretime',text='Hiretime')
    employeetable['show'] = 'headings'
    employeetable.column('Id',width=100)
    employeetable.column('Name',width=200)
    employeetable.column('Mobile No',width=200)
    employeetable.column('Email',width=300)
    employeetable.column('Address',width=200)
    employeetable.column('Gender',width=100)
    employeetable.column('Job',width=200)
    employeetable.column('D.O.B',width=150)
    employeetable.column('Hiredate',width=150)
    employeetable.column('Hiretime',width=150)
    employeetable.pack(fill=BOTH,expand=1)

    # Slider
    sl = "Welcome To Employee Management System"
    count = 0
    text = ""
    sliderlabel = Label(w,text=sl,relief=GROOVE,borderwidth=5,bg="mintcream")
    sliderlabel.place(x=560,y=0)

    # Clock
    clock = Label(w,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='lightskyblue')
    clock.place(x=0,y=0)

    # Database Connection Button
    cbutton = Button(w,text="Connect To Database",width=33,font=('times',10,'bold'),borderwidth=4,relief=RIDGE,bg='lightskyblue',activebackground='pink',activeforeground='white',command=connectdb)
    cbutton.place(x=1130,y=0)

    w.mainloop()
