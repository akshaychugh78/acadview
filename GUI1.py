#Question 1

from tkinter import *

root = Tk()
root.title('Welcome To Developer Phase')
root.geometry('400x400')

hwl = Label(root, text='Welcome To Developer Phase')
hwl.pack()

ext = Button(root,text='EXIT',width=25,command=root.destroy)
ext.pack(side=BOTTOM)

root.mainloop()

#Question 2

from tkinter import *

def pt():
    hwp= Label(root,text='Ready')
    hwp.pack()

root=Tk()
root.geometry('400x400')

hwl= Label(root,text='Welcome To Developer Phase')
hwl.pack()

prnt = Button(root,text='PRINT',width=25,command=pt)
prnt.place(relx=0.5, rely=0.5,anchor=CENTER)

ext = Button(root,text='EXIT',width=25,command = root.destroy)
ext.pack(side=BOTTOM)

root.mainloop()

#Question 3

from tkinter import *

root = Tk()
root.configure(background='black')
root.geometry('400x400')

def prt(var='Welcome To Developer Phase'):
    prnt= Label(root,text=var,bg='Blue')
    prnt.place(relx=0.5,rely=0.5,anchor=CENTER)
    
def change():
    var= 'Good Luck'
    prt(var)
    
f1= Frame(root,bg='green')
f1.pack(fill=X)

B1= Button(f1,text='Print',command=prt)
B1.pack()

B3= Button(f1,text='Change',command=change)
B3.pack()

f2= Frame(root, bg='blue')
f2.pack(fill=X,side=BOTTOM)

B2= Button(f2,text='EXIT',width=15,command=root.destroy)
B2.pack()

root.mainloop()


#Question 4

from tkinter import *

root=Tk()
root.geometry('400x400')

def prnt():
    str1=abc.get()
    z= Label(root,text=str1)
    z.place(relx=0.5,rely=0.5,anchor=CENTER)
     

na = Label(root,text='Enter Your Name')
na.grid(row=0,column=0)
abc = Entry(root)
abc.grid(row=0,column=1)

B1= Button(root,text='Print',command=prnt)
B1.grid(row=1,column=1)

root.mainloop()
