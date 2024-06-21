from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
top=Tk()
top.geometry('1500x600')        #1200:width,height:600
top.config(bg='green')
top.title('welcome')

def Login():

    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='arunidhi',db='project')
    cur=db.cursor()
    cur.execute("select*from emp where Name=%s and where Lastname=%s", (E1.get(), E2.get()))
    row=cur.fetchone()

    if row == None:
        messagebox.showerror("Error","Invalid User Name And Password")
    else:
        top.destroy()
        import welcome
    


def Exit():
    top.destroy 

p=StringVar()    

path="C:/Users/Administrator/Desktop/LIGHT.png"
img=ImageTk.PhotoImage(Image.open(path))
L2=Label(top,image=img)
L2.pack()


L=Label(top,text='Login Page',bg='white',fg='black',font=('Arial 25 bold'))
L.place(x=500,y=80)      #x:left(0) to right(100)|y:up(0) to down(100)        


L3=Label(top,text='Name',bg='green',fg='white',font=('Arial 20 bold'))
L3.place(x=300,y=200)
E1=Entry(top,font=('Arial 20 bold'))
E1.place(x=500,y=200)

L4=Label(top,text='Lastname',bg='green',fg='white',font=('Arial 20 bold'))
L4.place(x=300,y=250)
E2=Entry(top,font=('Arial 20 bold'),show="*")
E2.place(x=500,y=250)


B5=Button(top,text='login',font=('Arial 15 bold'),command=Login)
B5.place(x=500,y=300)


top.mainloop()     #ye mainloop design kiye hue page ko dikhata hai









