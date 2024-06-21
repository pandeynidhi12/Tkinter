from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
top=Tk()
top.geometry('1500x600')        #1200:width,height:600
top.config(bg='green')
top.title('welcome')
    

path="C:/Users/Administrator/Desktop/LIGHT.png"
img=ImageTk.PhotoImage(Image.open(path))
L2=Label(top,image=img)
L2.pack()


L=Label(top,text='WELCOME',bg='white',fg='black',font=('Arial 30 bold'))
L.place(x=600,y=80)      #x:left(0) to right(100)|y:up(0) to down(100)        


top.mainloop()     #ye mainloop design kiye hue page ko dikhata hai









