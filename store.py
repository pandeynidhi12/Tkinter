from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
top=Tk()
top.geometry('1500x600')        #1200:width,height:600
top.config(bg='green')
top.title('welcome')

path="C:/Users/admin/OneDrive/Desktop/flipkartLogo.jpg"
img=ImageTk.PhotoImage(Image.open(path))
L2=Label(top,image=img)
L2.pack()



L=Label(top,text='STORE',bg='lightgrey',fg='black',font=('Arial 25 bold'))
L.place(x=500,y=80)  


def insert():
    k=E1.get()
    k2=E2.get()
    k3=int(E3.get())
    k4=int(E4.get())
    k5=p.get()
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='india123',db='project')
    cur=db.cursor()      # cursor:cursor is a inbuilt method.to execute your query in python programming language.
    s="insert into emp values('%s','%s','%s','%s','%s')"%(k,k2,k3,k4,k5)
    result=cur.execute(s) 
    if(result>0):
        messagebox.showinfo("Result","Record insert successfully")
    else:  
        messagebox.showinfo("Result","Record  not inserted") 
    db.commit() 

    E1.delete(0,  'end')  
    E2.delete(0,  'end')
    E3.delete(0,  'end')
    E4.delete(0,  'end') 




def show():
    for i in tv.get_children():
        tv.delete(i)
        
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='india123',db='project')
    cur=db.cursor()
    s="select*from emp"
    cur.execute(s)
    result=cur.fetchall()
    for col in result:
        Name=col[0]
        Lastname=col[1]
        Salary=col[2]
        Age=col[3]
        Gender=col[4]
        tv.insert("", 'end', values=(Name,Lastname,Salary,Age,Gender))



def search():
    k=E8.get()
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='india123',db='project')
    cur=db.cursor()
    # p="select*from emp  where Name=%s"
    p="select*from emp  where name like '%s%%'" %k
    cur.execute(p)       #p=query,k=variable
    result=cur.fetchall()
    for col in result:
        Name=col[0]
        Lastname=col[1]
        Salary=col[2]
        Age=col[3]
        Gender=col[4]
        tv.insert("", 'end', values=(Name,Lastname,Salary,Age,Gender))


def delete():
    k=E8.get()
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='india123',db='project')
    cur=db.cursor()
    p="delete from emp where name=%s"
    result=cur.execute(p,k)
    if(result>0):
        messagebox.showinfo("Result","Record deleted")
    else:  
        messagebox.showinfo("Result","Record  not deleted") 
    db.commit() 

def Login():
    top.destroy ()  
    import Login                       


# #top.destroy ka mtlb hota hai ki current page band ho jana aur new page open ho jana.
def Exit():
    top.destroy 

p=StringVar()    

path="C:/Users/admin/OneDrive/Desktop/image.jpg"
img=ImageTk.PhotoImage(Image.open(path))
L2=Label(top,image=img)
L2.pack()


tv=ttk.Treeview(top)
tv['column']=('Name','Lastname','Salary','Age','Gender')
tv.column('#0',width=0,stretch=NO)
tv.column('Name',anchor=CENTER,width=150)
tv.column('Lastname',anchor=CENTER,width=150)
tv.column('Salary',anchor=CENTER,width=150)
tv.column('Age',anchor=CENTER,width=150)

tv.heading('Name',text='Name',anchor=CENTER)
tv.heading('Lastname',text='Lastname',anchor=CENTER)
tv.heading('Salary',text='Salary',anchor=CENTER)
tv.heading('Age',text='Age',anchor=CENTER)
tv.heading('Gender',text='Gender',anchor=CENTER)

tv.place(x=900,y=100)




L=Label(top,text='Registration',bg='lightgrey',fg='black',font=('Arial 25 bold'))
L.place(x=500,y=80)      #x:left(0) to right(100)|y:up(0) to down(100)        

L3=Label(top,text='Name',bg='green',fg='white',font=('Arial 20 bold'))
L3.place(x=300,y=200)
E1=Entry(top,font=('Arial 20 bold'))
E1.place(x=500,y=200)
L4=Label(top,text='Lastname',bg='green',fg='white',font=('Arial 20 bold'))
L4.place(x=300,y=250)
E2=Entry(top,font=('Arial 20 bold'))
E2.place(x=500,y=250)
L5=Label(top,text='Salary',bg='green',fg='white',font=('Arial 20 bold'))
L5.place(x=300,y=300)
E3=Entry(top,font=('Arial 20 bold'))
E3.place(x=500,y=300)

L6=Label(top,text='Age',bg='green',fg='white',font=('Arial 20 bold'))
L6.place(x=300,y=350)
E4=Entry(top,font=('Arial 20 bold'))
E4.place(x=500,y=350)

L7=Label(top,text='Gender',bg='green',fg='white',font=('Arial 20 bold'))
L7.place(x=300,y=400)

r1=Radiobutton(top,text='MALE',value='MALE',variable=p,font=('Arial 20 bold'))
r1.place(x=500,y=400)

r2=Radiobutton(top,text='FEMALE',value='FEMALE',variable=p,font=('Arial 20 bold'))
r2.place(x=600,y=400)

r1=Radiobutton(top,text='OTHERS',value='OTHERS',font=('Arial 20 bold'))
r1.place(x=740,y=400)

B2=Button(top,text='SUBMIT',font=('Arial 20 bold'),command=insert)
B2.place(x=550,y=500)


B3=Button(top,text='EXIT',font=('Arial 20 bold'),command=Exit)
B3.place(x=450,y=500)

B4=Button(top,text='SHOW',font=('Arial 20 bold'),command=show)
B4.place(x=700,y=500)

B5=Button(top,text='Search',font=('Arial 15 bold'),command=search)
B5.place(x=750,y=50)

B5=Button(top,text='Delete',font=('Arial 15 bold'),command=delete)
B5.place(x=800,y=500)


B5=Button(top,text='Login',font=('Arial 15 bold'),command=Login)
B5.place(x=900,y=500)





E8=Entry(top,font=('Arial 20 bold'))
E8.place(x=900,y=50)

top.mainloop()   
